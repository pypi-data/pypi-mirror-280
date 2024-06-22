"""
Module to create and update building energy models, and perform building energy simulation in sequence or parallel.

Delft University of Technology
Dr. Miguel Martin
"""
import multiprocessing
from abc import ABCMeta, abstractmethod
import os
import shutil
from subprocess import Popen
import glob
import platform
import traceback
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.termination import get_termination
from pymoo.optimize import minimize
import scipy.signal as sig

import numpy as np
import opyplus as op
import shutil
import subprocess
from datetime import datetime, date, timedelta
import string
import pandas as pd
from metpy.units import units
from metpy.calc import *
from sklearn.metrics import mean_squared_error
from pvlib.location import Location

from scipy.constants import Stefan_Boltzmann as sigma

from sciencespy.dom import *

class ErrorFunction():
    """
    Class with which the error between two numerical vectors can be calculated.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self):
        """
        :return: name of the error function.
        """
        pass

    @abstractmethod
    def err(self, vec1, vec2):
        """
        :param vec1: first numerical vector.
        :param vec2: second numerical vector.
        :return: error between two numerical vectors.
        """
        pass

class RootMeanSquareError(ErrorFunction):

    def get_name(self):
        """
        :return: name of the error function.
        """
        return 'RMSE'

    def err(self, vec1, vec2):
        """
        :param vec1: first numerical vector.
        :param vec2: second numerical vector.
        :return: error between two numerical vectors.
        """
        return np.sqrt(mean_squared_error(vec1, vec2))

class MeanBiasError(ErrorFunction):

    def get_name(self):
        """
        :return: name of the error function.
        """
        return 'MBE'

    def err(self, vec1, vec2):
        """
        :param vec1: first numerical vector.
        :param vec2: second numerical vector.
        :return: error between two numerical vectors.
        """
        return np.sum(vec1 - vec2) / len(vec1)

class CoefficientOfVariationOfRootMeanSquareError(RootMeanSquareError):

    def get_name(self):
        """
        :return: name of the error function.
        """
        return 'CV' + RootMeanSquareError.get_name(self)

    def err(self, vec1, vec2):
        """
        :param vec1: first numerical vector.
        :param vec2: second numerical vector.
        :return: error between two numerical vectors.
        """
        RMSE = RootMeanSquareError.err(self, vec1, vec2)
        return 100 * (RMSE / np.mean(vec2))

class NormalizeMeanBiasError(ErrorFunction):

    def get_name(self):
        """
        :return: name of the error function.
        """
        return "NMBE"

    def err(self, vec1, vec2):
        """
        :param vec1: first numerical vector.
        :param vec2: second numerical vector.
        :return: error between two numerical vectors.
        """
        return 100 * (np.mean(vec1) - np.mean(vec2)) / np.mean(vec2)

class WeatherData():
    """
    Class containing weather data.

    Attributes:
        year: year during which weather data were collected

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.year = date.today().year
        self.latitude = 0.0
        self.longitude = 0.0
        self.timezone = 0
        self.timestamps = None
        self.outdoor_air_temperature = None
        self.outdoor_air_relative_humidity = None
        self.outdoor_air_pressure = None
        self.outdoor_air_specific_humidity = None
        self.direct_normal_irradiance = None
        self.diffuse_horizontal_irradiance = None
        self.horizontal_infrared_radiation_intensity = None
        self.zenith_angle_sun = None
        self.azimuth_angle_sun = None
        self.outdoor_mean_radiant_temperature = None

    @abstractmethod
    def set_year(self, new_year):
        """
        :param new_year: year weather data were collected
        """
        pass
    @abstractmethod
    def set_latitude(self, new_latitude):
        """
        :param new_latitude: latitude weather data were collected
        """
        pass
    @abstractmethod
    def set_longitude(self, new_longitude):
        """
        :param new_longitude: longitude weather data were collected
        """
        pass

    @abstractmethod
    def set_timezone(self, new_timezone):
        """
        :param new_timezone: timezone weather data were collected
        """
        pass

    @abstractmethod
    def set_outdoor_air_temperature(self, new_outdoor_air_temperature):
        """
        :param new_outdoor_air_temperature: new values for the outdoor air temperature (in ^oC)
        """
        pass

    @abstractmethod
    def set_outdoor_air_relative_humidity(self, new_outdoor_air_relative_humidity):
        """
        :param new_outdoor_air_relative_humidity: new values for the outdoor air relative humidity (in %)
        """
        pass
    @abstractmethod
    def save(self, file_name, out_dir='.'):
        """
        Save weather data.
        :param file_name: file name where weather data must be saved
        :param out_dir: output directory where weather data must be saved
        """
        pass

class WeatherDataLoader():
    """
    Class to load weather data.

    Attributes:
        weather_file: file containing weather data.
    """
    __metaclass__ = ABCMeta

    def __init__(self, weather_file):
        """
        :param weather_file: file containg weather data.
        """
        self.weather_file = weather_file

    def load(self):
        weather_data = self.get_instance()
        weather_data.year = self.get_year()
        weather_data.latitude = self.get_latitude()
        weather_data.longitude = self.get_longitude()
        weather_data.timezone = self.get_timezone()
        weather_data.timestamps = self.get_timestamps()
        weather_data.outdoor_air_temperature = self.get_outdoor_air_temperature()
        weather_data.outdoor_air_relative_humidity = self.get_outdoor_air_relative_humidity()
        weather_data.outdoor_air_pressure = self.get_outdoor_air_pressure()
        weather_data.outdoor_air_specific_humidity = self.get_outdoor_air_specific_humidity()
        weather_data.direct_normal_irradiance = self.get_direct_normal_irradiance()
        weather_data.diffuse_horizontal_irradiance = self.get_diffuse_horizontal_irradiance()
        weather_data.horizontal_infrared_radiation_intensity = self.get_horizontal_infrared_radiation_intensity()
        weather_data.zenith_angle_sun = self.get_zenith_angle_sun()
        weather_data.azimuth_angle_sun = self.get_azimuth_angle_sun()
        weather_data.outdoor_mean_radiant_temperature = self.get_outdoor_mean_radiant_temperature()
        return weather_data

    @abstractmethod
    def get_instance(self):
        """
        :return: instance of weather data
        """
        pass


    @abstractmethod
    def get_year(self):
        """
        :return: year weather data were collected
        """
        pass

    @abstractmethod
    def get_latitude(self):
        """
        :return: latitude weather data were collected
        """
        pass

    @abstractmethod
    def get_longitude(self):
        """
        :return: longitude weather data were collected
        """
        pass

    @abstractmethod
    def get_timezone(self):
        """
        :return: longitude weather data were collected
        """
        pass

    @abstractmethod
    def get_timestamps(self):
        """
        :return: timestamps at which weather data were collected
        """
        pass

    @abstractmethod
    def get_outdoor_air_temperature(self):
        """
        :return: the outdoor air temperature (in ^oC)
        """
        pass

    @abstractmethod
    def get_outdoor_air_relative_humidity(self):
        """
        :return: the outdoor air relative humidity (in %)
        """
        pass

    @abstractmethod
    def get_outdoor_air_pressure(self):
        """
        :return: the outdoor air temperature (in Pa)
        """
        pass

    @abstractmethod
    def get_direct_normal_irradiance(self):
        """
        :return: the direct normal irradiance (in W/m^2)
        """
        pass

    @abstractmethod
    def get_diffuse_horizontal_irradiance(self):
        """
        :return: the diffuse horizontal irradiance (in W/m^2)
        """
        pass

    @abstractmethod
    def get_horizontal_infrared_radiation_intensity(self):
        """
        :return: the horizontal infrared radiation intensity (in W/m^2)
        """
        pass

    def get_outdoor_air_specific_humidity(self):
        """
        :return: the outdoor air specific humidity (in 0-1)
        """
        dew_point = dewpoint_from_relative_humidity(self.get_outdoor_air_temperature(), self.get_outdoor_air_relative_humidity())
        return specific_humidity_from_dewpoint(self.get_outdoor_air_pressure(), dew_point)

    def get_zenith_angle_sun(self):
        """
        :return: the zenith angle of the sun (in degrees)
        """
        timezone_offset = self.get_timezone()
        site = Location(latitude=self.get_latitude(), longitude=self.get_longitude(), tz=timezone_offset)
        timestamps = self.get_timestamps().tz_localize('UTC').tz_convert('Etc/GMT' + f"{-int(timezone_offset):+}")
        start_date = timestamps[0] + timedelta(hours=-timezone_offset)
        end_date = timestamps[-1] + timedelta(hours=-timezone_offset)
        dt = timestamps[1] - timestamps[0]
        solpos = site.get_solarposition(pd.date_range(start=start_date, end=end_date, freq=dt))
        return solpos['zenith']

    def get_azimuth_angle_sun(self):
        """
        :return: the azimuth angle of the sun (in degrees)
        """
        timezone_offset = self.get_timezone()
        site = Location(latitude=self.get_latitude(), longitude=self.get_longitude(), tz=timezone_offset)
        timestamps = self.get_timestamps().tz_localize('UTC').tz_convert('Etc/GMT' + f"{-int(timezone_offset):+}")
        start_date = timestamps[0] + timedelta(hours=-timezone_offset)
        end_date = timestamps[-1] + timedelta(hours=-timezone_offset)
        dt = timestamps[1] - timestamps[0]
        solpos = site.get_solarposition(pd.date_range(start=start_date, end=end_date, freq=dt))
        return solpos['azimuth']

    def get_outdoor_mean_radiant_temperature(self):
        """
        :return: the outdoor mean radiant temperature (in degrees Celcius)
        """
        elevation = [e if e > 0 else 0 for e in 90 - self.get_zenith_angle_sun()]
        outdoor_mean_radiant_flux_density = 0.7 * np.sin(np.deg2rad(elevation)) * self.get_direct_normal_irradiance().m \
                                    + 0.7 * self.get_diffuse_horizontal_irradiance().m \
                                    + 0.9 * self.get_horizontal_infrared_radiation_intensity().m
        return ((outdoor_mean_radiant_flux_density / sigma) ** (1 / 4) - 273.15) * units.degC



class EPWDataLoader(WeatherDataLoader):
    """
    Class to load EPW data.

    Attributes:
        weather_file: file containing EPW data.
    """
    __metaclass__ = ABCMeta

    def __init__(self, weather_file, year=datetime.today().year):
        """
        :param weather_file: file containg EPW data.
        """
        self.weather_file = weather_file
        self.epw_data = op.WeatherData.load(weather_file, create_datetime_instants=True, start_year=year)

    def get_instance(self):
        """
        :return: instance of weather data
        """
        weather_data = EnergyPlusWeatherData()
        weather_data.raw_epw_data = self.epw_data
        return weather_data

    def get_year(self):
        """
        :return: year weather data were collected
        """
        bounds = self.epw_data.get_bounds()
        return bounds[0].year

    def get_latitude(self):
        """
        :return: latitude weather data were collected
        """
        return float(self.epw_data._headers['latitude'])

    def get_longitude(self):
        """
        :return: longitude weather data were collected
        """
        return float(self.epw_data._headers['longitude'])

    def get_timezone(self):
        """
        :return: time zone weather data were collected
        """
        return float(self.epw_data._headers['timezone_offset'])

    def get_timestamps(self):
        """
        :return: timestamps at which weather data were collected
        """
        weather_dataframe = self.epw_data.get_weather_series()
        return weather_dataframe.axes[0]

    def get_outdoor_air_temperature(self):
        """
        :return: the outdoor air temperature (in ^oC)
        """
        return np.asarray(self.epw_data.get_weather_series()['drybulb']) * units.degC

    def get_outdoor_air_relative_humidity(self):
        """
        :return: the outdoor air relative humidity (in %)
        """
        return np.asarray(self.epw_data.get_weather_series()['relhum']) * units.percent

    def get_outdoor_air_pressure(self):
        """
        :return: the outdoor air temperature (in Pa)
        """
        return np.asarray(self.epw_data.get_weather_series()['atmos_pressure']) * units.Pa

    def get_direct_normal_irradiance(self):
        """
        :return: the direct normal irradiance (in W/m^2)
        """
        return np.asarray(self.epw_data.get_weather_series()['dirnorrad']) * (units.watts / (units.meter ** 2))

    def get_diffuse_horizontal_irradiance(self):
        """
        :return: the diffuse horizontal irradiance (in W/m^2)
        """
        return np.asarray(self.epw_data.get_weather_series()['difhorrad']) * (units.watts / (units.meter ** 2))

    def get_horizontal_infrared_radiation_intensity(self):
        """
        :return: the horizontal infrared radiation intensity (in W/m^2)
        """
        return np.asarray(self.epw_data.get_weather_series()['horirsky']) * (units.watts / (units.meter ** 2))

class EnergyPlusWeatherData(WeatherData):
    """
    Class representing EnergyPlus weather data.

    Attributes:
        raw_epw_data: raw epw data.
    """

    def __init__(self):
        self.raw_epw_data = None

    def set_year(self, new_year):
        """
        :param new_year: year weather data were collected
        """
        self.year = new_year
        weather_series = self.raw_epw_data.get_weather_series()
        vy = new_year * np.ones(len(weather_series))
        weather_series.year = weather_series.year.replace(to_replace = weather_series.axes[0], value = vy)
        self.raw_epw_data.set_weather_series(weather_series)

    def set_latitude(self, new_latitude):
        """
        :param new_latitude: latitude weather data were collected
        """
        self.latitude = new_latitude
        self.raw_epw_data._headers['latitude'] = str(new_latitude)

    def set_longitude(self, new_longitude):
        """
        :param new_longitude: longitude weather data were collected
        """
        self.longitude = new_longitude
        self.raw_epw_data._headers['longitude'] = str(new_longitude)

    def set_timezone(self, new_timezone):
        """
        :param new_timezone: time zone weather data were collected
        """
        self.timezone = new_timezone
        self.raw_epw_data._headers['timezone_offset'] = str(new_timezone)

    def set_outdoor_air_temperature(self, new_outdoor_air_temperature):
        """
        :param new_outdoor_air_temperature: new values for the outdoor air temperature (in ^oC)
        """
        self.outdoor_air_temperature = new_outdoor_air_temperature
        cdf = self.raw_epw_data.get_weather_series()
        cdf['drybulb'] = new_outdoor_air_temperature
        self.raw_epw_data.set_weather_series(cdf)

    def set_outdoor_air_relative_humidity(self, new_outdoor_air_relative_humidity):
        """
        :param new_outdoor_air_relative_humidity: new values for the outdoor air relative humidity (in %)
        """
        self.outdoor_air_relative_humidity = new_outdoor_air_relative_humidity
        cdf = self.raw_epw_data.get_weather_series()
        cdf['relhum'] = new_outdoor_air_relative_humidity
        self.raw_epw_data.set_weather_series(cdf)
    def save(self, file_name, out_dir='.'):
        """
        Save weather data.
        :param file_name: file name where weather data must be saved
        :param out_dir: output directory where weather data must be saved
        """
        self.raw_epw_data.save(os.path.join(out_dir, file_name), use_datetimes=False)

class BuildingLoader():
    """
    Class to load a building.

    Attributes:
        building_file: file in which details of the building are stored.
        x: position of the building on the x-axis
        y: position of the building on the y-axis
    """
    __metaclass__ = ABCMeta

    def __init__(self, building_file, x = 0.0, y = 0.0):
        """
        :param building_file: file in which details of the building are stored.
        :paran x: position of the building on the x-axis
        :paran y: position of the building on the y-axis
        """
        self.building_file = building_file
        self.x = x
        self.y = y

    def load(self):
        """
        Load the building
        :return: loaded building
        """
        building = Building(self.get_building_name())
        building.zones = self.get_building_zones()
        (x_center, y_center, z_center) = building.get_footprint().get_centroid()
        building.move(self.x - x_center, self.y - y_center)
        return building

    @abstractmethod
    def get_building_name(self):
        """
        :return: name of the building
        """
        pass

class BuildingEnergyModel():
    """
    Class representing a building energy model.

    Attributes:
        building: building being modelled
        building_loader: loader of building
        outputs: outputs resulting from simulations using the building energy model
    """
    __metaclass__ = ABCMeta

    def __init__(self, building_loader):
        """
        :param building_loader: loader of building
        """
        self.building_loader = building_loader
        self.building = None
        self.outputs = None

    @abstractmethod
    def update(self):
        """
        Update the modelled building with respect to outputs of simulations.
        """
        pass

class BuildingEnergySimulationPool():
    """
    Pool to perform simulations of a sequence of building energy models in parallel.

    Attributes:
        weather_data: weather data to perform simulations of building energy models.
        weather_data_loader: loader of weather data.
        nproc: number of processors to run in parallel.
        pool: list of building energy models used for parallel simulations.
    """
    __metaclass__ = ABCMeta

    def __init__(self, weather_data_loader, nproc = 2):
        """
        :param weather_data_loader: loader of weather data.
        :param nproc: number of processors to run in parallel.
        """
        self.weather_data = None
        self.weather_data_loader = weather_data_loader
        self.nproc = nproc
        self.pool = []

    def run(self):
        """
        Perform building energy simulations in parallel.
        :return: list of buildings resulting from simulation
        """
        self.create_simulation_environment()
        for bem in self.pool:
            if bem.building is None:
                bem.building = bem.building_loader.load()
        if self.weather_data is None:
            self.weather_data = self.weather_data_loader.load()
        self.weather_data.save(self.get_weather_data_filename(), self.get_weather_data_directory())
        self.run_parallel_simulation()
        for bem in self.pool:
            while True:
                try:
                    bem.outputs = self.get_building_outputs(bem.building.name)
                    bem.update()
                    break
                except FileNotFoundError:
                    pass
                except PermissionError:
                    pass
        self.cleanup()

    @abstractmethod
    def create_simulation_environment(self):
        """
        Create simulation environment to perform simulations using the pool of building energy models
        """
        pass

    @abstractmethod
    def get_weather_data_filename(self):
        """
        :return: filename under which weather data must be saved.
        """
        pass

    @abstractmethod
    def get_weather_data_directory(self):
        """
        :return: directory under which weather data must be saved.
        """
        pass

    @abstractmethod
    def run_parallel_simulation(self):
        """
        Run parallel building energy simulations.
        """
        pass

    @abstractmethod
    def get_building_outputs(self, building_name):
        """
        :param building_name: name of the building
        :return: outputs of the simulation for the building
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
        Cleanup the simulation environment.
        """
        pass

class IDFBuildingLoader(BuildingLoader):
    """
    Class to load a building from an IDF file

    Attributes:
        building_file: file in which details of the building are stored.
        idf_objects: IDF objects.
    """

    def __init__(self, building_file, x = 0.0, y = 0.0):
        """
        :param building_file: IDF file containing details of the building.
        :paran x: position of the building on the x-axis
        :paran y: position of the building on the y-axis
        """
        BuildingLoader.__init__(self, building_file, x, y)
        self.idf_objects = op.Epm.load(building_file)

    def get_building_name(self):
        """
        :return: name of the building
        """
        return self.idf_objects.Building.one().name
    def get_building_zones(self):
        """
        :return: name of the building
        """
        zones = []
        for zone_info in self.idf_objects.Zone:
            zone = Zone(zone_info.name)
            for surface in self.idf_objects.BuildingSurface_Detailed.select(
                    lambda x: x.zone_name.name == zone.name):
                number_points = int((len(surface) - 11) / 3)
                points = np.zeros((number_points, 3))
                offset = 0
                for point_ID in range(number_points):
                    points[point_ID][0] = surface[11 + offset]
                    points[point_ID][1] = surface[12 + offset]
                    points[point_ID][2] = surface[13 + offset]
                    offset = offset + 3
                if surface.surface_type == 'wall':
                    exterior_wall = ExteriorWall(surface.name, points)
                    for window_surface in self.idf_objects.FenestrationSurface_Detailed.select(
                        lambda x: x.building_surface_name.name == exterior_wall.name):
                        window_points = np.zeros((4, 3))
                        window_offset = 0
                        for point_ID in range(4):
                            window_points[point_ID][0] = window_surface[9 + window_offset]
                            window_points[point_ID][1] = window_surface[10 + window_offset]
                            window_points[point_ID][2] = window_surface[11 + window_offset]
                            window_offset = window_offset + 3
                        exterior_wall.windows.append(Surface(window_surface.name, window_points))
                    zone.exterior_walls.append(exterior_wall)
                elif surface.surface_type == 'floor':
                    zone.ground_floor = Surface(surface.name, points)
                elif surface.surface_type == 'roof':
                    zone.roofs.append(Surface(surface.name, points))
            zones.append(zone)
        return zones

class EnergyPlusModel(BuildingEnergyModel):
    """
    Class representing an EnergyPlus model

    Attributes:
        building: building being modelled
        building_loader: loader of building
        outputs: outputs resulting from simulations using the building energy model
    """

    def __init__(self, building_loader):
        """
        :param building_loader: loader of building
        """
        BuildingEnergyModel.__init__(self, building_loader)


    def update(self):
        """
        Update the modelled building with respect to outputs of simulations.
        """
        idcols = self.outputs.keys().to_list()
        for zone in self.building.zones:
            zone_name = zone.name.upper()
            idx_cooling_load = np.where([(zone_name in s) for s in idcols])[0]
            if 'Zone Ideal Loads Zone Sensible Cooling Rate' in idcols[idx_cooling_load[0]]:
                zone.sensible_load = pd.Series(self.outputs[idcols[idx_cooling_load[0]]] * units.watt, index = self.outputs.index)
                zone.latent_load = pd.Series(self.outputs[idcols[idx_cooling_load[1]]] * units.watt, index = self.outputs.index)
            else:
                zone.sensible_load = pd.Series(self.outputs[idcols[idx_cooling_load[1]]] * units.watt, index=self.outputs.index)
                zone.latent_load = pd.Series(self.outputs[idcols[idx_cooling_load[0]]] * units.watt, index=self.outputs.index)
            for roof in zone.roofs:
                roof_name = roof.name.upper()
                idx_roof_surface_temperature = np.where([(roof_name in s) for s in idcols])[0]
                roof.temperature = pd.Series(self.outputs[idcols[idx_roof_surface_temperature[0]]] * units.degC, index = self.outputs.index)
            for exterior_wall in zone.exterior_walls:
                exterior_wall_name = exterior_wall.name.upper()
                idx_exterior_wall_surface_temperature = np.where([(exterior_wall_name in s) for s in idcols])[0]
                exterior_wall.temperature = pd.Series(self.outputs[idcols[idx_exterior_wall_surface_temperature[0]]] * units.degC, index = self.outputs.index)
                for window in exterior_wall.windows:
                    window_name = window.name.upper()
                    idx_window_surface_temperature = np.where([(window_name in s) for s in idcols])[0]
                    window.temperature = pd.Series(self.outputs[idcols[idx_window_surface_temperature[0]]])
            ground_floor_name = zone.ground_floor.name.upper()
            idx_ground_floor_surface_temperature = np.where([(ground_floor_name in s) for s in idcols])[0]
            zone.ground_floor.temperature = pd.Series(self.outputs[idcols[idx_ground_floor_surface_temperature[0]]] * units.degC, index=self.outputs.index)


def read_ep_outputs(building_name, output_dir, year = datetime.today().year):
    """
    Read outputs generated by the EnergyPlus simulation engine.
    :param building_name: name of the building
    :param output_dir: directory in which the outputs are generated
    :param year: year in which simulation were performed
    :return: outputs as a dataframe
    """
    if platform.system() == 'Windows':
        if output_dir.endswith('\\'):
            output_file = output_dir + building_name + '.csv'
        else:
            output_file = output_dir + '\\' + building_name + '.csv'
    elif platform.system() == 'Linux':
        if output_dir.endswith('/'):
            output_file = output_dir + building_name + '.idfout.csv'
        else:
            output_file = output_dir + '/' + building_name + '.idfout.csv'
    df = pd.read_csv(output_file, index_col=[0])
    idxs = [str(year) + '/' + s[1:] for s in df.index.tolist()]
    idxd = []
    for sd in idxs:
        if '24:' in sd:
            s = sd.replace('24:', '00:')
            d = datetime.strptime(s, '%Y/%m/%d  %H:%M:%S')
            idxd.append(d + timedelta(days=1))
        else:
            idxd.append(datetime.strptime(sd, '%Y/%m/%d  %H:%M:%S'))
    return df.set_index(pd.DatetimeIndex(idxd))

def run_energyplus_linux(input_file):
    command = ["energyplus", "-x", "-r", "-w", os.getenv('ENERGYPLUS') + "/WeatherData/LOCAL_CLIMATE.epw",
               "-p", os.path.basename(input_file), "-d", os.path.dirname(input_file), "-r", input_file]
    subprocess.run(command)

class EnergyPlusSimulationPool(BuildingEnergySimulationPool):
    """
    Pool to perform simulations using EnergyPlus in parallel.

    Attributes:
        nproc: number of processors to run in parallel.
        pool: list of building energy models used for parallel simulations.
        output_dir: directory in which parallel simulations must be performed and outputs being stored.
    """
    def __init__(self, weather_data_loader, nproc = 2, output_dir = '.'):
        BuildingEnergySimulationPool.__init__(self, weather_data_loader, nproc)
        self.output_dir = output_dir
    def create_simulation_environment(self):
        """
        Create simulation environment to perform simulations using the pool of building energy models
        """
        ENERGYPLUS_DIR = os.getenv('ENERGYPLUS')
        if (self.output_dir != '.') and (not os.path.isdir(self.output_dir)):
            os.mkdir(self.output_dir)
        for bem in self.pool:
            shutil.copy(bem.building_loader.building_file, self.output_dir)
        shutil.copy(os.path.join(ENERGYPLUS_DIR, 'RunDirMulti.bat'), self.output_dir)
        if self.weather_data is not None:
            self.weather_data_loader = EPWDataLoader(os.path.join(ENERGYPLUS_DIR, 'WeatherData', 'LOCAL_CLIMATE.epw'), year=self.weather_data_loader.get_year())
    def get_weather_data_filename(self):
        """
        :return: filename under which weather data must be saved.
        """
        return 'LOCAL_CLIMATE.epw'
    def get_weather_data_directory(self):
        """
        :return: directory under which weather data must be saved.
        """
        return os.path.join(os.getenv('ENERGYPLUS'), 'WeatherData')

    def run_parallel_simulation(self):
        """
        Run parallel building energy simulations.
        """
        if platform.system() == 'Windows':
            p = Popen('RunDirMulti.bat LOCAL_CLIMATE ' + str(self.nproc), cwd=self.output_dir, shell=True)
            p.communicate()
        elif platform.system() == 'Linux':
            if self.output_dir.endswith("/"):
                input_files = [self.output_dir + file for file in os.listdir(self.output_dir) if file.endswith(".idf")]
            else:
                input_files = [self.output_dir + "/" + file for file in os.listdir(self.output_dir) if file.endswith(".idf")]
            for input_file in input_files:
                run_energyplus_linux(input_file)

    def get_building_outputs(self, building_name):
        """
        :param building_name: name of the building
        :return: outputs of the simulation for the building
        """
        return read_ep_outputs(building_name, self.output_dir, year = self.weather_data.year)

    def cleanup(self):
        """
        Cleanup the simulation environment.
        """
        for f in glob.glob(os.path.join(self.output_dir, '*.audit')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.bnd')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.csv')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.eio')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.err')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.eso')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.expidf')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.idf')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.mdd')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.mtd')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.rdd')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.rvaudit')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.shd')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.sql')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.svg')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, '*.html')):
            os.remove(f)
        for f in glob.glob(os.path.join(self.output_dir, 'tempsim*')):
            shutil.rmtree(f)
        os.remove(os.path.join(self.output_dir, 'RunDirMulti.bat'))

class DataDrivenBuildingEnergyModel(BuildingEnergyModel):
    """
    Class representing a data driven building energy model.

    Attributes:
        building: building being modelled.
        building_loader: loader of building.
        outputs: outputs resulting from simulations using the building energy model.
        weather_data: weather data to be considered for boundary conditions of the data driven building energy model.
        training_split_ratio: ratio between the size of the training set and the total data set over the period of simulation.
        target_building_load: sensible and latent load as measured by a smart meter or generated using a detailed building energy model.
        start_date: starting date of simulation.
        end_date: ending date of simulation.
        dt: timestep of simulation.
        output_dir: directory where outputs are saved.
    """
    __metaclass__ = ABCMeta

    def __init__(self, building_loader, weather_data = None, start_date = None, end_date = None, dt = None, training_split_ratio = 0.0, output_dir = '.'):
        """
        :param building_loader: loader of building
        """
        BuildingEnergyModel.__init__(self, building_loader)
        self.weather_data = weather_data
        self.training_split_ratio = training_split_ratio
        self.start_date = start_date
        self.end_date = end_date
        self.dt = dt
        self.output_dir = output_dir
        self.target_sensible_load = None
        self.target_latent_load = None
        self.target_walls_temperature = None
        self.target_ground_floor_temperature = None

    def update(self):
        """
        Update the modelled building with respect to outputs of simulations.
        """
        file_path = os.path.join(self.output_dir, self.building.name + '.csv')
        if os.path.exists(file_path):
            os.remove(file_path)
        self.outputs.to_csv(file_path)

    def get_target_building_load(self):
        """
        :return: the target building load
        """
        return self.building.get_building_load_measurements()

    @abstractmethod
    def train(self, start_date, end_date, dt):
        """
        Train the data driven building energy model
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        pass

    @abstractmethod
    def test(self, start_date, end_date, dt):
        """
        Test the data driven building energy model
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        pass

    @abstractmethod
    def get_previous_error_building_load(self, start_date, end_date, dt):
        """
        Previous error made on building load
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        pass

    @abstractmethod
    def get_current_error_building_load(self, start_date, end_date, dt):
        """
        Current error made on building load
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        pass

    @abstractmethod
    def update_previous_solution(self):
        """
        Update previous solution found by the data driven building energy model
        """
        pass

class LinearStateSpaceBuildingEnergyModel(DataDrivenBuildingEnergyModel):
    """
    Class representing a single zone model

    Attributes:
        building: building being modelled
        building_loader: loader of building
        outputs: outputs resulting from simulations using the building energy model
        training_split_ratio: ratio between the size of the training set and the total data set over the period of simulation.
        start_date: starting date of simulation.
        end_date: ending date of simulation.
        dt: timestep of simulation.
        previous_lumped_thermal_parameters: previously found lumped thermal parameters.
        current_lumped_thermal_parameters: currently found lumped thermal parameters.
        error_function: error function to optimize the building load.
    """

    def __init__(self, building_loader, weather_data = None, start_date = None, end_date = None, dt = None, training_split_ratio = 0.0, output_dir = '.', error_function = RootMeanSquareError(),
                 indoor_temperature = 24, indoor_humidity = 0.01, internal_heat_gains = 150000):
        """
        :param building_loader: loader of building
        """
        DataDrivenBuildingEnergyModel.__init__(self, building_loader, weather_data, start_date, end_date, dt, training_split_ratio, output_dir)
        self.previous_lumped_thermal_parameters = None
        self.current_lumped_thermal_parameters = None
        self.error_function = error_function
        self.indoor_temperature = indoor_temperature
        self.indoor_humidity = indoor_humidity
        self.internal_heat_gains = internal_heat_gains

    def get_input_vectors(self, start_date, end_date, dt):
        """
        :param start_date: start date of simulations
        :param end_date: end date of simulations
        :param dt: timestep of simulations
        """
        input_vectors = []
        input_vectors.append(pd.Series(data=self.indoor_temperature, index=pd.date_range(start=start_date, end=end_date, freq=dt)).values.tolist())
        outdoor_air_temperature = pd.Series(data=self.weather_data.outdoor_air_temperature, index=self.weather_data.timestamps)
        input_vectors.append(outdoor_air_temperature.resample(dt).interpolate()[start_date:end_date].values.tolist())
        outdoor_mean_radiant_temperature = pd.Series(data=self.weather_data.outdoor_mean_radiant_temperature, index=self.weather_data.timestamps)
        input_vectors.append(outdoor_mean_radiant_temperature.resample(dt).interpolate()[start_date:end_date].values.tolist())
        input_vectors.append(pd.Series(data=self.indoor_humidity, index=pd.date_range(start=start_date, end=end_date, freq=dt)).values.tolist())
        outdoor_air_specific_humidity = pd.Series(data=self.weather_data.outdoor_air_specific_humidity, index=self.weather_data.timestamps)
        input_vectors.append(outdoor_air_specific_humidity.resample(dt).interpolate()[start_date:end_date].values.tolist())
        input_vectors.append(pd.Series(data=self.internal_heat_gains, index=pd.date_range(start=start_date, end=end_date, freq=dt)).values.tolist())
        return np.asarray(input_vectors)

    def get_state_matrix(self, lumped_thermal_parameters):
        """
        :return: state matrix
        """
        thermal_capacitance_building_exterior_surface = lumped_thermal_parameters[0]
        thermal_capacitance_building_interior_floor = lumped_thermal_parameters[1]
        thermal_resistance_outdoor_air_exterior_surface = lumped_thermal_parameters[2]
        thermal_resistance_outdoor_mean_radiant_exterior_surface = lumped_thermal_parameters[3]
        thermal_resistance_indoor_air_exterior_surface = lumped_thermal_parameters[4]
        thermal_resistance_interior_floor_exterior_surface = lumped_thermal_parameters[5]
        thermal_resistance_indoor_air_interior_floor = lumped_thermal_parameters[6]
        thermal_resistance_outdoor_mean_radiant_interior_floor = lumped_thermal_parameters[7]
        A = np.zeros((2, 2))
        A[0, 0] = -(1.0 / thermal_resistance_outdoor_air_exterior_surface +
                    1.0 / thermal_resistance_outdoor_mean_radiant_exterior_surface +
                    1.0 / thermal_resistance_indoor_air_exterior_surface +
                    1.0 / thermal_resistance_interior_floor_exterior_surface) / thermal_capacitance_building_exterior_surface
        A[0, 1] = 1.0 / (thermal_resistance_interior_floor_exterior_surface * thermal_capacitance_building_exterior_surface)
        A[1, 0] = 1.0 / (thermal_resistance_interior_floor_exterior_surface * thermal_capacitance_building_interior_floor)
        A[1, 1] = -(1.0 / thermal_resistance_interior_floor_exterior_surface +
                    1.0 / thermal_resistance_indoor_air_interior_floor +
                    1.0 / thermal_resistance_outdoor_mean_radiant_interior_floor) / thermal_capacitance_building_interior_floor
        return A

    def get_input_matrix(self, lumped_thermal_parameters):
        """
        :return: input matrix
        """
        thermal_capacitance_building_exterior_surface = lumped_thermal_parameters[0]
        thermal_capacitance_building_interior_floor = lumped_thermal_parameters[1]
        thermal_resistance_outdoor_air_exterior_surface = lumped_thermal_parameters[2]
        thermal_resistance_outdoor_mean_radiant_exterior_surface = lumped_thermal_parameters[3]
        thermal_resistance_indoor_air_exterior_surface = lumped_thermal_parameters[4]
        thermal_resistance_indoor_air_interior_floor = lumped_thermal_parameters[6]
        thermal_resistance_outdoor_mean_radiant_interior_floor = lumped_thermal_parameters[7]
        radiant_portion_internal_heat_gains = lumped_thermal_parameters[10]
        latent_portion_internal_heat_gains = lumped_thermal_parameters[11]

        B = np.zeros((2, 6))
        B[0, 0] = 1.0 / (thermal_resistance_indoor_air_exterior_surface * thermal_capacitance_building_exterior_surface)
        B[0, 1] = 1.0 / (thermal_resistance_outdoor_air_exterior_surface * thermal_capacitance_building_exterior_surface)
        B[0, 2] = 1.0 / (thermal_resistance_outdoor_mean_radiant_exterior_surface * thermal_capacitance_building_exterior_surface)
        B[0, 5] = (1.0 - radiant_portion_internal_heat_gains - latent_portion_internal_heat_gains) / thermal_capacitance_building_exterior_surface
        B[1, 0] = 1.0 / (thermal_resistance_indoor_air_interior_floor * thermal_capacitance_building_interior_floor)
        B[1, 2] = 1.0 / (thermal_resistance_outdoor_mean_radiant_interior_floor * thermal_capacitance_building_interior_floor)
        B[1, 5] = radiant_portion_internal_heat_gains / thermal_capacitance_building_interior_floor
        return B

    def get_output_matrix(self, lumped_thermal_parameters):
        """
        :return: output matrix
        """
        thermal_resistance_indoor_air_exterior_surface = lumped_thermal_parameters[4]
        thermal_resistance_indoor_air_interior_floor = lumped_thermal_parameters[6]
        C = np.zeros((2, 2))
        C[0, 0] = 1.0 / thermal_resistance_indoor_air_exterior_surface
        C[0, 1] = 1.0 / thermal_resistance_indoor_air_interior_floor
        return C

    def get_direct_transition_matrix(self, lumped_thermal_parameters):
        """
        :return: direct transition matrix
        """
        thermal_resistance_indoor_air_exterior_surface = lumped_thermal_parameters[4]
        thermal_resistance_indoor_air_interior_floor = lumped_thermal_parameters[6]
        thermal_resistance_outdoor_air_indoor_air = lumped_thermal_parameters[8]
        mass_resistance_outdoor_air_indoor_air = lumped_thermal_parameters[9]
        radiant_portion_internal_heat_gains = lumped_thermal_parameters[10]
        latent_portion_internal_heat_gains = lumped_thermal_parameters[11]

        D = np.zeros((2, 6))
        D[0, 0] = - (1.0 / thermal_resistance_indoor_air_exterior_surface +
                     1.0 / thermal_resistance_indoor_air_interior_floor +
                     1.0 / thermal_resistance_outdoor_air_indoor_air)
        D[0, 1] = 1.0 / thermal_resistance_outdoor_air_indoor_air
        D[0, 5] = 1.0 - radiant_portion_internal_heat_gains - latent_portion_internal_heat_gains
        D[1, 3] = - 1.0 / mass_resistance_outdoor_air_indoor_air
        D[1, 4] = 1.0 / mass_resistance_outdoor_air_indoor_air
        D[1, 5] = latent_portion_internal_heat_gains
        return D

    def get_state_outputs(self, lumped_thermal_parameters, start_date, end_date, dt):
        U = np.transpose(self.get_input_vectors(start_date, end_date, dt))
        A = self.get_state_matrix(lumped_thermal_parameters)
        B = self.get_input_matrix(lumped_thermal_parameters)
        C = self.get_output_matrix(lumped_thermal_parameters)
        D = self.get_direct_transition_matrix(lumped_thermal_parameters)
        sys = sig.StateSpace(A, B, C, D)
        sys_d = sys.to_discrete(dt=dt.seconds, method='backward_diff')
        x0 = np.asarray([40.0, 20.0])
        t, Y, X = sig.dlsim(sys_d, u=U, x0=x0)
        X = np.transpose(X)
        Y = np.transpose(Y)
        return (Y, X)

    def train(self, start_date, end_date, dt):
        """
        Train the data driven building energy model
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        N = 12
        lb = np.asarray([1e4, 1e4, 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 1e-6, 0.0, 0.0])
        ub = np.asarray([1e6, 1e6, 1e-1, 1e-1, 1e-1, 1e-1, 1e-1, 1e-1, 1e-1, 1e-4, 1.0, 1.0])
        if self.previous_lumped_thermal_parameters is None:
            self.previous_lumped_thermal_parameters = np.random.uniform(lb, ub, size = 12)
        problem = self.MultiObjectiveProblem(n_var=N, n_obj=4, lb=lb, ub=ub, bem=self.copy(),
                                             start_date=start_date, end_date=end_date, dt=dt)
        algorithm = NSGA2(pop_size=40, n_offsprings=10, sampling=FloatRandomSampling(),
                          crossover=SBX(prob=0.9, eta=15), mutation=PM(eta=20),
                          eliminate_duplicates=True)
        termination = get_termination("n_gen", 40)
        results = minimize(problem, algorithm, termination, seed=1, save_history=True, verbose=True)
        self.current_lumped_thermal_parameters = results.X[np.argmin(results.F[:, 0]), :]
        if self.get_previous_error_building_load(start_date, end_date, dt) < self.get_current_error_building_load(start_date, end_date, dt):
            Y, X = self.get_state_outputs(self.previous_lumped_thermal_parameters, start_date, end_date, dt)
        else:
            Y, X = self.get_state_outputs(self.current_lumped_thermal_parameters, start_date, end_date, dt)
        num_zones = len(self.building.zones)
        for zone in self.building.zones:
            zone.sensible_load = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=Y[0, :]) / num_zones
            zone.latent_load = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=Y[1, :]) / num_zones
            for exterior_wall in zone.exterior_walls:
                exterior_wall.temperature = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[0, :])
                for window in exterior_wall.windows:
                    window.temperature = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[0, :])
            zone.ground_floor.temperature = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[1, :])


    def test(self, start_date, end_date, dt):
        """
        Test the data driven building energy model
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        Y, X = self.get_state_outputs(self.current_lumped_thermal_parameters, start_date, end_date, dt)
        num_zones = len(self.building.zones)
        for zone in self.building.zones:
            if zone.sensible_load is not None:
                zone.sensible_load = pd.concat([zone.sensible_load, pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=Y[0, :]) / num_zones])
            else:
                zone.sensible_load = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=Y[0, :]) / num_zones
            if zone.latent_load is not None:
                zone.latent_load = pd.concat([zone.latent_load, pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=Y[1, :]) / num_zones])
            else:
                zone.latent_load = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=Y[1, :]) / num_zones
            for exterior_wall in zone.exterior_walls:
                if exterior_wall.temperature is not None:
                    exterior_wall.temperature = pd.concat([exterior_wall.temperature, pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[0, :])])
                else:
                    exterior_wall.temperature = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[0, :])
                for window in exterior_wall.windows:
                    if window.temperature is not None:
                        window.temperature = pd.concat([window.temperature, pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[0, :])])
                    else:
                        window.temperature = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[0, :])
            if zone.ground_floor.temperature is not None:
                zone.ground_floor.temperature = pd.concat([zone.ground_floor.temperature, pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[1, :])])
            else:
                zone.ground_floor.temperature = pd.Series(index=pd.date_range(start=start_date, end=end_date, freq=dt), data=X[1, :])

    def get_previous_error_building_load(self, start_date, end_date, dt):
        """
        Previous error made on building load
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        Y, X = self.get_state_outputs(self.previous_lumped_thermal_parameters, start_date, end_date, dt)
        return self.error_function.err(Y[0, :] + Y[1, :],
                                       self.target_sensible_load[start_date:end_date].resample(dt).interpolate().values +
                                       self.target_latent_load[start_date:end_date].resample(dt).interpolate().values)

    def get_current_error_building_load(self, start_date, end_date, dt):
        """
        Current error made on building load
        :param start_date: date to start simulation
        :param end_date: date to end simulation
        :param dt: timestamp of simulation
        """
        Y, X = self.get_state_outputs(self.current_lumped_thermal_parameters, start_date, end_date, dt)
        return self.error_function.err(Y[0, :] + Y[1, :],
                                       self.target_sensible_load[start_date:end_date].resample(dt).interpolate().values +
                                       self.target_latent_load[start_date:end_date].resample(dt).interpolate().values)

    def update_previous_solution(self):
        """
        Update previous solution found by the data driven building energy model
        """
        self.current_lumped_thermal_parameters = self.previous_lumped_thermal_parameters

    def copy(self):
        """
        Copy of the linear state space urban microclimate model
        :return: copy of the linear state space urban microclimate model
        """
        instance = LinearStateSpaceBuildingEnergyModel(self.building_loader, weather_data=self.weather_data)
        instance.building_loader = None
        instance.building = self.building
        instance.target_sensible_load = self.target_sensible_load
        instance.target_latent_load = self.target_latent_load
        instance.target_walls_temperature = self.target_walls_temperature
        instance.target_ground_floor_temperature = self.target_ground_floor_temperature
        return instance

    class MultiObjectiveProblem(ElementwiseProblem):
        """
        Class stating the multi objective problem we would like to optimise to find convective heat transfer coefficients.

        Attributes:
            umm: the linear state space urban microclimate model to optimize
            start_date: date to start simulation
            end_date: date to end simulation
            dt: timestamp of simulation
        """

        def __init__(self, n_var, n_obj, lb, ub, bem, start_date, end_date, dt):
            """
            :param n_var: number of variables to optimize
            :param n_obj: number of objectives to optimize
            :param lb: lower bounds of each variable
            :param ub: upper bounds of each variable
            :param bem: building energy model to optimize
            :param start_date: date to start simulation
            :param end_date: date to end simulation
            :param dt: timestamp of simulation
            """
            ElementwiseProblem.__init__(self, n_var=n_var, n_obj=n_obj, xl=lb, xu=ub)
            self.bem = bem
            self.start_date = start_date
            self.end_date = end_date
            self.dt = dt

        def _evaluate(self, x, out, *args, **kwargs):
            """
            :param x: list of heat transfer coefficients to optimize
            :param out: objectives to optimize
            """
            Y, X = self.bem.get_state_outputs(x, self.start_date, self.end_date, self.dt)
            error_function = RootMeanSquareError()
            out["F"] = [error_function.err(Y[0, :], self.bem.target_sensible_load[self.start_date:self.end_date].resample(self.dt).interpolate().values),
                        error_function.err(Y[1, :], self.bem.target_latent_load[self.start_date:self.end_date].resample(self.dt).interpolate().values),
                        error_function.err(X[0, :], self.bem.target_walls_temperature[self.start_date:self.end_date].resample(self.dt).interpolate().values),
                        error_function.err(X[1, :], self.bem.target_ground_floor_temperature[self.start_date:self.end_date].resample(self.dt).interpolate().values)]

def simulate(ddbem):
    """
    :return: results of simulation of a single zone model.
    """
    if ddbem.training_split_ratio > 0.0:
        dsplit = int(ddbem.training_split_ratio * (ddbem.end_date - ddbem.start_date) / ddbem.dt)
        split_date = ddbem.start_date + dsplit * ddbem.dt
        ddbem.train(ddbem.start_date, split_date, ddbem.dt)
        previous_error_building_load = ddbem.get_previous_error_building_load(ddbem.start_date, split_date, ddbem.dt)
        current_error_building_load = ddbem.get_current_error_building_load(ddbem.start_date, split_date, ddbem.dt)
        if previous_error_building_load > current_error_building_load:
            ddbem.update_previous_solution()
        ddbem.test(split_date + ddbem.dt, ddbem.end_date, ddbem.dt)
    else:
        ddbem.test(ddbem.start_date, ddbem.end_date, ddbem.dt)

class DataDrivenBuildingEnergySimulationPool(BuildingEnergySimulationPool):
    """
    Pool to perform simulations using EnergyPlus in parallel.

    Attributes:
        nproc: number of processors to run in parallel.
        pool: list of building energy models used for parallel simulations.
        start_date: start date of simulations
        end_date: end date of simulations
        dt: timestep of simulations
        bems_dir: directory in which building energy models to emulate are stored
        output_dir: directory in which simulation outputs will be stored
    """
    def __init__(self, weather_data_loader, start_date, end_date, dt, nproc = 2, bems_dir = '.', output_dir = '.'):
        BuildingEnergySimulationPool.__init__(self, weather_data_loader, nproc)
        self.start_date = start_date
        self.end_date = end_date
        self.dt = dt
        self.bems_dir = bems_dir
        self.output_dir = output_dir

    def create_simulation_environment(self):
        """
        Create simulation environment to perform simulations using the pool of building energy models
        """
        pass

    def get_weather_data_filename(self):
        """
        :return: filename under which weather data must be saved.
        """
        return 'LOCAL_CLIMATE.epw'

    def get_weather_data_directory(self):
        """
        :return: directory under which weather data must be saved.
        """
        return os.path.join(os.getenv('ENERGYPLUS'), 'WeatherData')

    def run_parallel_simulation(self):
        """
        Run parallel building energy simulations.
        """
        for ddbem in self.pool:
            ddbem.weather_data = self.weather_data
            ddbem.start_date = self.start_date
            ddbem.end_date = self.end_date
            ddbem.dt = self.dt
            ddbem.output_dir = self.output_dir
            df = pd.read_csv(os.path.join(self.bems_dir, ddbem.building.name +'.csv'), index_col=0, parse_dates=True)
            ddbem.target_sensible_load = pd.Series(index=df.index, data=df['Total sensible load'].values).drop_duplicates()
            ddbem.target_latent_load = pd.Series(index=df.index, data=df['Total latent load'].values).drop_duplicates()
            ddbem.target_walls_temperature = pd.Series(index=df.index, data=df['Average walls surface temperature'].values).drop_duplicates()
            ddbem.target_ground_floor_temperature = pd.Series(index=df.index, data=df['Ground floor surface temperature'].values).drop_duplicates()
            simulate(ddbem)
        # with multiprocessing.Pool(self.nproc) as mpool:
        #     results = mpool.map(simulate, self.pool)

    def get_building_outputs(self, building_name):
        """
        :param building_name: name of the building
        :return: outputs of the simulation for the building
        """
        building = None
        for ddbem in self.pool:
            if ddbem.building.name == building_name:
                building = ddbem.building
                break
        data = {
            'Total sensible load': building.get_sensible_load().values,
            'Total latent load': building.get_latent_load().values,
            'Average walls surface temperature': building.get_walls_temperature().values,
            'Ground floor surface temperature': building.get_ground_floor_temperature().values
        }
        return pd.DataFrame(index=pd.date_range(self.start_date, self.end_date, freq=self.dt), data=data)

    def cleanup(self):
        """
        Cleanup the simulation environment.
        """
        pass


