"""
Module dedicated to extract data stored within a 3D city model.

Delft University of Technology
Dr. Miguel Martin
"""

import os
import json
from sciencespy.dom import *
from shapely.geometry import Polygon
from pyproj import Proj, transform, Transformer
import pytz
from enum import Enum
import numpy as np
from eppy.modeleditor import IDF

class CityModelFormatException(Exception):
    """
    Class of exception referring to the format of a 3D city model
    """
    pass

class CityModelCoordinateReferenceSystemException(Exception):
    """
    Class of exception referring to the format of a 3D city model
    """
    pass

class CityModelReferenceSystem(Enum):
    UNKNOWN = 0
    EPSG_7415 = 1
    CRS84 = 2

class CompressCoordinates():
    """
    Class used to compress coordinates
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def compress(self, x, y):
        """
        Compress the coordinates
        :param x: x-coordinates to compress
        :param y: y-coordinates to compress
        :return: compressed xy coordinates
        """
        pass

class CompressCoordinatesScaleTranslate(CompressCoordinates):
    """
    Class to compress coordinates based on the scale and translate of the map

    Attributes:
        xscale: scale of x-axis
        yscal: scale of y-axis
        xtranslate: translate of x-axis
        ytranslate: translate of y-axis
    """

    def __init__(self, xscale, yscale, zscale, xtranslate, ytranslate, ztranslate):
        """
        Construct the compression of coordinates based on the scale and translate
        :param xscale: scale of x-axis
        :param yscal: scale of y-axis
        :param zscale: scale of z-axis
        :param xtranslate: translate of x-axis
        :param ytranslate: translate of y-axis
        :param ztranslate: translate of z-axis
        """
        self.xscale = xscale
        self.yscale = yscale
        self.zscale = zscale
        self.xtranslate = xtranslate
        self.ytranslate = ytranslate
        self.ztranslate = ztranslate

    def compress(self, x, y, z):
        """
        Compress the coordinates
        :param x: x-coordinates to compress
        :param y: y-coordinates to compress
        :return: compressed xy coordinates
        """
        xc = [(x[n] - self.xtranslate) / self.xscale for n in range(0, len(x))]
        yc = [(y[n] - self.ytranslate) / self.yscale for n in range(0, len(y))]
        zc = [(z[n] - self.ztranslate) / self.zscale for n in range(0, len(z))]
        return xc, yc, zc

class DecompressCoordinates():
    """
    Class used to decompress coordinates
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def decompress(self, x, y, z):
        """
        Decompress the coordinates
        :param x: x-coordinates to decompress
        :param y: y-coordinates to decompress
        :param z: z-coordinates to decompress
        :return: decompressed xy coordinates
        """
        pass

class DecompressCoordinatesScaleTranslate(CompressCoordinates):
    """
    Class to decompress coordinates based on the scale and translate of the map

    Attributes:
        xscale: scale of x-axis
        yscal: scale of y-axis
        xtranslate: translate of x-axis
        ytranslate: translate of y-axis
    """

    def __init__(self, xscale, yscale, zscale, xtranslate, ytranslate, ztranslate):
        """
        Construct the decompression of coordinates based on the scale and translate
        :param xscale: scale of x-axis
        :param yscal: scale of y-axis
        :param zscale: scale of z-axis
        :param xtranslate: translate of x-axis
        :param ytranslate: translate of y-axis
        :param ztranslate: translate of z-axis
        """
        self.xscale = xscale
        self.yscale = yscale
        self.zscale = zscale
        self.xtranslate = xtranslate
        self.ytranslate = ytranslate
        self.ztranslate = ztranslate

    def decompress(self, x, y, z):
        """
        Decompress the coordinates
        :param x: x-coordinates to decompress
        :param y: y-coordinates to decompress
        :param z: z-coordinates to decompress
        :return: decompressed xyz coordinates
        """
        xd = [(x[n] * self.xscale) + self.xtranslate for n in range(0, len(x))]
        yd = [(y[n] * self.yscale) + self.ytranslate for n in range(0, len(y))]
        zd = [(z[n] * self.zscale) + self.ztranslate for n in range(0, len(z))]
        return xd, yd, zd

class CityModelLoader():
    """
    Class used to load a 3D city model as a list of buildings.

    Attributs:
        city_model_filename: file containing the 3D city model
        _city_model_data: data stored in the 3D city model to be expressed as a list of buildings.
        reference_system: reference system used in the 3D city model
    """
    __metaclass__ = ABCMeta

    def __init__(self, city_model_filename):
        """
        :param city_model_filename: file containing the 3D city model
        """
        self.city_model_filename = city_model_filename
        self._city_model_data = None
        self.reference_system = None

    def load(self):
        """
        Load the 3D city model as a list of buildings
        :return: list of buildings stored in the 3D city model
        """
        self._city_model_data = self.read_city_model()
        self.reference_system = self.get_reference_system()
        building_names = self.get_building_names()
        buildings = []
        for bn in building_names:
            building = Building(bn)
            building.zones = self.get_zones(bn)
            if len(building.zones) > 0:
                buildings.append(building)
        return buildings

    @abstractmethod
    def read_city_model(self):
        """
        Read the data strored in the 3D city model.
        :return: dictionary containing data stored in the 3D city model.
        """
        pass

    @abstractmethod
    def get_reference_system(self):
        """
        Get the reference system of the 3D city model.
        :return: the reference system
        """
        pass

    @abstractmethod
    def get_building_names(self):
        """
        :return: list of building names stored in the 3D city model.
        """
        pass

    @abstractmethod
    def get_zones(self, building_name):
        """
        Get zones of a building in the 3D city model.
        :param building_name: name of the building
        :return: list of zones of the building.
        """
        pass


class CityJSONLoader(CityModelLoader):
    """
    Class used to load a CityJSON model (https://www.cityjson.org/) as a list of buildings

    Attributes:
        city_model_filename: file containing the 3D city model
        _city_model_data: data stored in the 3D city model to be expressed as a list of buildings.
        reference_system: reference system used in the 3D city model
        lod: level of detail of the 3D city model expressed in CityJSON
    """

    def __init__(self, city_model_filename, lod):
        """
        :param city_model_filename: file containing the 3D city model.
        :param lod: level of detail of the 3D city.
        """
        CityModelLoader.__init__(self, city_model_filename)
        self.lod = lod

    def read_city_model(self):
        """
        Read the data strored in the 3D city model.
        :return: dictionary containing data stored in the 3D city model.
        """
        with open(self.city_model_filename, 'r') as f:
            data = json.load(f)
        return data

    def get_reference_system(self):
        """
        Get the reference system of the 3D city model.
        :return: the reference system
        """
        if self._city_model_data['metadata']['referenceSystem'] == 'https://www.opengis.net/def/crs/EPSG/0/7415':
            return CityModelReferenceSystem.EPSG_7415
        else:
            return CityModelReferenceSystem.UNKNOWN

    def get_building_names(self):
        """
        :return: list of building names stored in the 3D city model.
        """
        building_names = []
        for k in list(self._city_model_data['CityObjects'].keys()):
            if 'children' in list(self._city_model_data['CityObjects'][k].keys()):
                building_names.append(k)
        return building_names

    def get_zones(self, building_name):
        """
        Get zones of a building in the 3D city model.
        :param building_name: name of the building
        :param lod: level of detail of the building
        :return: list of zones of the building.
        """
        building_info = self._city_model_data['CityObjects'][building_name]
        building_geometries = self._city_model_data['CityObjects'][building_info['children'][0]]['geometry']
        city_model_vertices = self._city_model_data['vertices']
        for n in range(len(building_geometries)):
            if building_geometries[n]['lod'] == self.lod:
                building_geometry = building_geometries[n]
        building_vertices = building_geometry['boundaries']
        building_surface_semantics_values = building_geometry['semantics']['values'][0]
        decompressor = self.get_decompressor()
        xfp, yfp, zfp = self.get_footprint(building_name)
        min_x = min(xfp)
        min_y = min(yfp)
        min_z = min(zfp)
        zones = [Zone('zone:0')]
        n_roof_surfaces = 0
        roof_surfaces = []
        n_exterior_wall_surfaces = 0
        exterior_wall_surfaces = []
        ground_floor_surface = None
        for n in range(len(building_surface_semantics_values)):
            point_indexes = building_vertices[0][n][0]
            points = []
            for pindex in point_indexes:
                point = city_model_vertices[pindex]
                x, y, z = decompressor.decompress([point[0]], [point[1]], [point[2]])
                points.append([x[0] - min_x, y[0] - min_y, z[0] - min_z])
            if building_geometry['semantics']['surfaces'][building_surface_semantics_values[n]]['type'] == 'GroundSurface':
                surface = Surface('zone:0:floor:0', np.asarray(points))
                ground_floor_surface = surface
            if building_geometry['semantics']['surfaces'][building_surface_semantics_values[n]]['type'] == 'RoofSurface':
                surface = Surface('zone:0:roof:' + str(n_roof_surfaces), np.asarray(points))
                n_roof_surfaces = n_roof_surfaces + 1
                roof_surfaces.append(surface)
            if building_geometry['semantics']['surfaces'][building_surface_semantics_values[n]]['type'] == 'WallSurface':
                surface = Surface('zone:0:extwall:' + str(n_exterior_wall_surfaces), np.asarray(points))
                n_exterior_wall_surfaces = n_exterior_wall_surfaces + 1
                exterior_wall_surfaces.append(surface)
        if (ground_floor_surface is None) or (len(roof_surfaces) == 0) or (len(exterior_wall_surfaces) == 0):
            return []
        else:
            zones[0].ground_floor = ground_floor_surface
            zones[0].roofs = roof_surfaces
            zones[0].exterior_walls = exterior_wall_surfaces
            return zones

    def get_decompressor(self):
        """
        Get decompressor of xyz-coordinates
        :return: the decompressor.
        """
        transform = self._city_model_data['transform']
        return DecompressCoordinatesScaleTranslate(transform["scale"][0], transform["scale"][1], transform["scale"][2],
                                                   transform["translate"][0], transform["translate"][1], transform["translate"][2])

    def get_footprint(self, building_name):
        """
        Get the xyz-coordinates of the footprint of a building.
        :param building_name: name of the building.
        :return: the xyz-coordinates of the footprint.
        """
        building_info = self._city_model_data['CityObjects'][building_name]
        building_geometries = self._city_model_data['CityObjects'][building_info['children'][0]]['geometry']
        city_model_vertices = self._city_model_data['vertices']
        city_model_metadata = self._city_model_data['metadata']

        point_indexes = building_geometries[0]['boundaries'][0][0][0]
        building_footprint = [city_model_vertices[n] for n in point_indexes]
        building_footprint.append(city_model_vertices[point_indexes[0]])
        xs, ys, zs = zip(*[point[0:3] for point in building_footprint])
        if self.get_reference_system() == CityModelReferenceSystem.EPSG_7415:
            decompressor = self.get_decompressor()
        else:
            raise CityModelCoordinateReferenceSystemException('The coordinate reference system is unknown.')
        return decompressor.decompress(xs, ys, zs)


class GeoJSONLoader(CityModelLoader):
    """
    Class used to load a CityJSON model (https://www.cityjson.org/) as a list of buildings

    Attributes:
        city_model_filename: file containing the 3D city model
        _city_model_data: data stored in the 3D city model to be expressed as a list of buildings.
        reference_system: reference system used in the 3D city model
    """

    def __init__(self, city_model_filename):
        """
        :param city_model_filename: file containing the 3D city model.
        """
        CityModelLoader.__init__(self, city_model_filename)

    def read_city_model(self):
        """
        Read the data strored in the 3D city model.
        :return: dictionary containing data stored in the 3D city model.
        """
        with open(self.city_model_file, 'r') as f:
            data = json.load(f)
        return data

    def get_reference_system(self):
        """
        Get the reference system of the 3D city model.
        :return: the reference system
        """
        if self._city_model_data['crs']['properties']['name'] == 'urn:ogc:def:crs:OGC:1.3:CRS84':
            return CityModelReferenceSystem.CRS84
        else:
            return CityModelReferenceSystem.UNKNOWN

    def get_building_names(self):
        """
        :return: list of building names stored in the 3D city model.
        """
        #TODO: Implementation
        pass

    def get_zones(self, building_name):
        """
        Get zones of a building in the 3D city model.
        :param building_name: name of the building
        :return: list of zones of the building.
        """
        buildings_data = self._city_model_data['features']
        building_height = 0.0
        building_footprint = None
        for n in range(len(buildings_data)):
            if building_name == str(buildings_data[n]['properties']['OBJECTID']):
                building_height = buildings_data[n]['properties']['Height']
                building_footprint = buildings_data[n]['geometry']['coordinates']
                break
        coordinates = np.array(building_footprint[0][0])
        lat = coordinates[:, 1]
        lon = coordinates[:, 0]
        transformer = None
        if self.get_reference_system() == CityModelReferenceSystem.CRS84:
            transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857")
        else:
            raise CityModelCoordinateReferenceSystemException('The coordinate reference system is unknown.')
        x, y = transformer.transform(lat, lon)
        x = x - min(x)
        y = y - min(y)
        zones = [Zone('zone:0')]
        roof_surface = Surface('zone:0:roof:0')
        exterior_wall_surfaces = []
        ground_floor_surface = Surface('zone:0:floor:0')
        N = len(x)
        for n in range(N - 1):
            exterior_wall_surface = Surface('zone:0:extwall:' + str(n))
            ground_floor_surface.points.append([x[n], y[n], 0.0])
            roof_surface.points.append([x[N - 1 - n], y[N - 1 - n], building_height])
            exterior_wall_surface.points.append([x[n], y[n], 0.0])
            exterior_wall_surface.points.append([x[n + 1], y[n + 1], 0.0])
            exterior_wall_surface.points.append([x[n + 1], y[n + 1], building_height])
            exterior_wall_surface.points.append([x[n], y[n], building_height])
            exterior_wall_surfaces.append(exterior_wall_surface)
        zones[0].ground_floor_surface = ground_floor_surface
        zones[0].roof_surfaces = [roof_surface]
        zones[0].exterior_wall_surfaces = exterior_wall_surfaces
        return zones

class BuildingEnergyModelGeneratorHandler():
    """
    Class used to handle the generation of a building energy model from building information and a template.

    Attributes:
        next: next handler of the generation of the building energy model.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.next = None

    def set_next_handler(self, next):
        """
        Set next handler for generating a building energy model.
        """
        self.next = next

    @abstractmethod
    def handle(self, template, building, output_dir):
        """
        Handle the generation of a building energy model.
        :param template: file containing the template of the building energy model.
        :param building: building object containing information of the resulting building energy model.
        :param output_dir: directory in which the building energy model must be saved.
        """
        pass

class BuildingEnergyModelGenerator():
    """
    Class used to generate building energy models from a template file.

    Attributes:
        buildings: list if buildings to be expressed as building energy models.
        template: file containing the template for generating building energy models.
        output_dir: directory in which building energy models must be saved.
        first_handler: first handler for generating building energy models.
    """

    __metaclass__ = ABCMeta

    def __init__(self, buildings, template, output_dir="."):
        """
        :param buildings: list if buildings to be expressed as building energy models.
        :param template: file containing the template for generating building energy models.
        :param output_dir: directory in which building energy models must be saved.
        """
        self.buildings = buildings
        self.template = template
        self.output_dir = output_dir
        self.first_handler = None

    def generate(self):
        """
        Generate the list of building energy models from the template.
        """
        for b in self.buildings:
            self.first_handler.handle(self.template, b, self.output_dir)

class EnergyPlusGeneratorHandler(BuildingEnergyModelGeneratorHandler):
    """
    Class used to handle the generation of an EnergyPlus model from building information and a template.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        BuildingEnergyModelGeneratorHandler.__init__(self)
        self.idf = None

    def handle(self, template, building, output_dir):
        """
        Handle the generation of a building energy model.
        :param template: file containing the template of the building energy model.
        :param output_dir: directory in which building energy models must be saved.
        :param building: building object containing information of the resulting building energy model.
        """
        if self.idf is None:
            IDF.setiddname(os.path.join(os.environ['ENERGYPLUS'], 'Energy+.idd'))
            self.idf = IDF(template)
        self.add_idf_objects(building)
        if self.next is not None:
            self.next.idf = self.idf
            self.next.handle(template, building, output_dir)
        else:
            print('--> Generated building: ' + building.name)
            self.idf.saveas(os.path.join(output_dir, building.name + '.idf'))

    @abstractmethod
    def add_idf_objects(self, building):
        """
        Add corresponding objects in the IDF.
        :param building: building corresponding to the BEM to be created.
        """
        pass

class EnergyPlusGeneratorHandlerBuilding(EnergyPlusGeneratorHandler):
    """
    Class used to generate building of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """

    def __init__(self):
        """
        :param output_dir: directory in which building energy models must be saved.
        """
        EnergyPlusGeneratorHandler.__init__(self)

    def add_idf_objects(self, building):
        """
        Add corresponding objects in the IDF.
        :param building: building corresponding to the BEM to be created.
        """
        idf_buildings = self.idf.idfobjects["BUILDING"]
        self.idf.newidfobject("BUILDING")
        idf_buildings[-1].Name = building.name


class EnergyPlusGeneratorHandlerZones(EnergyPlusGeneratorHandler):
    """
    Class used to generate zones of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """

    def __init__(self):
        """
        :param output_dir: directory in which building energy models must be saved.
        """
        EnergyPlusGeneratorHandler.__init__(self)

    def add_idf_objects(self, building):
        """
        Add corresponding objects in the IDF.
        :param building: building corresponding to the BEM to be created.
        """
        idf_zones = self.idf.idfobjects["ZONE"]
        for z in building.zones:
            self.idf.newidfobject("ZONE")
            idf_zones[-1].Name = z.name
            idf_zones[-1].Floor_Area = round(z.get_area().m, 3)
            idf_zones[-1].Volume = round(z.get_volume().m, 3)

class EnergyPlusGeneratorHandlerSurfaces(EnergyPlusGeneratorHandler):
    """
    Class used to generate surfaces of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        EnergyPlusGeneratorHandler.__init__(self)

    def add_idf_objects(self, building):
        """
        Add corresponding objects in the IDF.
        :param building: building corresponding to the BEM to be created.
        """
        idf_surfaces = self.idf.idfobjects["BUILDINGSURFACE:DETAILED"]
        for z in building.zones:
            surfaces = self.get_surfaces(z)
            for s in surfaces:
                self.idf.newidfobject("BUILDINGSURFACE:DETAILED")
                idf_surfaces[-1].Name = s.name
                idf_surfaces[-1].Surface_Type = self.get_surface_type()
                idf_surfaces[-1].Construction_Name = self.get_construction_name()
                idf_surfaces[-1].Zone_Name = z.name
                idf_surfaces[-1].Outside_Boundary_Condition = self.get_outside_boundary_condition()
                idf_surfaces[-1].Outside_Boundary_Condition_Object = self.get_outside_boundary_condition_object()
                idf_surfaces[-1].Sun_Exposure = 'SunExposed' if self.is_sun_exposed() else 'NoSun'
                idf_surfaces[-1].Wind_Exposure = 'WindExposed' if self.is_wind_exposed() else 'NoWind'
                idf_surfaces[-1].View_Factor_to_Ground = 'autocalculate'
                idf_surfaces[-1].Number_of_Vertices = str(s.points.shape[0])
                point_id = 1
                for p in s.points:
                    idf_surfaces[-1]["Vertex_" + str(point_id) + "_Xcoordinate"] = str(p[0])
                    idf_surfaces[-1]["Vertex_" + str(point_id) + "_Ycoordinate"] = str(p[1])
                    idf_surfaces[-1]["Vertex_" + str(point_id) + "_Zcoordinate"] = str(p[2])
                    point_id += 1

    @abstractmethod
    def get_surfaces(self, zone):
        """
        :return: surfaces containing information to be added to the IDF.
        """
        pass

    @abstractmethod
    def get_surface_type(self):
        """
        :return: surface type to be added to the IDF
        """
        pass

    @abstractmethod
    def get_construction_name(self):
        """
        :return: construction name to be added to the IDF
        """
        pass

    @abstractmethod
    def get_outside_boundary_condition(self):
        """
        :return: outside boundary condition to be added to the IDF.
        """
        pass

    @abstractmethod
    def get_outside_boundary_condition_object(self):
        """
        :return: outside boundary condition object to be added to the IDF.
        """
        pass

    @abstractmethod
    def is_sun_exposed(self):
        """
        :return: True if sun exposed
        """
        pass

    @abstractmethod
    def is_wind_exposed(self):
        """
        :return: True if wind exposed
        """
        pass


class EnergyPlusGeneratorHandlerGroundFloor(EnergyPlusGeneratorHandlerSurfaces):
    """
    Class used to generate the ground floor of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """

    def __init__(self):
        EnergyPlusGeneratorHandlerSurfaces.__init__(self)

    def get_surfaces(self, zone):
        """
        :return: surfaces containing information to be added to the IDF.
        """
        if not zone.ground_floor is None:
            return [zone.ground_floor]
        else:
            return []

    def get_surface_type(self):
        """
        :return: surface type to be added to the IDF
        """
        return 'Floor'

    def get_construction_name(self):
        """
        :return: construction name to be added to the IDF
        """
        return 'GROUND FLOOR'

    def get_outside_boundary_condition(self):
        """
        :return: outside boundary condition to be added to the IDF.
        """
        return 'Ground'

    def get_outside_boundary_condition_object(self):
        """
        :return: outside boundary condition object to be added to the IDF.
        """
        return ''

    def is_sun_exposed(self):
        """
        :return: True if sun exposed
        """
        return False

    def is_wind_exposed(self):
        """
        :return: True if wind exposed
        """
        return False

class EnergyPlusGeneratorHandlerExteriorWalls(EnergyPlusGeneratorHandlerSurfaces):
    """
    Class used to generate exterior walls of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """

    def __init__(self):
        EnergyPlusGeneratorHandlerSurfaces.__init__(self)

    def get_surfaces(self, zone):
        """
        :return: surfaces containing information to be added to the IDF.
        """
        if len(zone.exterior_walls) > 0:
            return zone.exterior_walls
        else:
            return []

    def get_surface_type(self):
        """
        :return: surface type to be added to the IDF
        """
        return 'Wall'

    def get_construction_name(self):
        """
        :return: construction name to be added to the IDF
        """
        return 'EXTERIOR WALL'

    def get_outside_boundary_condition(self):
        """
        :return: outside boundary condition to be added to the IDF.
        """
        return 'Outdoors'

    def get_outside_boundary_condition_object(self):
        """
        :return: outside boundary condition object to be added to the IDF.
        """
        return ''

    def is_sun_exposed(self):
        """
        :return: True if sun exposed
        """
        return True

    def is_wind_exposed(self):
        """
        :return: True if wind exposed
        """
        return True

class EnergyPlusGeneratorHandlerRoofs(EnergyPlusGeneratorHandlerSurfaces):
    """
    Class used to generate roofs of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """

    def __init__(self):
        EnergyPlusGeneratorHandlerSurfaces.__init__(self)

    def get_surfaces(self, zone):
        """
        :return: surfaces containing information to be added to the IDF.
        """
        if len(zone.roofs) > 0:
            return zone.roofs
        else:
            return []

    def get_surface_type(self):
        """
        :return: surface type to be added to the IDF
        """
        return 'Roof'

    def get_construction_name(self):
        """
        :return: construction name to be added to the IDF
        """
        return 'ROOF'

    def get_outside_boundary_condition(self):
        """
        :return: outside boundary condition to be added to the IDF.
        """
        return 'Outdoors'

    def get_outside_boundary_condition_object(self):
        """
        :return: outside boundary condition object to be added to the IDF.
        """
        return ''

    def is_sun_exposed(self):
        """
        :return: True if sun exposed
        """
        return True

    def is_wind_exposed(self):
        """
        :return: True if wind exposed
        """
        return True

class EnergyPlusGeneratorHandlerOutputVariables(EnergyPlusGeneratorHandler):
    """
    Class used to generate output variables of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        EnergyPlusGeneratorHandler.__init__(self)

    def add_idf_objects(self, building):
        """
        Add corresponding objects in the IDF.
        :param building: building corresponding to the BEM to be created.
        """
        idf_output_variables = self.idf.idfobjects["OUTPUT:VARIABLE"]
        self.idf.newidfobject("OUTPUT:VARIABLE")
        idf_output_variables[-1].Key_Value = '*'
        idf_output_variables[-1].Variable_Name = self.get_variable_name()
        idf_output_variables[-1].Reporting_Frequency = 'Timestep'

    @abstractmethod
    def get_variable_name(self):
        """
        :return: the name of the output variable.
        """
        pass

class EnergyPlusGeneratorHandlerIdealSensibleHeatingLoad(EnergyPlusGeneratorHandlerOutputVariables):
    """
    Class used to generate the ideal sensible heating load of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        EnergyPlusGeneratorHandlerOutputVariables.__init__(self)

    def get_variable_name(self):
        """
        :return: the name of the output variable.
        """
        return 'Zone Ideal Loads Zone Sensible Heating Rate'

class EnergyPlusGeneratorHandlerIdealLatentHeatingLoad(EnergyPlusGeneratorHandlerOutputVariables):
    """
    Class used to generate the ideal latent heating load of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        EnergyPlusGeneratorHandlerOutputVariables.__init__(self)

    def get_variable_name(self):
        """
        :return: the name of the output variable.
        """
        return 'Zone Ideal Loads Zone Latent Heating Rate'

class EnergyPlusGeneratorHandlerIdealSensibleCoolingLoad(EnergyPlusGeneratorHandlerOutputVariables):
    """
    Class used to generate the ideal sensible cooling load of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        EnergyPlusGeneratorHandlerOutputVariables.__init__(self)

    def get_variable_name(self):
        """
        :return: the name of the output variable.
        """
        return 'Zone Ideal Loads Zone Sensible Cooling Rate'

class EnergyPlusGeneratorHandlerIdealLatentCoolingLoad(EnergyPlusGeneratorHandlerOutputVariables):
    """
    Class used to generate the ideal latent cooling load of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        EnergyPlusGeneratorHandlerOutputVariables.__init__(self)

    def get_variable_name(self):
        """
        :return: the name of the output variable.
        """
        return 'Zone Ideal Loads Zone Latent Cooling Rate'

class EnergyPlusGeneratorHandlerExteriorSurfaceTemperature(EnergyPlusGeneratorHandlerOutputVariables):
    """
    Class used to generate the exterior surface temperature of an EnergyPlus model.

    Attributes:
        next: next handler of the generation of the building energy model.
        idf: object containing information of the EnergyPlus model
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        EnergyPlusGeneratorHandlerOutputVariables.__init__(self)

    def get_variable_name(self):
        """
        :return: the name of the output variable.
        """
        return 'Surface Outside Face Temperature'


class EnergyPlusGenerator(BuildingEnergyModelGenerator):
    """
    Class used to generate EnergyPlus models from a template file.

    Attributes:
        buildings: list if buildings to be expressed as building energy models.
        template: file containing the template for generating building energy models.
        first_handler: first handler for generating building energy models.
    """

    def __init__(self, buildings, template, output_dir="."):
        """
        :param buildings: list if buildings to be expressed as building energy models.
        :param template: file containing the template for generating building energy models.
        :param output_dir: directory in which building energy models must be saved.
        """
        BuildingEnergyModelGenerator.__init__(self, buildings, template, output_dir)
        handler_building = EnergyPlusGeneratorHandlerBuilding()
        handler_zones = EnergyPlusGeneratorHandlerZones()
        handler_ground_floor = EnergyPlusGeneratorHandlerGroundFloor()
        handler_exterior_walls = EnergyPlusGeneratorHandlerExteriorWalls()
        handler_roofs = EnergyPlusGeneratorHandlerRoofs()
        handler_sensible_heating_load = EnergyPlusGeneratorHandlerIdealSensibleHeatingLoad()
        handler_latent_heating_load = EnergyPlusGeneratorHandlerIdealLatentHeatingLoad()
        handler_sensible_cooling_load = EnergyPlusGeneratorHandlerIdealSensibleCoolingLoad()
        handler_latent_cooling_load = EnergyPlusGeneratorHandlerIdealLatentCoolingLoad()
        handler_exterior_surface_temperature = EnergyPlusGeneratorHandlerExteriorSurfaceTemperature()

        handler_building.set_next_handler(handler_zones)
        handler_zones.set_next_handler(handler_ground_floor)
        handler_ground_floor.set_next_handler(handler_exterior_walls)
        handler_exterior_walls.set_next_handler(handler_roofs)
        handler_roofs.set_next_handler(handler_sensible_heating_load)
        handler_sensible_heating_load.set_next_handler(handler_latent_heating_load)
        handler_latent_heating_load.set_next_handler(handler_sensible_cooling_load)
        handler_sensible_cooling_load.set_next_handler(handler_latent_cooling_load)
        handler_latent_cooling_load.set_next_handler(handler_exterior_surface_temperature)

        self.first_handler = handler_building

def generate_building_energy_models(city_model_file, building_energy_model_template,
                                    city_model_format = 'cityjson', lod = '1.2', building_energy_model_format = 'eplus',
                                    output_dir = "."):
    """
    Generate a list of building energy models from a 3D city model
    :param city_model_file: file containing the 3D city model.
    :param building_energy_model_template: template file used to generate building energy models.
    :param city_model_format: format with which the 3D city model is expressed (e.g. CityJSON or GeoJSON).
    :param lod: level of detail with which building energy models should be generated (if achievable by the 3D city model).
    :param building_energy_model_format: format with which the building energy model should be generated (e.g. EnergyPlus)
    :param output_dir: directory in which building energy models must be saved.
    """
    buildings = []
    if city_model_format == 'cityjson':
        buildings = CityJSONLoader(city_model_file, lod).load()
    elif city_model_format == 'geojson':
        buildings = GeoJSONLoader(city_model_file).load()
    if building_energy_model_format == 'eplus':
        EnergyPlusGenerator(buildings, building_energy_model_template, output_dir).generate()













