"""
Module dedicated to calibration of an urban building energy model.

Delft University of Technology
Dr. Miguel Martin
"""

from abc import ABCMeta, abstractmethod

import torch
import pygad
from eppy.modeleditor import IDF
import os
import platform
import numpy as np
import pandas as pd
import calendar
from enum import Enum
import json
import gpflow
import pickle
import pyro
import pyro.distributions as dist
from pyro.infer import MCMC, NUTS
import tensorflow as tf
from scipy.stats import gamma
from scipy.optimize import curve_fit


from sklearn.metrics import mean_squared_error

from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor

from SALib.analyze import morris
from SALib.sample import morris as morris_sampler
from SALib.sample import latin

from sciencespy.bem import *
from sciencespy.cosim import *
from sciencespy.dom import *

class CategoryParameterBuildingEnergyModel(Enum):
    """
    Enumeration of parameter caregories for a building energy model.
    """
    OCCUPANCY = 1
    LIGHTING = 2
    ELECTRIC_EQUIPMENT = 3
    INFILTRATION = 4
    WINDOW_TO_WALL_RATIO = 5
    WINDOW_THERMAL_RESISTANCE = 6
    WINDOW_SHGC = 7
    WALL_THERMAL_RESISTANCE = 8
    WALL_DENSITY = 9
    WALL_SPECIFIC_HEAT_CAPACITY = 10
    WALL_THERMAL_EMISSIVITY = 11
    WALL_THERMAL_ABSORPTIVITY = 12
    HEATING_TEMPERATURE_SETPOINT = 13
    COOLING_TEMPERATURE_SETPOINT = 14
    MECHANICAL_VENTILATION = 15

class ParameterBuildingEnergyModel():
    """
    Class representing the parameter of a building energy model to be calibrated.

    Attributes:
        name: name of the parameter
        _value: value of the parameter
    """
    __metaclass__ = ABCMeta

    def __init__(self, name = None):
        """
        :param name: name of the parameter.
        """
        self.name = name

    @abstractmethod
    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        pass

    @abstractmethod
    def get_value(self):
        """
        :return: value of the parameter
        """
        pass

    @abstractmethod
    def set_value(self, value):
        """
        :param value: value of the parameter.
        """
        pass

class ParameterEnergyPlusModel(ParameterBuildingEnergyModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """
    __metaclass__ = ABCMeta

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterBuildingEnergyModel.__init__(self, name)
        self.idf = idf

    def get_value(self):
        """
        :return: value of the parameter
        """
        object_name = self.name.split(':')[0]
        category_name = self.name.split(':')[1]
        for obj in self.idf.idfobjects[self.get_classname()]:
            if self.get_name(obj) == object_name and category_name == self.get_category_name():
                return self.get_field_value(obj)
        return None

    def set_value(self, value):
        """
        :param value: value of the parameter.
        """
        object_name = self.name.split(':')[0]
        category_name = self.name.split(':')[1]
        for obj in self.idf.idfobjects[self.get_classname()]:
            if self.get_name(obj) == object_name and category_name == self.get_category_name():
                self.update(obj, value)

    @abstractmethod
    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        pass

    @abstractmethod
    def get_category_name(self):
        """
        :return: name of the category of the parameter
        """
        pass

    @abstractmethod
    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        pass

    @abstractmethod
    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        pass

    @abstractmethod
    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        pass

class ParameterEnergyPlusModelOccupancy(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.OCCUPANCY

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'PEOPLE'

    def get_category_name(self):
        """
        :return:
        """
        return 'Occupancy'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Number_of_People)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Number_of_People_Calculation_Method = 'People'
        obj.Number_of_People = "{:.2f}".format(round(value, 2))
        obj.People_per_Floor_Area = ''
        obj.Floor_Area_per_Person = ''


class ParameterEnergyPlusModelLighting(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.LIGHTING

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'LIGHTS'

    def get_category_name(self):
        """
        :return:
        """
        return 'Lighting Level'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Lighting_Level)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Design_Level_Calculation_Method = 'LightingLevel'
        obj.Lighting_Level = "{:.2f}".format(round(value, 2))
        obj.Watts_per_Zone_Floor_Area = ''
        obj.Watts_per_Person = ''


class ParameterEnergyPlusModelElectricEquipment(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.ELECTRIC_EQUIPMENT

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'ELECTRICEQUIPMENT'

    def get_category_name(self):
        """
        :return:
        """
        return 'Electric Equipment Level'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Design_Level)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Design_Level_Calculation_Method = 'EquipmentLevel'
        obj.Design_Level = "{:.2f}".format(round(value, 2))
        obj.Watts_per_Zone_Floor_Area = ''
        obj.Watts_per_Person = ''


class ParameterEnergyPlusModelInfiltration(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.INFILTRATION

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'ZONEINFILTRATION:DESIGNFLOWRATE'

    def get_category_name(self):
        """
        :return:
        """
        return 'Infiltration Flow Rate'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Design_Flow_Rate)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Design_Flow_Rate_Calculation_Method = 'Flow/Zone'
        obj.Design_Flow_Rate = "{:.2f}".format(round(value, 2))
        obj.Flow_Rate_per_Floor_Area = ''
        obj.Flow_Rate_per_Exterior_Surface_Area = ''
        obj.Air_Changes_per_Hour = ''

class FactorySurface():
    """"
    Class used to create surface from IDF object.

    Attributes:
        surface_idfobject: the IDF object containing information of the surface.
    """


    __metaclass__ = ABCMeta

    def __init__(self, surface_idfobject):
        """
        :param surface_idfobject: the IDF object containing information of the surface.
        """
        self.surface_idfobject = surface_idfobject

    def get_surface(self):
        """
        :return: the corresponding dom.Surface object.
        """
        coords_position_0 = self.get_position_initial_x()
        coords = [None, None, None]
        points = []
        for n, field in enumerate(self.surface_idfobject.obj):
            if n >= coords_position_0 and str(field).strip():
                coords[(n - coords_position_0) % 3] = float(field)
                if not any(coord is None for coord in coords):
                    points.append(coords)
                    coords = [None, None, None]
        return Surface(self.surface_idfobject.Name, np.array(points))


    @abstractmethod
    def get_position_initial_x(self):
        """
        :return: the position in the IDF object of the first x-coordinate.
        """
        pass

class FactorySurfaceExteriorWall(FactorySurface):
    """"
    Class used to create surface from IDF object.

    Attributes:
        surface_idfobject: the IDF object containing information of the surface.
    """

    def __init__(self, surface_idfobject):
        """
        :param surface_idfobject: the IDF object containing information of the surface.
        """
        FactorySurface.__init__(self, surface_idfobject)


    def get_position_initial_x(self):
        """
        :return: the position in the IDF object of the first x-coordinate.
        """
        return 12


class FactorySurfaceExteriorWindow(FactorySurface):
    """"
    Class used to create surface from IDF object.

    Attributes:
        surface_idfobject: the IDF object containing information of the surface.
    """

    def __init__(self, surface_idfobject):
        """
        :param surface_idfobject: the IDF object containing information of the surface.
        """
        FactorySurface.__init__(self, surface_idfobject)

    def get_position_initial_x(self):
        """
        :return: the position in the IDF object of the first x-coordinate.
        """
        return 10

def add_imaginary_exterior_window_layer(idf):
    """
    Add an imaginary exterior window layer to the IDF
    :param idf: IDF file contain
    :return: IDF object corresponding to the imaginary exterior window layer.
    """
    is_imaginary_exterior_window = False
    for obj in idf.idfobjects['WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM']:
        if obj.Name == 'Imaginary Exterior Window Layer':
            is_imaginary_exterior_window = True
            break
    if not is_imaginary_exterior_window:
        idf.newidfobject('WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM')
        materials = idf.idfobjects['WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM']
        exterior_window_layer = materials[-1]
        exterior_window_layer.Name = 'Imaginary Exterior Window Layer'
        exterior_window_layer.UFactor = '1.5'
        exterior_window_layer.Solar_Heat_Gain_Coefficient = '0.7'
        exterior_window_layer.Visible_Transmittance = ''
        idf.newidfobject("CONSTRUCTION")
        constructions = idf.idfobjects["CONSTRUCTION"]
        constructions[-1].Name = 'Imaginary Exterior Window'
        constructions[-1].Outside_Layer = 'Imaginary Exterior Window Layer'
    else:
        for obj in idf.idfobjects['WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM']:
            if obj.Name == 'Imaginary Exterior Window Layer':
                exterior_window_layer = obj
    for obj in idf.idfobjects["FENESTRATIONSURFACE:DETAILED"]:
        if obj.Surface_Type == 'Window':
            obj.Construction_Name = 'Imaginary Exterior Window'
    return exterior_window_layer


class ParameterEnergyPlusModelWindowToWallRatio(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WINDOW_TO_WALL_RATIO

    def get_value(self):
        """
        :return: value of the parameter
        """
        total_wall_surface = 0
        total_window_surface = 0
        for obj in self.idf.idfobjects["BUILDINGSURFACE:DETAILED"]:
            if obj.Surface_Type == 'Wall' and obj.Sun_Exposure == 'SunExposed' and obj.Wind_Exposure == 'WindExposed':
                total_wall_surface += FactorySurfaceExteriorWall(obj).get_surface().get_area()
        for obj in self.idf.idfobjects["FENESTRATIONSURFACE:DETAILED"]:
            if obj.Surface_Type == 'Window':
                total_window_surface += FactorySurfaceExteriorWindow(obj).get_surface().get_area()
        return total_window_surface.m / total_wall_surface.m

    def set_value(self, value):
        """
        :param value: value of the parameter.
        """
        window_surfaces = self.idf.idfobjects["FENESTRATIONSURFACE:DETAILED"]
        while len(window_surfaces) > 0:
            window_surfaces.pop(0)
        if value > 0:
            for obj in self.idf.idfobjects["BUILDINGSURFACE:DETAILED"]:
                if obj.Surface_Type == 'Wall' and obj.Sun_Exposure == 'SunExposed' and obj.Wind_Exposure == 'WindExposed':
                    wall_surface = FactorySurfaceExteriorWall(obj).get_surface()
                    window_surface = wall_surface.crop(value).bounding_box()
                    self.idf.newidfobject("FENESTRATIONSURFACE:DETAILED")
                    window_surface_idf = self.idf.idfobjects["FENESTRATIONSURFACE:DETAILED"][-1]
                    window_surface_idf.Name = obj.Name + ":Window"
                    window_surface_idf.Surface_Type = 'Window'
                    window_surface_idf.Building_Surface_Name = obj.Name
                    window_surface_idf.View_Factor_to_Ground = 'autocalculate'
                    window_surface_idf.Multiplier = '1'
                    num_vertices = 4
                    window_surface_idf.Number_of_Vertices = str(num_vertices)
                    for n_vertice in range(num_vertices):
                        window_surface_idf["Vertex_" + str(n_vertice + 1) + "_Xcoordinate"] = str(window_surface.points[n_vertice][0])
                        window_surface_idf["Vertex_" + str(n_vertice + 1) + "_Ycoordinate"] = str(window_surface.points[n_vertice][1])
                        window_surface_idf["Vertex_" + str(n_vertice + 1) + "_Zcoordinate"] = str(window_surface.points[n_vertice][2])
            add_imaginary_exterior_window_layer(self.idf)


class ParameterEnergyPlusModelExteriorWindow(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    __metaclass__ = ABCMeta

    def __init__(self, name = None, idf = None):
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def set_value(self, value):
        exterior_window_layer = add_imaginary_exterior_window_layer(self.idf)
        self.update(exterior_window_layer, value)


class ParameterEnergyPlusModelWindowThermalResistance(ParameterEnergyPlusModelExteriorWindow):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModelExteriorWindow.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WINDOW_THERMAL_RESISTANCE

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM'

    def get_category_name(self):
        """
        :return:
        """
        return 'Window Thermal Resistance'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.UFactor)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.UFactor = "{:.2f}".format(round(value, 2))

class ParameterEnergyPlusModelWindowSolarHeatGainCoefficient(ParameterEnergyPlusModelExteriorWindow):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModelExteriorWindow.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WINDOW_SHGC

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM'

    def get_category_name(self):
        """
        :return:
        """
        return 'Window Solar Heat Gain Coefficient'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Solar_Heat_Gain_Coefficient)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Solar_Heat_Gain_Coefficient = "{:.2f}".format(round(value, 2))

class ParameterEnergyPlusModelExteriorWall(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    __metaclass__ = ABCMeta

    def __init__(self, name = None, idf = None):
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def set_value(self, value):
        is_imaginary_exterior_wall = False
        for obj in self.idf.idfobjects['MATERIAL']:
            if obj.Name == 'Imaginary Exterior Wall Outer Layer' or obj.Name == 'Imaginary Exterior Wall Inner Layer':
                is_imaginary_exterior_wall = True
                break
        if not is_imaginary_exterior_wall:
            self.idf.newidfobject("MATERIAL")
            materials = self.idf.idfobjects["MATERIAL"]
            exterior_wall_outer_layer = materials[-1]
            exterior_wall_outer_layer.Name = 'Imaginary Exterior Wall Outer Layer'
            exterior_wall_outer_layer.Roughness = 'MediumSmooth'
            exterior_wall_outer_layer.Thickness = 0.5
            exterior_wall_outer_layer.Conductivity = 0.1
            exterior_wall_outer_layer.Density = 500
            exterior_wall_outer_layer.Specific_Heat = 1000
            exterior_wall_outer_layer.Thermal_Absorptance = 0.9
            exterior_wall_outer_layer.Solar_Absorptance = 0.7
            exterior_wall_outer_layer.Visible_Absorptance = 0.7
            self.idf.newidfobject("MATERIAL")
            materials = self.idf.idfobjects["MATERIAL"]
            exterior_wall_inner_layer = materials[-1]
            exterior_wall_inner_layer.Name = 'Imaginary Exterior Wall Inner Layer'
            exterior_wall_inner_layer.Roughness = 'MediumSmooth'
            exterior_wall_inner_layer.Thickness = 0.5
            exterior_wall_inner_layer.Conductivity = 0.1
            exterior_wall_inner_layer.Density = 500
            exterior_wall_inner_layer.Specific_Heat = 1000
            exterior_wall_inner_layer.Thermal_Absorptance = 0.9
            exterior_wall_inner_layer.Solar_Absorptance = 0.7
            exterior_wall_inner_layer.Visible_Absorptance = 0.7
            self.idf.newidfobject("CONSTRUCTION")
            constructions = self.idf.idfobjects["CONSTRUCTION"]
            constructions[-1].Name = 'Imaginary Exterior Wall'
            constructions[-1].Outside_Layer = 'Imaginary Exterior Wall Outer Layer'
            constructions[-1].Layer_2 = 'Imaginary Exterior Wall Inner Layer'
            for obj in self.idf.idfobjects["BUILDINGSURFACE:DETAILED"]:
                if obj.Surface_Type == 'Wall' and obj.Sun_Exposure == 'SunExposed' and obj.Wind_Exposure == 'WindExposed':
                    obj.Construction_Name = 'Imaginary Exterior Wall'
        else:
            for obj in self.idf.idfobjects["MATERIAL"]:
                if obj.Name == 'Imaginary Exterior Wall Outer Layer':
                    exterior_wall_outer_layer = obj
                elif obj.Name == 'Imaginary Exterior Wall Inner Layer':
                    exterior_wall_inner_layer = obj
        self.update(exterior_wall_outer_layer, value)
        self.update(exterior_wall_inner_layer, value)

class ParameterEnergyPlusModelWallThermalResistance(ParameterEnergyPlusModelExteriorWall):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WALL_THERMAL_RESISTANCE

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'MATERIAL'

    def get_category_name(self):
        """
        :return:
        """
        return 'Wall Thermal Resistance'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return 1 / float(obj.Conductivity)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Conductivity = "{:.2f}".format(round(1 / value, 2))

class ParameterEnergyPlusModelWallDensity(ParameterEnergyPlusModelExteriorWall):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModelExteriorWall.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WALL_DENSITY

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'MATERIAL'

    def get_category_name(self):
        """
        :return:
        """
        return 'Wall Density'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Density)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Density = str(round(value))

class ParameterEnergyPlusModelWallSpecificHeatCapacity(ParameterEnergyPlusModelExteriorWall):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModelExteriorWall.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WALL_SPECIFIC_HEAT_CAPACITY

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'MATERIAL'

    def get_category_name(self):
        """
        :return:
        """
        return 'Wall Specific Heat Capacity'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Specific_Heat)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Specific_Heat = str(round(value))

class ParameterEnergyPlusModelWallThermalEmissivity(ParameterEnergyPlusModelExteriorWall):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name=None, idf=None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModelExteriorWall.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WALL_THERMAL_EMISSIVITY

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'MATERIAL'

    def get_category_name(self):
        """
        :return:
        """
        return 'Wall Thermal Emissivity'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Thermal_Absorptance)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        if obj.Name == 'Imaginary Exterior Wall Outer Layer':
            obj.Thermal_Absorptance = "{:.2f}".format(round(value, 2))

class ParameterEnergyPlusModelWallThermalAbsorptivity(ParameterEnergyPlusModelExteriorWall):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name=None, idf=None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModelExteriorWall.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.WALL_THERMAL_ABSORPTIVITY

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'MATERIAL'

    def get_category_name(self):
        """
        :return:
        """
        return 'Wall Thermal Absorptivity'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Solar_Absorptance)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        if obj.Name == 'Imaginary Exterior Wall Outer Layer':
            obj.Solar_Absorptance = "{:.2f}".format(round(value, 2))

class ParameterEnergyPlusModelHeatingTemperatureSetpoint(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.HEATING_TEMPERATURE_SETPOINT

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'HVACTEMPLATE:THERMOSTAT'

    def get_category_name(self):
        """
        :return:
        """
        return 'Heating Setpoint'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Constant_Heating_Setpoint)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Heating_Setpoint_Schedule_Name = ''
        obj.Constant_Heating_Setpoint = "{:.2f}".format(round(value, 2))


class ParameterEnergyPlusModelCoolingTemperatureSetpoint(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.COOLING_TEMPERATURE_SETPOINT

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'HVACTEMPLATE:THERMOSTAT'

    def get_category_name(self):
        """
        :return:
        """
        return 'Cooling Setpoint'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Constant_Cooling_Setpoint)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Cooling_Setpoint_Schedule_Name = ''
        obj.Constant_Cooling_Setpoint = "{:.2f}".format(round(value, 2))


class ParameterEnergyPlusModelMechanicalVentilation(ParameterEnergyPlusModel):
    """
    Class representing the parameter of an EnergyPlus model to be calibrated.

    Attributes:
        name: name of the parameter
        idf: list of IDF objects representing the EnergyPlus model.
    """

    def __init__(self, name = None, idf = None):
        """
        :param name: name of the parameter.
        :param idf: list of IDF objects representing the EnergyPlus model.
        """
        ParameterEnergyPlusModel.__init__(self, name, idf)

    def get_category(self):
        """
        :return: category of parameter of the building energy model.
        """
        return CategoryParameterBuildingEnergyModel.MECHANICAL_VENTILATION

    def get_classname(self):
        """
        :return: name of the class of the EnergyPlus object
        """
        return 'HVACTEMPLATE:ZONE:IDEALLOADSAIRSYSTEM'

    def get_category_name(self):
        """
        :return:
        """
        return 'Mechanical Ventilation'

    def get_name(self, obj):
        """
        :param obj: EnergyPlus object.
        :return: name of the object.
        """
        return obj.Zone_Name

    def get_field_value(self, obj):
        """
        :param obj: EnergyPlus object
        :return: desired field value.
        """
        return float(obj.Outdoor_Air_Flow_Rate_per_Zone)

    def update(self, obj, value):
        """
        Update IDF object accordingly.
        :param obj: EnergyPlus object
        :param value: value to be set.
        """
        obj.Outdoor_Air_Method = 'Flow/Zone'
        obj.Outdoor_Air_Flow_Rate_per_Person = ''
        obj.Outdoor_Air_Flow_Rate_per_Zone_Floor_Area = ''
        obj.Outdoor_Air_Flow_Rate_per_Zone = "{:.2f}".format(round(value, 2))



class ProxyBuildingEnergyModel():
    """
    Class representing the proxy of a building energy model to be calibrated.

    Attributes:
        name: the name of the building energy model
        _parameters : list of parameters of the building energy model
    """
    __metaclass__ = ABCMeta

    def __init__(self, name):
        """
        :param name: name of the building energy model
        """
        self.name = name
        self._parameters = []
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.OCCUPANCY))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.LIGHTING))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.ELECTRIC_EQUIPMENT))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.INFILTRATION))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WINDOW_TO_WALL_RATIO))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WINDOW_THERMAL_RESISTANCE))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WINDOW_SHGC))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WALL_THERMAL_RESISTANCE))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WALL_DENSITY))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WALL_SPECIFIC_HEAT_CAPACITY))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WALL_THERMAL_EMISSIVITY))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.WALL_THERMAL_ABSORPTIVITY))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.HEATING_TEMPERATURE_SETPOINT))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.COOLING_TEMPERATURE_SETPOINT))
        self._parameters.extend(self.create_parameters(CategoryParameterBuildingEnergyModel.MECHANICAL_VENTILATION))

    def get_parameters(self, category):
        """
        :param category: category of parameter.
        :return: list of parameters corresponding to the category.
        """
        parameters = []
        for p in self._parameters:
            if p.get_category() == category:
                parameters.append(p)
        return parameters

    def get_parameter_values(self, names):
        """
        :param names: list of parameter names.
        :return: list of parameter values.
        """
        values = []
        for p in self._parameters:
            if p.name in names:
                values.append(p.get_value())
        return values

    def set_parameters(self, names, values):
        """
        Set parameters of the building energy model.
        :param names: list of parameter names.
        :param values: list of parameter values.
        """
        priority = [CategoryParameterBuildingEnergyModel.WINDOW_TO_WALL_RATIO]
        for n, name in enumerate(names):
            for param in self._parameters:
                if param.name == name and param.get_category() in priority:
                    param.set_value(values[n])
        for n, name in enumerate(names):
            for param in self._parameters:
                if param.name == name and not param.get_category() in priority:
                    param.set_value(values[n])
        self.save()


    @abstractmethod
    def create_parameters(self, category):
        """
        Create parameters of a certain category.

        :param category: category of parameter.
        :return: list of parameters corresponding to the category.
        """
        pass

    @abstractmethod
    def save(self):
        """
        Save the building energy model after setting parameters.
        """
        pass


class ProxyEnergyPlusModel(ProxyBuildingEnergyModel):
    """
    Class representing the proxy of an EnergyPlus model to be calibrated.

    Attribute:
        name: name of the building energy model.
        idf: pointer towards IDF objects.
        output_filename: name of the output file storing the updated EnergyPlus model.
    """

    def __init__(self, idf_filename, output_filename):
        IDF.setiddname(os.path.join(os.environ['ENERGYPLUS'], 'Energy+.idd'))
        self.idf = IDF(idf_filename)
        self.output_filename = output_filename
        ProxyBuildingEnergyModel.__init__(self, os.path.splitext(os.path.basename(idf_filename))[0])

    def create_parameters(self, category):
        """
        Create parameters of a certain category.

        :param category: category of parameter.
        :return: list of parameters corresponding to the category.
        """
        parameters = []
        is_changing_window_to_wall_ratio = False
        if category == CategoryParameterBuildingEnergyModel.OCCUPANCY:
            for obj in self.idf.idfobjects[ParameterEnergyPlusModelOccupancy().get_classname()]:
                parameters.append(ParameterEnergyPlusModelOccupancy(obj.Name + ':' + ParameterEnergyPlusModelOccupancy().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.LIGHTING:
            for obj in self.idf.idfobjects[ParameterEnergyPlusModelLighting().get_classname()]:
                parameters.append(ParameterEnergyPlusModelLighting(obj.Name + ':' + ParameterEnergyPlusModelLighting().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.ELECTRIC_EQUIPMENT:
            for obj in self.idf.idfobjects[ParameterEnergyPlusModelElectricEquipment().get_classname()]:
                parameters.append(ParameterEnergyPlusModelElectricEquipment(obj.Name + ':' + ParameterEnergyPlusModelElectricEquipment().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.INFILTRATION:
            for obj in self.idf.idfobjects[ParameterEnergyPlusModelInfiltration().get_classname()]:
                parameters.append(ParameterEnergyPlusModelInfiltration(obj.Name + ':' + ParameterEnergyPlusModelInfiltration().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.WINDOW_TO_WALL_RATIO:
            p = ParameterEnergyPlusModelWindowToWallRatio('Window to Wall Ratio', self.idf)
            p.set_value(0.5)
            parameters.append(p)
        elif category == CategoryParameterBuildingEnergyModel.WINDOW_THERMAL_RESISTANCE:
            parameters.append(ParameterEnergyPlusModelWindowThermalResistance('Imaginary Exterior Window Layer:'  + ParameterEnergyPlusModelWindowThermalResistance().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.WINDOW_SHGC:
            parameters.append(ParameterEnergyPlusModelWindowSolarHeatGainCoefficient('Imaginary Exterior Window Layer:' + ParameterEnergyPlusModelWindowSolarHeatGainCoefficient().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.WALL_THERMAL_RESISTANCE:
            parameters.append(ParameterEnergyPlusModelWallThermalResistance('Imaginary Exterior Wall Outer Layer:' + ParameterEnergyPlusModelWallThermalResistance().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.WALL_DENSITY:
            parameters.append(ParameterEnergyPlusModelWallDensity('Imaginary Exterior Wall Outer Layer:' + ParameterEnergyPlusModelWallDensity().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.WALL_SPECIFIC_HEAT_CAPACITY:
            parameters.append(ParameterEnergyPlusModelWallSpecificHeatCapacity('Imaginary Exterior Wall Outer Layer:' + ParameterEnergyPlusModelWallSpecificHeatCapacity().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.WALL_THERMAL_EMISSIVITY:
            parameters.append(ParameterEnergyPlusModelWallThermalEmissivity('Imaginary Exterior Wall Outer Layer:' + ParameterEnergyPlusModelWallThermalEmissivity().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.WALL_THERMAL_ABSORPTIVITY:
            parameters.append(ParameterEnergyPlusModelWallThermalAbsorptivity('Imaginary Exterior Wall Outer Layer:' + ParameterEnergyPlusModelWallThermalAbsorptivity().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.HEATING_TEMPERATURE_SETPOINT:
            for obj in self.idf.idfobjects[ParameterEnergyPlusModelHeatingTemperatureSetpoint().get_classname()]:
                parameters.append(ParameterEnergyPlusModelHeatingTemperatureSetpoint(obj.Name + ':' + ParameterEnergyPlusModelHeatingTemperatureSetpoint().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.COOLING_TEMPERATURE_SETPOINT:
            for obj in self.idf.idfobjects[ParameterEnergyPlusModelCoolingTemperatureSetpoint().get_classname()]:
                parameters.append(ParameterEnergyPlusModelCoolingTemperatureSetpoint(obj.Name + ':' + ParameterEnergyPlusModelCoolingTemperatureSetpoint().get_category_name(), self.idf))
        elif category == CategoryParameterBuildingEnergyModel.MECHANICAL_VENTILATION:
            for obj in self.idf.idfobjects[ParameterEnergyPlusModelMechanicalVentilation().get_classname()]:
                parameters.append(ParameterEnergyPlusModelMechanicalVentilation(obj.Zone_Name + ':' + ParameterEnergyPlusModelMechanicalVentilation().get_category_name(), self.idf))
        return parameters

    def save(self):
        """
        Save the building energy model after setting parameters.
        """
        self.idf.save(self.output_filename)

class UrbanBuildingEnergyModel():
    """
    Class representing an urban building energy model to be calibrated.

    Attributes:
        building_names: list of building names.
        bems_directory (str): directory where building energy models to be calibrated are stored.
        bem_proxies (dict): dictionary containing proxies of each building energy model to be calibrated.
    """
    __metaclass__ = ABCMeta

    def __init__(self, input_dir, output_dir = '.'):
        """
        :param building_names: list of building names.
        :param input_dir: directory in which building energy models are stored.
        :param output_dir: directory in which modified building energy models are stored.
        """
        self.bems_directory = output_dir
        self.bem_proxies = self.create_bem_proxies(input_dir, output_dir)

    def get_building_names(self):
        """
        :return: list of building names
        """
        return self.bem_proxies.keys()

    def get_parameters(self, building_name, category):
        """
        :param building_name: name of the building
        :param category: category of parameters
        :return: list of parameters of the building corresponding to the category
        """
        return self.bem_proxies[building_name].get_parameters(category)

    def set_parameters(self, building_name, param_names, values):
        """
        Set a list of
        """
        self.bem_proxies[building_name].set_parameters(param_names, values)

    @abstractmethod
    def create_bem_proxies(self, input_dir, output_dir):
        """
        Create the dictionary of proxies for each building energy model.
        :param input_dir: directory in which building energy models are stored.
        :param output_dir: directory in which modified building energy models are stored.
        """
        pass

    @abstractmethod
    def simulate(self, from_date, to_date, dt):
        """
        Simulate the urban building energy model.

        :param from_date: date from which simulations must be performed using the urban building energy model.
        :param to_date: date to which simulations must be performed using the urban building energy model.
        :param dt: time step between outputs.
        :return: outputs of simulation.
        """
        pass

class StandaloneEnergyPlusModels(UrbanBuildingEnergyModel):
    """
    Class representing an urban building energy model consisting of individual EnergyPlus models.

    Attributes:
        building_names: list of building names.
        bems_directory (str): directory where building energy models to be calibrated are stored.
        bem_proxies (dict): dictionary containing proxies of each building energy model to be calibrated.
        weather_file: file containing weather data to perform EnergyPlus simulations.
        num_processes_bems_pool: number of processes to run the pool of BEMS.
    """

    def __init__(self, input_dir, weather_file, output_dir = '.', num_processes_bems_pool = 2):
        """
        :param input_dir: directory in which building energy models are stored.
        :param weather_file: file containing weather data to perform EnergyPlus simulations.
        :param output_vars: list of output variables to be used for calibration.
        :param output_dir: directory in which modified building energy models are stored.
        """
        UrbanBuildingEnergyModel.__init__(self, input_dir, output_dir)
        self.weather_file = weather_file
        self.num_processes_bems_pool = num_processes_bems_pool

    def create_bem_proxies(self, input_dir, output_dir):
        """
        Create the dictionary of proxies for each building energy model.
        :param input_dir: directory in which building energy models are stored.
        :param output_dir: directory in which modified building energy models are stored.
        """
        proxies = {}
        for fn in os.listdir(input_dir):
            building_name = os.path.splitext(fn)[0]
            proxies[building_name] = ProxyEnergyPlusModel(idf_filename=input_dir + fn, output_filename=output_dir + fn)
        return proxies

    def simulate(self, from_date, to_date, dt):
        """
        Simulate the urban building energy model.

        :param from_date: date from which simulations must be performed using the urban building energy model.
        :param to_date: date to which simulations must be performed using the urban building energy model.
        :param dt: time step between outputs.
        :return: outputs of simulation.
        """
        bem_pool = EnergyPlusSimulationPool(EPWDataLoader(self.weather_file, year=from_date.year), nproc=self.num_processes_bems_pool)
        bem_pool.pool = []
        for building_name, proxy in self.bem_proxies.items():
            bem_pool.pool.append(EnergyPlusModel(IDFBuildingLoader(self.bems_directory + building_name + '.idf')))
        bem_pool.output_dir = os.path.join('simulation')
        bem_pool.run()
        output_data = {}
        for bem in bem_pool.pool:
            output_data[bem.building.name] = bem.building.get_sensible_cooling_load()[from_date:to_date].resample(dt).interpolate().values + \
                                                           bem.building.get_latent_cooling_load()[from_date:to_date].resample(dt).interpolate().values
        return output_data

class CoupledEnergyPlusModels(StandaloneEnergyPlusModels):
    """
    Class representing an urban building energy model consisting of EnergyPlus models coupled with a data driven urban canopy model.

    Attributes:
        building_names: list of building names.
        bems_directory (str): directory where building energy models to be calibrated are stored.
        bem_proxies (dict): dictionary containing proxies of each building energy model to be calibrated.
        weather_file: file containing weather data to perform EnergyPlus simulations.
        cfg_file: file containing configuration of the cosimulation engine.
        neighborhood_file: file containing information of the neighborhood to be considered for cosimulation.
        max_iter: maximum of iterations within which the coupled scheme should achieve convergence.
        ddm: type of data driven urban canopy model to be coupled with EnergyPlus models.
        training_split_ratio: ratio between the size of the training set and the total data set over the period of simulation.
        error_function: error function to determine whether the coupled scheme achieved convergence.
        num_processes_bems_pool: number of processes to run the pool of BEMS.
    """

    def __init__(self, input_dir, weather_file, cfg_file, neighborhood_file, output_dir = '.', max_iter = 100, ddm = 'dummy', training_split_ratio = 0.0, error_function = RootMeanSquareError(), num_processes_bems_pool = 2):
        """
        :param input_dir: directory in which building energy models are stored.
        :param weather_file: file containing weather data to perform EnergyPlus simulations.
        :param output_dir: directory in which modified building energy models are stored.
        :param cfg_file: file containing configuration of the cosimulation engine.
        :param neighborhood_file: file containing information of the neighborhood to be considered for cosimulation.
        :param max_iter: maximum of iterations within which the coupled scheme should achieve convergence.
        :param ddm: type of data driven urban canopy model to be coupled with EnergyPlus models.
        :param training_split_ratio: ratio between the size of the training set and the total data set over the period of simulation.
        :param n_processes: number of processes to speed up the training phase if it can be parallelized.
        """
        StandaloneEnergyPlusModels.__init__(self, input_dir, weather_file, output_dir, num_processes_bems_pool)
        self.cfg_file = cfg_file
        self.neighborhood_file = neighborhood_file
        self.max_iter = max_iter
        self.ddm = ddm
        self.training_split_ratio = training_split_ratio
        self.error_function = error_function

    def simulate(self, from_date, to_date, dt):
        """
        Simulate the urban building energy model.

        :param from_date: date from which simulations must be performed using the urban building energy model.
        :param to_date: date to which simulations must be performed using the urban building energy model.
        :param dt: time step between outputs.
        :return: outputs of simulation.
        """
        cosim = ExclusiveCosimulationEnergyPlusDataDriven(self.cfg_file, self.neighborhood_file, self.weather_file, max_iter=self.max_iter, ddm=self.ddm, training_split_ratio=self.training_split_ratio, error_function=self.error_function, num_processes_bems_pool=self.num_processes_bems_pool)
        cosim.cosimulate()
        output_data = {}
        for bem in cosim.bems:
            output_data[bem.building.name] = bem.building.get_sensible_cooling_load()[from_date:to_date].resample(dt).interpolate().values + \
                                             bem.building.get_latent_cooling_load()[from_date:to_date].resample(dt).interpolate().values
        return output_data

class ParametersSelector():
    """
    Class used to select parameters of an urban building energy model to be calibrated.

    Attributes:
        ubem: urban building energy model to be calibrated.
        metered_data: metered data used to calibrate the urban building energy model.
        categories: list of parameter categories to be calibrated.
        upper_bounds: list containing upper bounds for each parameter.
        lower_bounds: list containing lower bounds for each parameter.
        from_date: date from which estimates provided by the UBEM and measurements must be compared.
        to_date: date to which estimates provided by the UBEM and measurements must be compared.
        dt: timestep with which estimates provided by the UBEM and measurements must be compared.
        iter_saved: number of iterations to save samples for parameter selections.
    """
    __metaclass__ = ABCMeta

    def __init__(self, ubem = None, metered_data = None, categories = None, upper_bounds = None, lower_bounds = None,
                 from_date = None, to_date = None, dt = None, error_function = RootMeanSquareError(), iter_saved = 5,
                 generate_more_samples = True):
        """
        :param ubem: urban building energy model to be calibrated.
        :param metered_data: metered data used to calibrate the urban building energy model.
        :param categories: list of parameter categories to be calibrated.
        :param upper_bounds: list containing upper bounds for each parameter.
        :param lower_bounds: list containing lower bounds for each parameter.
        :param from_date: date from which estimates provided by the UBEM and measurements must be compared.
        :param to_date: date to which estimates provided by the UBEM and measurements must be compared.
        :param dt: timestep with which estimates provided by the UBEM and measurements must be compared.
        :param error_function: method used to evaluate the discrepancy between measurements and estimates.
        :param iter_saved: number of iterations to save samples for parameter selections.
        """
        self.ubem = ubem
        self.metered_data = metered_data
        self.categories = categories
        self.upper_bounds = upper_bounds
        self.lower_bounds = lower_bounds
        self.from_date = from_date
        self.to_date = to_date
        self.dt = dt
        self.error_function = error_function
        self.iter_saved = iter_saved
        self.generate_more_samples = generate_more_samples

    def select_parameters(self):
        """
        :return: selected parameters for each building of the urban building energy model.
        """
        calibration_data = {}
        path_to_save = os.path.join('calibration', 'sensitivity')
        selected_parameters = {}
        for building_name in self.ubem.get_building_names():
            calibration_data[building_name] = {}
            all_parameters = []
            parameters_upper_bounds = np.array([])
            parameters_lower_bounds = np.array([])
            for n, category in enumerate(self.categories):
                params = self.ubem.get_parameters(building_name, category)
                for p in params:
                    all_parameters.append(p.name)
                parameters_upper_bounds = np.concatenate((parameters_upper_bounds, self.upper_bounds[n] * np.ones(len(params))))
                parameters_lower_bounds = np.concatenate((parameters_lower_bounds, self.lower_bounds[n] * np.ones(len(params))))
            column_names = all_parameters + [self.error_function.get_name()]
            if os.path.exists(path_to_save + building_name + '.csv'):
                df = pd.read_csv(path_to_save + building_name + '.csv')
                input_samples = df[all_parameters].values
                number_samples = input_samples.shape[0]
                output_samples = df[self.error_function.get_name()].values
            else:
                input_samples = self.generate_input_samples(all_parameters, parameters_upper_bounds, parameters_lower_bounds)
                number_samples = input_samples.shape[0]
                output_samples = np.full(number_samples, np.nan)
                data = np.concatenate((input_samples, output_samples.reshape(-1, 1)), axis=1)
                df = pd.DataFrame(data, columns=column_names)
                df.to_csv(path_to_save + building_name + '.csv', index=False)
            n_start = 0
            for n in range(number_samples):
                if not np.isnan(output_samples[n]):
                    n_start = n_start + 1
                else:
                    break
            for n in range(n_start, number_samples):
                for building_name in self.ubem.get_building_names():
                    self.ubem.set_parameters(building_name, all_parameters, input_samples[n])
                outputs = self.ubem.simulate(self.from_date, self.to_date, self.dt)
                for building_name in self.ubem.get_building_names():
                    measurements = self.metered_data[building_name][self.from_date:self.to_date].resample(self.dt).interpolate().values
                    estimates = outputs[building_name]
                    output_samples[n] = self.error_function.err(estimates, measurements)
                    if (n == number_samples - 1) or ((n % self.iter_saved) == 0):
                        print('Samples being saved ... (Remaining: ' + str(number_samples - n) + ')')
                        data = np.concatenate((input_samples, output_samples.reshape(-1, 1)), axis=1)
                        df = pd.DataFrame(data, columns=column_names)
                        df.to_csv(path_to_save + building_name + '.csv', index=False)
            sensitivity_data = self.perform_sensitivity_analysis(building_name, all_parameters, parameters_upper_bounds, parameters_lower_bounds, input_samples, output_samples)
            selected_parameters[building_name] = self.make_parameters_selection(sensitivity_data, parameters_lower_bounds, parameters_upper_bounds)
        return selected_parameters


    @abstractmethod
    def generate_input_samples(self, building_name, parameters, upper_bounds, lower_bounds):
        """
        Generate input samples for the sensitivity analysis.
        :param building_name: name of the building for which the sensitivity analysis must be performed.
        :param parameters: list of parameters for the sensitivity analysis.
        :param upper_bounds: upper bounds for each parameter.
        :param lower_bounds: lower bounds for each parameter.
        :return: input samples for the sensitivity analysis.
        """
        pass

    @abstractmethod
    def perform_sensitivity_analysis(self, building_name, parameters, upper_bounds, lower_bounds, inputs, outputs):
        """
        Perform sensitivity analysis for selection of parameters
        :param building_name: name of the building for which the sensitivity analysis must be performed.
        :param parameters: list of parameters for the sensitivity analysis.
        :param upper_bounds: upper bounds for each parameter.
        :param lower_bounds: lower bounds for each parameter.
        :param inputs: input samples for the sensitivity analysis.
        :param outputs: output samples for the sensitivity analysis.
        :return: results of sensitivity analysis.
        """
        pass

    @abstractmethod
    def make_parameters_selection(self, results, lower_bounds, upper_bounds):
        """
        Make the selection of parameters.
        :param results: results of the sensitivity analysis.
        :param lower_bounds: lower bounds of all parameters.
        :param upper_bounds: upper bounds of all parameters.
        :return: list of selected parameters.
        """
        pass


class ParametersSelectorMorris(ParametersSelector):
    """
    Class used to select parameters of an urban building energy model to be calibrated using the Morris method.

    Attributes:
        ubem: urban building energy model to be calibrated.
        metered_data: metered data used to calibrate the urban building energy model.
        categories: list of parameter categories to be calibrated.
        upper_bounds: list containing upper bounds for each parameter.
        lower_bounds: list containing lower bounds for each parameter.
        from_date: date from which estimates provided by the UBEM and measurements must be compared.
        to_date: date to which estimates provided by the UBEM and measurements must be compared.
        dt: timestep with which estimates provided by the UBEM and measurements must be compared.
        error_function: method used to evaluate the discrepancy between measurements and estimates.
        iter_saved: number of iterations to save samples for parameter selections.
        num_trajectories: number of trajectories to generate with the Morris method.
        num_levels: number of grid levels to consider with the Morris method.
        optimal_trajectories: number of optimal trajectories to samples using the Morris method.
        num_best_parameters: number of best parameters to select from the Morris method.
        problem: specification of the problem to be studied using the Morris method.
    """

    def __init__(self, ubem = None, metered_data = None, categories = None, upper_bounds = None, lower_bounds = None,
                 from_date = None, to_date = None, dt = None, error_function = RootMeanSquareError(), iter_saved = 5,
                 generate_more_samples = True, num_trajectories=10,
                 num_levels=4, optimal_trajectories=2, num_best_parameters=1):
        """
        :param ubem: urban building energy model to be calibrated.
        :param metered_data: metered data used to calibrate the urban building energy model.
        :param categories: list of parameter categories to be calibrated.
        :param upper_bounds: list containing upper bounds for each parameter.
        :param lower_bounds: list containing lower bounds for each parameter.
        :param from_date: date from which estimates provided by the UBEM and measurements must be compared.
        :param to_date: date to which estimates provided by the UBEM and measurements must be compared.
        :param dt: timestep with which estimates provided by the UBEM and measurements must be compared.
        :param error_function: method used to evaluate the discrepancy between measurements and estimates.
        :param number_samples: number of samples to use for performing the parameter selection (i.e. sensitivity analysis).
        :param iter_saved: number of iterations to save samples for parameter selections.
        :param num_trajectories: number of trajectories to generate with the Morris method.
        :param num_levels: number of grid levels to consider with the Morris method.
        :param optimal_trajectories: number of optimal trajectories to samples using the Morris method.
        """
        ParametersSelector.__init__(self, ubem, metered_data, categories, upper_bounds, lower_bounds, from_date, to_date, dt, error_function, iter_saved, generate_more_samples)
        self.num_trajectories = num_trajectories
        self.num_levels = num_levels
        self.optimal_trajectories = optimal_trajectories
        self.num_best_parameters = num_best_parameters

    def generate_input_samples(self, parameters, upper_bounds, lower_bounds):
        """
        Generate input samples for the sensitivity analysis.
        :param parameters: list of parameters for the sensitivity analysis.
        :param upper_bounds: upper bounds for each parameter.
        :param lower_bounds: lower bounds for each parameter.
        :return: input samples for the sensitivity analysis.
        """
        problem = {
            'num_vars': len(parameters),
            'names': parameters,
            'groups': None,
            'bounds': np.concatenate((lower_bounds.reshape(-1, 1), upper_bounds.reshape(-1, 1)), axis=1)
        }
        return morris_sampler.sample(problem, N=self.num_trajectories, num_levels=self.num_levels, optimal_trajectories=self.optimal_trajectories)

    def perform_sensitivity_analysis(self, building_name, parameters, upper_bounds, lower_bounds, inputs, outputs):
        """
        Perform sensitivity analysis for selection of parameters.
        :param building_name: name of the building for which the sensitivity analysis must be performed.
        :param inputs: input samples for the sensitivity analysis.
        :param outputs: output samples for the sensitivity analysis.
        :return: results of sensitivity analysis.
        """
        problem = {
            'num_vars': len(parameters),
            'names': parameters,
            'groups': None,
            'bounds': np.concatenate((lower_bounds.reshape(-1, 1), upper_bounds.reshape(-1, 1)), axis=1)
        }
        N = int((inputs.shape[1] + 1) * (inputs.shape[0] // (inputs.shape[1] + 1)))
        sensitivity_analysis_data = {}
        results = morris.analyze(problem, inputs[:N], outputs[:N], conf_level=0.95, num_levels=4)
        sensitivity_analysis_data = {}
        sensitivity_analysis_data['parameters'] = results['names']
        sensitivity_analysis_data['mu_star'] = results['mu_star'].filled(fill_value=np.nan).tolist()
        sensitivity_analysis_data['sigma'] = results['sigma'].tolist()
        SENSITIVITY_DIR = os.path.join('calibration', 'sensitivity')
        with open(SENSITIVITY_DIR + building_name + '.json', 'w') as file:
            json.dump(sensitivity_analysis_data, file)
        return sensitivity_analysis_data

    def make_parameters_selection(self, results, lower_bounds, upper_bounds):
        """
        Make the selection of parameters.
        :param results: results of the sensitivity analysis.
        :param lower_bounds: lower bounds of all parameters.
        :param upper_bounds: upper bounds of all parameters.
        :return: list of selected parameters.
        """
        sorted_indexes = [i for i, _ in sorted(enumerate(results['mu_star']), key=lambda x: x[1], reverse=True)]
        selected_parameters = {}
        selected_parameters['names'] = []
        selected_parameters['lower_bounds'] = []
        selected_parameters['upper_bounds'] = []
        for i in sorted_indexes[0:self.num_best_parameters]:
            selected_parameters['names'].append(results['parameters'][i])
            selected_parameters['lower_bounds'].append(lower_bounds[i])
            selected_parameters['upper_bounds'].append(upper_bounds[i])
        return selected_parameters

class Calibration():
    """
    Class representing an algorithm to calibrate an urban building energy model.

    Attributes:
        ubem: urban building energy model to calibrate
        metered_data: metered data used to calibrate the urban building energy model
        categories: categories of parameters that must be calibrated.
        upper_bounds: upper bounds for each category of parameters.
        lower_bounds: lower bounds for each category of parameters.
        from_date: date from which estimates and measurements must be compared.
        to_date: date to which estimates and measurements must be compared.
        dt: timestep with which estimates and measurements must be compared.
        error_function: method to calculate the discrepancy between measurements and estimates.
    """
    __metaclass__ = ABCMeta

    def __init__(self, ubem, metered_data, categories, upper_bounds, lower_bounds, from_date, to_date, dt, parameters_selector = ParametersSelectorMorris(), error_function = RootMeanSquareError()):
        """
        :param ubem: urban building energy model to calibrate
        :param metered_data: metered data used to calibrate the urban building energy model
        :param categories: categories of parameters that must be calibrated.
        :param upper_bounds: upper bounds for each category of parameters.
        :param lower_bounds: lower bounds for each category of parameters.
        :param from_date: date from which estimates and measurements must be compared.
        :param to_date: date to which estimates and measurements must be compared.
        :param dt: timestep with which estimates and measurements must be compared.
        :param error_function: method to calculate the discrepancy between measurements and estimates.
        """
        self.ubem = ubem
        self.metered_data = metered_data
        self.categories = categories
        self.upper_bounds = upper_bounds
        self.lower_bounds = lower_bounds
        self.from_date = from_date
        self.to_date = to_date
        self.dt = dt
        self.parameters_selector = parameters_selector
        self.parameters_selector.ubem = ubem
        self.parameters_selector.metered_data = metered_data
        self.parameters_selector.categories = categories
        self.parameters_selector.upper_bounds = upper_bounds
        self.parameters_selector.lower_bounds = lower_bounds
        self.parameters_selector.from_date = from_date
        self.parameters_selector.to_date = to_date
        self.parameters_selector.dt = dt
        self.parameters_selector.error_function = error_function
        self.error_function = error_function

    def calibrate(self):
        os.makedirs(os.path.join('calibration'), exist_ok=True)
        os.makedirs(os.path.join('calibration', 'sensitivity'), exist_ok=True)
        selected_parameters = self.parameters_selector.select_parameters()
        calibrated_params = self.get_calibrated_parameters(selected_parameters)
        for building_name, proxy in self.ubem.bem_proxies.items():
            proxy.output_filename = os.path.join("calibration", building_name + '.idf')
            proxy.set_parameters(calibrated_params[building_name]['names'], calibrated_params[building_name]['values'])

    @abstractmethod
    def get_calibrated_parameters(self, selected_parameters):
        """
        :param selected_parameters: parameters selected from sensitivity analysis
        :return (dict): calibrated parameters for each building of the urban building energy model.
        """
        pass

class SurrogateBuildingEnergyModel():
    """
    Class used to emulate the behaviour of a building energy model during the calibration of an urban building energy model.

    Attributes:
        building_name: name of the building the surrogate model is supposed to emulate.
    """
    __metaclass__ = ABCMeta

    def __init__(self, building_name):
        """
        :param building_name: building_name: name of the building the surrogate model is supposed to emulate.
        """
        self.building_name = building_name


    @abstractmethod
    def train(self, inputs, outputs):
        """
        Train a surrogate model.
        :param inputs: inputs used to train the surrogate model.
        :param outputs: outputs used to train the surrogate model.
        """
        pass

    @abstractmethod
    def predict(self, inputs):
        """
        Make predictions using the surrogate model.
        :param inputs: inputs used to make predictions.
        :return: predictions
        """
        pass

class LinearRegressionModel(SurrogateBuildingEnergyModel):
    """
    Class used to emulate the behaviour of a building energy model as a linear regression.

    Attribute:
        building_name: name of the building the surrogate model is supposed to emulate.
        linear_regression_model: internal state of the linear regression model used to emulate a building energy model.
    """

    def __init__(self, building_name):
        SurrogateBuildingEnergyModel.__init__(self, building_name)
        self.linear_regression_model = None

    def train(self, inputs, outputs):
        """
        Train a surrogate model.
        :param inputs: inputs used to train the surrogate model.
        :param outputs: outputs used to train the surrogate model.
        """
        self.linear_regression_model = LinearRegression().fit(inputs, outputs)


    def predict(self, inputs):
        """
        Make predictions using the surrogate model.
        :param inputs: inputs used to make predictions.
        :return: predictions
        """
        return self.linear_regression_model.predict(inputs)

class SupportVectorMachineModel(SurrogateBuildingEnergyModel):
    """
    Class used to emulate the behaviour of a building energy model as a support vector machine.

    Attribute:
        building_name: name of the building the surrogate model is supposed to emulate.
        support_vector_machine_model: internal state of the support vector machine model used to emulate a building energy model.
    """

    def __init__(self, building_name):
        SurrogateBuildingEnergyModel.__init__(self, building_name)
        self.support_vector_machine_model = None

    def train(self, inputs, outputs):
        """
        Train a surrogate model.
        :param inputs: inputs used to train the surrogate model.
        :param outputs: outputs used to train the surrogate model.
        """
        self.support_vector_machine_model = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2)).fit(inputs, outputs)


    def predict(self, inputs):
        """
        Make predictions using the surrogate model.
        :param inputs: inputs used to make predictions.
        :return: predictions
        """
        return self.support_vector_machine_model.predict(inputs)

class GradientBoostingModel(SurrogateBuildingEnergyModel):
    """
    Class used to emulate the behaviour of a building energy model as a gradient boosting.

    Attribute:
        building_name: name of the building the surrogate model is supposed to emulate.
        gradient_boosting_model: internal state of the gradient boosting model used to emulate a building energy model.
    """

    def __init__(self, building_name):
        SurrogateBuildingEnergyModel.__init__(self, building_name)
        self.gradient_boosting_model = None

    def train(self, inputs, outputs):
        """
        Train a surrogate model.
        :param inputs: inputs used to train the surrogate model.
        :param outputs: outputs used to train the surrogate model.
        """
        self.gradient_boosting_model = GradientBoostingRegressor().fit(inputs, outputs)


    def predict(self, inputs):
        """
        Make predictions using the surrogate model.
        :param inputs: inputs used to make predictions.
        :return: predictions
        """
        return self.gradient_boosting_model.predict(inputs)

class ArtificialNeuralNetworkModel(SurrogateBuildingEnergyModel):
    """
    Class used to emulate the behaviour of a building energy model as an artificial neural network.

    Attribute:
        building_name: name of the building the surrogate model is supposed to emulate.
        artificial_neural_network_model: internal state of the artificial neural network model used to emulate a building energy model.
        hidden_layer_sizes: the ith element represents the number of neurons in the ith hidden layer.
    """

    def __init__(self, building_name, hidden_layer_sizes = (100,)):
        SurrogateBuildingEnergyModel.__init__(self, building_name)
        self.artificial_neural_network_model = None
        self.hidden_layer_sizes = hidden_layer_sizes

    def train(self, inputs, outputs):
        """
        Train a surrogate model.
        :param inputs: inputs used to train the surrogate model.
        :param outputs: outputs used to train the surrogate model.
        """
        self.artificial_neural_network_model = MLPRegressor(hidden_layer_sizes=self.hidden_layer_sizes, activation='identity').fit(inputs, outputs)


    def predict(self, inputs):
        """
        Make predictions using the surrogate model.
        :param inputs: inputs used to make predictions.
        :return: predictions
        """
        return self.artificial_neural_network_model.predict(inputs)

class RandomForestModel(SurrogateBuildingEnergyModel):
    """
    Class used to emulate the behaviour of a building energy model as a random forest.

    Attribute:
        building_name: name of the building the surrogate model is supposed to emulate.
        random_forest_model: internal state of the random forest model used to emulate a building energy model.
        n_estimators: the number of trees in the forest.
    """

    def __init__(self, building_name, n_estimators = 100):
        SurrogateBuildingEnergyModel.__init__(self, building_name)
        self.random_forest_model = None
        self.n_estimators = n_estimators

    def train(self, inputs, outputs):
        """
        Train a surrogate model.
        :param inputs: inputs used to train the surrogate model.
        :param outputs: outputs used to train the surrogate model.
        """
        self.random_forest_model = RandomForestRegressor(n_estimators=self.n_estimators).fit(inputs, outputs)

    def predict(self, inputs):
        """
        Make predictions using the surrogate model.
        :param inputs: inputs used to make predictions.
        :return: predictions
        """
        return self.random_forest_model.predict(inputs)

class GaussianProcessModel(SurrogateBuildingEnergyModel):
    """
    Class used to emulate the behaviour of a building energy model as a gaussian process.

    Attribute:
        building_name: name of the building the surrogate model is supposed to emulate.
        gaussian_process_model: internal state of the gaussian process model used to emulate a building energy model.
    """

    def __init__(self, building_name):
        SurrogateBuildingEnergyModel.__init__(self, building_name)
        self.gaussian_process_model = None

    def train(self, inputs, outputs):
        """
        Train a surrogate model.
        :param inputs: inputs used to train the surrogate model.
        :param outputs: outputs used to train the surrogate model.
        """
        self.gaussian_process_model = gpflow.models.GPR(data=(inputs, outputs.reshape(-1, 1)), kernel=gpflow.kernels.SquaredExponential())
        optimizer = gpflow.optimizers.Scipy()
        optimizer.minimize(self.gaussian_process_model.training_loss, self.gaussian_process_model.trainable_variables)


    def predict(self, inputs):
        """
        Make predictions using the surrogate model.
        :param inputs: inputs used to make predictions.
        :return: predictions
        """
        m, v = self.gaussian_process_model.predict_y(inputs)
        return m.numpy()


class SurrogateBuildingEnergyModelLoader():
    """
    Class used to load the surrogate of a building energy model.

    Attributes:
        building_name: name of the building the surrogate is supposed to emulate.
        inputs: inputs used to train the surrogate model in case it has not been previously saved.
        outputs: outputs used to train the surrogate model in case it has not been previously saved.
    """
    __metaclass__ = ABCMeta

    def __init__(self, building_name = None,  training_inputs = None, training_outputs = None,
                 test_inputs = None, test_outputs = None):
        """
        :param building_name: name of the building the surrogate is supposed to emulate.
        :param training_inputs: inputs used to train the surrogate model.
        :param training_outputs: outputs used to train the surrogate model.
        :param test_inputs: inputs used to test the surrogate model.
        :param test_outputs: outputs used to test the surrogate model.
        """
        self.building_name = building_name
        self.training_inputs = training_inputs
        self.training_outputs = training_outputs
        self.test_inputs = test_inputs
        self.test_outputs = test_outputs

    def load(self):
        """
        Load the surrogate of a building energy model.
        :return: the surrogate model.
        """
        SURROGATE_MODELS_DIR = os.path.join('calibration', self.get_name())
        surrogate_model = None
        if os.path.exists(SURROGATE_MODELS_DIR) or not os.listdir(SURROGATE_MODELS_DIR):
            np.savetxt(SURROGATE_MODELS_DIR + self.building_name + '_training_inputs.txt', self.training_inputs, delimiter=",")
            np.savetxt(SURROGATE_MODELS_DIR + self.building_name + '_training_outputs.txt', self.training_outputs, delimiter=",")
            np.savetxt(SURROGATE_MODELS_DIR + self.building_name + '_test_inputs.txt', self.test_inputs, delimiter=",")
            np.savetxt(SURROGATE_MODELS_DIR + self.building_name + '_test_outputs.txt', self.test_outputs, delimiter=",")
        else:
            self.training_inputs = np.genfromtxt(SURROGATE_MODELS_DIR + self.building_name + '_training_inputs.txt', delimiter=",")
            self.training_outputs = np.genfromtxt(SURROGATE_MODELS_DIR + self.building_name + '_training_outputs.txt', delimiter=",")
            self.test_inputs = np.genfromtxt(SURROGATE_MODELS_DIR + self.building_name + '_test_inputs.txt', delimiter=",")
            self.test_outputs = np.genfromtxt(SURROGATE_MODELS_DIR + self.building_name + '_test_outputs.txt', delimiter=",")
        surrogate_model = self.get_instance()
        surrogate_model.train(self.training_inputs, self.training_outputs)
        return surrogate_model

    @abstractmethod
    def get_name(self):
        """
        :return: the name of the surrogate model.
        """
        pass

    @abstractmethod
    def get_instance(self):
        """
        Get instance of the surrogate model.
        """
        pass

class LinearRegressionModelLoader(SurrogateBuildingEnergyModelLoader):
    """
    Class used to load the linear regression model of a building.

    Attributes:
        building_name: name of the building the surrogate is supposed to emulate.
        training_samples: samples used to train the surrogate model if needed.
    """

    def __init__(self, building_name = None, inputs = None, outputs = None):
        """
        :param building_name: name of the building the surrogate is supposed to emulate.
        :param training_samples: samples used to train the surrogate model if needed.
        """
        SurrogateBuildingEnergyModelLoader.__init__(self, building_name, inputs, outputs)

    def get_name(self):
        """
        :return: the name of the surrogate model.
        """
        return 'linear_regression'

    def get_instance(self):
        """
        Get instance of the surrogate model.
        """
        return LinearRegressionModel(self.building_name)

class SupportVectorMachineModelLoader(SurrogateBuildingEnergyModelLoader):
    """
    Class used to load the support vector machine model of a building.

    Attributes:
        building_name: name of the building the surrogate is supposed to emulate.
        training_samples: samples used to train the surrogate model if needed.
    """

    def __init__(self, building_name = None, inputs = None, outputs = None):
        """
        :param building_name: name of the building the surrogate is supposed to emulate.
        :param training_samples: samples used to train the surrogate model if needed.
        """
        SurrogateBuildingEnergyModelLoader.__init__(self, building_name, inputs, outputs)

    def get_name(self):
        """
        :return: the name of the surrogate model.
        """
        return 'support_vector_machine'

    def get_instance(self):
        """
        Get instance of the surrogate model.
        """
        return SupportVectorMachineModel(self.building_name)

class GradientBoostingModelLoader(SurrogateBuildingEnergyModelLoader):
    """
    Class used to load the support vector machine model of a building.

    Attributes:
        building_name: name of the building the surrogate is supposed to emulate.
        training_samples: samples used to train the surrogate model if needed.
    """

    def __init__(self, building_name = None, inputs = None, outputs = None):
        """
        :param building_name: name of the building the surrogate is supposed to emulate.
        :param training_samples: samples used to train the surrogate model if needed.
        """
        SurrogateBuildingEnergyModelLoader.__init__(self, building_name, inputs, outputs)

    def get_name(self):
        """
        :return: the name of the surrogate model.
        """
        return 'gradient_boosting'

    def get_instance(self):
        """
        Get instance of the surrogate model.
        """
        return GradientBoostingModel(self.building_name)

class ArtificialNeuralNetworkModelLoader(SurrogateBuildingEnergyModelLoader):
    """
    Class used to load the artificial neural network model of a building.

    Attributes:
        building_name: name of the building the surrogate is supposed to emulate.
        training_samples: samples used to train the surrogate model if needed.
        hidden_layer_sizes: the ith element represents the number of neurons in the ith hidden layer.
    """

    def __init__(self, building_name = None, inputs = None, outputs = None, hidden_layer_sizes = (100,)):
        """
        :param building_name: name of the building the surrogate is supposed to emulate.
        :param training_samples: samples used to train the surrogate model if needed.
        :param hidden_layer_sizes: the ith element represents the number of neurons in the ith hidden layer.
        """
        SurrogateBuildingEnergyModelLoader.__init__(self, building_name, inputs, outputs)
        self.hidden_layer_sizes = hidden_layer_sizes

    def get_name(self):
        """
        :return: the name of the surrogate model.
        """
        return 'artificial_neural_network'

    def get_instance(self):
        """
        Get instance of the surrogate model.
        """
        return ArtificialNeuralNetworkModel(self.building_name, hidden_layer_sizes = self.hidden_layer_sizes)

class RandomForestLoader(SurrogateBuildingEnergyModelLoader):
    """
    Class used to load the random forest model of a building.

    Attributes:
        building_name: name of the building the surrogate is supposed to emulate.
        training_samples: samples used to train the surrogate model if needed.
        n_estimators: the number of trees in the forest.
    """

    def __init__(self, building_name = None, inputs = None, outputs = None, n_estimators = 100):
        """
        :param building_name: name of the building the surrogate is supposed to emulate.
        :param training_samples: samples used to train the surrogate model if needed.
        :param n_estimators: the number of trees in the forest.
        """
        SurrogateBuildingEnergyModelLoader.__init__(self, building_name, inputs, outputs)
        self.n_estimators = n_estimators

    def get_name(self):
        """
        :return: the name of the surrogate model.
        """
        return 'random_forest'

    def get_instance(self):
        """
        Get instance of the surrogate model.
        """
        return RandomForestModel(self.building_name, n_estimators = self.n_estimators)

class GaussianProcessModelLoader(SurrogateBuildingEnergyModelLoader):
    """
    Class used to load the gaussian process model of a building.

    Attributes:
        building_name: name of the building the surrogate is supposed to emulate.
        training_samples: samples used to train the surrogate model if needed.
    """

    def __init__(self, building_name = None, inputs = None, outputs = None):
        """
        :param building_name: name of the building the surrogate is supposed to emulate.
        :param training_samples: samples used to train the surrogate model if needed.
        """
        SurrogateBuildingEnergyModelLoader.__init__(self, building_name, inputs, outputs)

    def get_name(self):
        """
        :return: the name of the surrogate model.
        """
        return 'gaussian_process'

    def get_instance(self):
        """
        Get instance of the surrogate model.
        """
        return GaussianProcessModel(self.building_name)

class CalibrationByOptimization(Calibration):
    """
    Class representing for calibration of an urban building energy model using an optimization technique.

    Attributes:
        ubem: urban building energy model to calibrate
        metered_data: metered data used to calibrate the urban building energy model
        categories: categories of parameters that must be calibrated.
        upper_bounds: upper bounds for each category of parameters.
        lower_bounds: lower bounds for each category of parameters.
        from_date: date from which estimates and measurements must be compared.
        to_date: date to which estimates and measurements must be compared.
        dt: timestep with which estimates and measurements must be compared.
        error_function: method to calculate the discrepancy between measurements and estimates.
        parameters_selector: method used to select parameters.
        surrogate_training_ratio: number of samples to train/test a surrogate model of buildings.
        surrogate_model_loader: method to load surrogate models of building energy models.
    """

    def __init__(self, ubem, metered_data, categories, upper_bounds, lower_bounds, from_date, to_date, dt,
                 parameters_selector = ParametersSelectorMorris(), error_function = RootMeanSquareError(),
                 surrogate_model_loader = GaussianProcessModelLoader(), surrogate_number_samples = 100,
                 surrogate_training_ratio = 0.1, iter_saved = 10):
        """
        :param ubem: urban building energy model to calibrate
        :param metered_data: metered data used to calibrate the urban building energy model
        :param categories: categories of parameters that must be calibrated.
        :param upper_bounds: upper bounds for each category of parameters.
        :param lower_bounds: lower bounds for each category of parameters.
        :param from_date: date from which estimates and measurements must be compared.
        :param to_date: date to which estimates and measurements must be compared.
        :param dt: timestep with which estimates and measurements must be compared.
        :param parameters_selector: method used to select the most sensitive parameters of each building in an urban building energy model.
        :param surrogate_number_samples: number of samples to generate to train the surrogate model.
        :param surrogate_training_ratio: number of samples to train/test a surrogate model of buildings.
        :param surrogate_model_loader: method to load surrogate models of building energy models.
        """
        Calibration.__init__(self, ubem, metered_data, categories, upper_bounds, lower_bounds, from_date, to_date, dt, parameters_selector, error_function)
        self.surrogate_model_loader = surrogate_model_loader
        self.surrogate_number_samples = surrogate_number_samples
        self.surrogate_training_ratio = surrogate_training_ratio
        self.iter_saved = iter_saved

    def get_calibrated_parameters(self, selected_parameters):
        """
        :param selected_parameters: parameters selected from sensitivity analysis
        :return: calibrated parameters for each building of the urban building energy model.
        """
        SAMPLES_DIR = os.path.join('calibration', 'samples')
        SURROGATE_DIR = os.path.join('calibration', self.surrogate_model_loader.get_name())
        os.makedirs(SAMPLES_DIR, exist_ok=True)
        os.makedirs(SURROGATE_DIR, exist_ok=True)
        calibrated_parameters = {}
        for building_name in self.ubem.get_building_names():
            input_names = selected_parameters[building_name]['names']
            lower_bounds = np.array(selected_parameters[building_name]['lower_bounds'])
            upper_bounds = np.array(selected_parameters[building_name]['upper_bounds'])
            column_names = input_names + [self.error_function.get_name()]
            if os.path.exists(SAMPLES_DIR + building_name + '.csv'):
                df = pd.read_csv(SAMPLES_DIR + building_name + '.csv')
                input_samples = df[input_names].values
                output_samples = df[self.error_function.get_name()].values
            else:
                input_samples = np.random.uniform(lower_bounds, upper_bounds, size = (self.surrogate_number_samples, len(input_names)))
                output_samples = np.full(self.surrogate_number_samples, np.nan)
                data = np.concatenate((input_samples, output_samples.reshape(-1, 1)), axis=1)
                df = pd.DataFrame(data, columns=column_names)
                df.to_csv(SAMPLES_DIR + building_name + '.csv', index=False)
            n_start = 0
            for n in range(self.surrogate_number_samples):
                if not np.isnan(output_samples[n]):
                    n_start = n_start + 1
            for n in range(n_start, self.surrogate_number_samples):
                for building_name in self.ubem.get_building_names():
                    self.ubem.set_parameters(building_name, input_names, input_samples[n])
                outputs = self.ubem.simulate(self.from_date, self.to_date, self.dt)
                for building_name in self.ubem.get_building_names():
                    measurements = self.metered_data[building_name][self.from_date:self.to_date].resample(self.dt).interpolate().values
                    estimates = outputs[building_name]
                    output_samples[n] = self.error_function.err(estimates, measurements)
                    if (n == self.surrogate_number_samples - 1) or ((n % self.iter_saved) == 0):
                        print('Samples being saved ... (Remaining: ' + str(self.surrogate_number_samples - n) + ')')
                        data = np.concatenate((input_samples, output_samples.reshape(-1, 1)), axis=1)
                        df = pd.DataFrame(data, columns=column_names)
                        df.to_csv(SAMPLES_DIR + building_name + '.csv', index=False)
            random_indices = np.random.choice(input_samples.shape[0], int(np.round(self.surrogate_training_ratio * len(input_samples))), replace=False)
            self.surrogate_model_loader.building_name = building_name
            self.surrogate_model_loader.training_inputs = input_samples[random_indices]
            self.surrogate_model_loader.training_outputs = output_samples[random_indices]
            self.surrogate_model_loader.test_inputs = np.delete(input_samples, random_indices, axis=0)
            self.surrogate_model_loader.test_outputs = np.delete(output_samples, random_indices, axis=0)
            surrogate_model = self.surrogate_model_loader.load()
            def fitness_func(ga_instance, solution, solution_idx):
                result = surrogate_model.predict(solution.reshape(1, -1))
                if np.isscalar(result):
                    return result
                elif result.ndim == 1:
                    return result[0]
                else:
                    return result[0][0]
            fitness_function = fitness_func
            num_generations = 50
            num_parents_mating = 4
            sol_per_pop = 8
            num_genes = len(input_names)
            init_range_low = -2
            init_range_high = 5
            parent_selection_type = "sss"
            keep_parents = 1
            crossover_type = "single_point"
            mutation_type = "random"
            mutation_percent_genes = 10
            ga_instance = pygad.GA(num_generations=num_generations,
                                   num_parents_mating=num_parents_mating,
                                   fitness_func=fitness_function,
                                   sol_per_pop=sol_per_pop,
                                   num_genes=num_genes,
                                   init_range_low=init_range_low,
                                   init_range_high=init_range_high,
                                   parent_selection_type=parent_selection_type,
                                   keep_parents=keep_parents,
                                   crossover_type=crossover_type,
                                   mutation_type=mutation_type,
                                   mutation_percent_genes=mutation_percent_genes,
                                   gene_space=np.concatenate((lower_bounds.reshape(-1, 1), upper_bounds.reshape(-1, 1)), axis=1))
            ga_instance.run()
            calibrated_parameters[building_name] = {}
            calibrated_parameters[building_name]['names'] = []
            calibrated_parameters[building_name]['values'] = []
            for n, pname in enumerate(selected_parameters[building_name]['names']):
                calibrated_parameters[building_name]['names'].append(pname)
                calibrated_parameters[building_name]['values'].append(ga_instance.best_solution()[0][n])
        return calibrated_parameters

