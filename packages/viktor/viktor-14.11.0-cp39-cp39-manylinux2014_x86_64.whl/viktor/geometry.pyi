import abc
import numpy as np
import trimesh
import uuid
from .core import Color as Color, File as File, ISCLOSE_ATOL as ISCLOSE_ATOL, ISCLOSE_RTOL as ISCLOSE_RTOL
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Any, Iterator, List, Optional, Sequence, TextIO, Tuple, TypeVar, Union

trimesh_logger: Incomplete
logger: Incomplete
T = TypeVar('T')

class Vector:
    x: Incomplete
    y: Incomplete
    z: Incomplete
    def __init__(self, x: float, y: float, z: float = ...) -> None: ...
    def __getitem__(self, index: int) -> float: ...
    def __iter__(self) -> Iterator[float]: ...
    def __eq__(self, other: object) -> bool: ...
    def __neg__(self) -> Vector: ...
    def __add__(self, other: Vector) -> Vector: ...
    def __sub__(self, other: Vector) -> Vector: ...
    def __mul__(self, other: float) -> Vector: ...
    def __rmul__(self, other: float) -> Vector: ...
    @property
    def squared_magnitude(self) -> float: ...
    @property
    def magnitude(self) -> float: ...
    @property
    def coordinates(self) -> Tuple[float, float, float]: ...
    def normalize(self) -> Vector: ...
    def dot(self, other: Vector) -> float: ...
    def cross(self, other: Vector) -> Vector: ...

class _GLTF:
    @staticmethod
    def add_geometry_to_scene(scene: trimesh.Scene, geometry: trimesh.parent.Geometry3D, *, transform: np.ndarray = ..., **metadata: Any) -> str: ...
    @classmethod
    def to_gltf(cls, *objects: TransformableObject) -> File: ...

class Material:
    uuid: Incomplete
    name: Incomplete
    density: Incomplete
    price: Incomplete
    color: Incomplete
    roughness: Incomplete
    metalness: Incomplete
    opacity: Incomplete
    def __init__(self, name: str = ..., density: float = ..., price: float = ..., *, threejs_type: str = ..., roughness: float = ..., metalness: float = ..., opacity: float = ..., color: Color = ...) -> None: ...

class TransformableObject(ABC, metaclass=abc.ABCMeta):
    def __init__(self, *, identifier: str = ...) -> None: ...
    def translate(self, translation_vector: Union[Vector, Tuple[float, float, float]]) -> TransformableObject: ...
    def rotate(self, angle: float, direction: Union[Vector, Tuple[float, float, float]], point: Union['Point', Tuple[float, float, float]] = ...) -> TransformableObject: ...
    def mirror(self, point: Union['Point', Tuple[float, float, float]], normal: Union[Vector, Tuple[float, float, float]]) -> TransformableObject: ...
    def scale(self, scaling_vector: Union[Vector, Tuple[float, float, float]]) -> TransformableObject: ...

class Group(TransformableObject):
    def __init__(self, objects: Sequence[TransformableObject], *, identifier: str = ...) -> None: ...
    def add(self, objects: Union[list, tuple, TransformableObject]) -> None: ...
    @property
    def children(self) -> List[TransformableObject]: ...
    def duplicate(self) -> Group: ...

class Point:
    def __init__(self, x: float, y: float, z: float = ...) -> None: ...
    def __getitem__(self, index: int) -> float: ...
    def __iter__(self) -> Iterator[float]: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float: ...
    @property
    def coordinates(self) -> np.ndarray: ...
    def copy(self) -> Point: ...
    def coincides_with(self, other: Point) -> bool: ...
    def vector_to(self, point: Union['Point', Tuple[float, float, float]]) -> Vector: ...
    def get_local_coordinates(self, local_origin: Union['Point', Tuple[float, float, float]], spherical: bool = ...) -> np.ndarray: ...

class Line(TransformableObject):
    color: Incomplete
    def __init__(self, start_point: Union[Point, Tuple[float, float, float]], end_point: Union[Point, Tuple[float, float, float]], *, color: Color = ..., identifier: str = ...) -> None: ...
    def __getitem__(self, index: int) -> Point: ...
    def __iter__(self) -> Iterator[Point]: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def start_point(self) -> Point: ...
    @property
    def end_point(self) -> Point: ...
    @property
    def length(self) -> float: ...
    def direction(self, normalize: bool = ...) -> Vector: ...
    def collinear(self, point: Union[Point, Tuple[float, float, float]]) -> bool: ...
    def project_point(self, point: Union[Point, Tuple[float, float, float]]) -> Point: ...
    def distance_to_point(self, point: Union[Point, Tuple[float, float, float]]) -> float: ...
    @property
    def length_vector(self) -> np.ndarray: ...
    @property
    def unit_vector(self) -> np.ndarray: ...
    @property
    def geometries(self) -> Tuple[Point, Point]: ...
    @property
    def horizontal(self) -> bool: ...
    @property
    def vertical(self) -> bool: ...
    def discretize(self, num: int = ...) -> List[Point]: ...
    def revolve(self, *, material: Material = ..., identifier: str = ..., **kwargs: Any) -> LineRevolve: ...
    def get_line_function_parameters(self) -> Tuple[float, float]: ...
    def find_overlap(self, other: Line, inclusive: bool = ...) -> Optional[Union[Point, 'Line']]: ...

def calculate_intersection_bounded_line_with_y(line: Line, y_intersection: float) -> Optional[float]: ...
def calculate_intersection_extended_line_with_y(line: Line, y_intersection: float) -> float: ...
def line_is_horizontal(line: Line) -> bool: ...
def line_is_vertical(line: Line) -> bool: ...
def x_between_bounds(x: float, x1: float, x2: float, inclusive: bool = ...) -> bool: ...
def y_between_bounds(y: float, y1: float, y2: float, inclusive: bool = ...) -> bool: ...
def point_is_on_bounded_line(point: Union[Point, Tuple[float, float, float]], line: Union[Line, Tuple[Tuple[float, float, float], Tuple[float, float, float]]], inclusive: bool = ...) -> bool: ...
def calculate_intersection_extended_line_with_x(line: Line, x: float) -> Point: ...
def get_line_function_parameters(line: Line) -> Tuple[float, float]: ...
def calculate_intersection_extended_lines(extended_line1: Line, extended_line2: Line) -> Optional[Point]: ...
def calculate_intersection_bounded_line_extended_line(bounded_line: Line, extended_line: Line, inclusive: bool = ...) -> Optional[Point]: ...
def calculate_intersection_bounded_lines(bounded_line1: Line, bounded_line2: Line, inclusive: bool = ...) -> Optional[Point]: ...

class Revolve(TransformableObject, ABC, metaclass=abc.ABCMeta):
    material: Incomplete
    def __init__(self, *args: Any, rotation_angle: float = ..., material: Material = ..., identifier: str = ..., **kwargs: Any) -> None: ...
    @property
    @abstractmethod
    def surface_area(self) -> float: ...
    @property
    @abstractmethod
    def inner_volume(self) -> float: ...
    @property
    def thickness(self) -> float: ...
    @thickness.setter
    def thickness(self, thickness: float) -> None: ...
    @property
    def mass(self) -> float: ...

class LineRevolve(Revolve):
    def __init__(self, line: Line, *args: Any, material: Material = ..., identifier: str = ..., **kwargs: Any) -> None: ...
    @property
    def line(self) -> Line: ...
    @property
    def uuid(self) -> uuid.UUID: ...
    @property
    def height(self) -> float: ...
    @property
    def surface_area(self) -> float: ...
    @property
    def inner_volume(self) -> float: ...
    @property
    def geometries(self) -> Tuple[Line, ...]: ...

class Arc(TransformableObject):
    color: Incomplete
    def __init__(self, centre_point: Union[Point, Tuple[float, float, float]], start_point: Union[Point, Tuple[float, float, float]], end_point: Union[Point, Tuple[float, float, float]], short_arc: bool = ..., *, n_segments: int = ..., color: Color = ..., identifier: str = ...) -> None: ...
    @property
    def radius(self) -> float: ...
    @property
    def centre_point(self) -> Point: ...
    @property
    def start_point(self) -> Point: ...
    @property
    def end_point(self) -> Point: ...
    @property
    def n_segments(self) -> int: ...
    @property
    def theta1_theta2(self) -> Tuple[float, float]: ...
    @property
    def theta1(self) -> float: ...
    @property
    def theta2(self) -> float: ...
    @property
    def short_arc(self) -> bool: ...
    @property
    def geometries(self) -> Tuple[Point, Point, Point]: ...
    @property
    def angle(self) -> float: ...
    @property
    def length(self) -> float: ...
    def discretize(self, num: int = ...) -> List[Point]: ...
    def revolve(self, *, rotation_angle: float = ..., material: Material = ..., identifier: str = ..., **kwargs: Any) -> ArcRevolve: ...

class ArcRevolve(Revolve):
    def __init__(self, arc: Arc, *args: Any, rotation_angle: float = ..., material: Material = ..., identifier: str = ..., **kwargs: Any) -> None: ...
    @property
    def arc(self) -> Arc: ...
    @property
    def uuid(self) -> str: ...
    @property
    def surface_area(self) -> float: ...
    @property
    def inner_volume(self) -> float: ...
    @property
    def height(self) -> float: ...
    @property
    def geometries(self) -> Tuple[Arc, ...]: ...

class Triangle:
    profile: Incomplete
    vertices: Incomplete
    def __init__(self, point1: Point, point2: Point, point3: Point) -> None: ...
    def area(self) -> float: ...
    @property
    def centroid(self) -> Tuple[float, float, float]: ...
    @property
    def moment_of_inertia(self) -> Tuple[float, float]: ...

class CartesianAxes(Group):
    def __init__(self, origin: Point = ..., axis_length: float = ..., axis_diameter: float = ...) -> None: ...

class RDWGSConverter:
    X0: int
    Y0: int
    phi0: float
    lam0: float
    @staticmethod
    def from_rd_to_wgs(coords: Tuple[float, float]) -> List[float]: ...
    @staticmethod
    def from_wgs_to_rd(coords: Tuple[float, float]) -> List[float]: ...

def spherical_to_cartesian(spherical_coordinates: Tuple[float, float, float]) -> np.ndarray: ...
def cartesian_to_spherical(cartesian_coordinates: Tuple[float, float, float]) -> np.ndarray: ...
def cylindrical_to_cartesian(cylindrical_coordinates: Tuple[float, float, float]) -> np.ndarray: ...
def cartesian_to_cylindrical(cartesian_coordinates: Tuple[float, float, float]) -> np.ndarray: ...

class Extrusion(Group):
    def __init__(self, profile: List[Point], line: Line, profile_rotation: float = ..., *, material: Material = ..., identifier: str = ...) -> None: ...
    @property
    def children(self) -> None: ...
    @property
    def profile(self) -> List[Point]: ...
    @property
    def material(self) -> Material: ...
    @material.setter
    def material(self, material: Material) -> None: ...
    @property
    def line(self) -> Line: ...
    @property
    def length(self) -> float: ...
    @property
    def uuid(self) -> str: ...
    @property
    def geometries(self) -> Line: ...
    @property
    def transformation(self) -> np.ndarray: ...

class ArcExtrusion(Group):
    def __init__(self, profile: List[Point], arc: Arc, profile_rotation: float = ..., n_segments: int = ..., *, material: Material = ..., identifier: str = ...) -> None: ...
    @property
    def children(self) -> None: ...

class CircularExtrusion(TransformableObject):
    material: Incomplete
    def __init__(self, diameter: float, line: Line, *, shell_thickness: float = ..., material: Material = ..., identifier: str = ...) -> None: ...
    @property
    def line(self) -> Line: ...
    @property
    def length(self) -> float: ...
    @property
    def diameter(self) -> float: ...
    @property
    def radius(self) -> float: ...
    @property
    def shell_thickness(self) -> Optional[float]: ...
    @property
    def cross_sectional_area(self) -> float: ...

class RectangularExtrusion(Extrusion):
    def __init__(self, width: float, height: float, line: Line, profile_rotation: float = ..., *, material: Material = ..., identifier: str = ...) -> None: ...
    @property
    def width(self) -> float: ...
    @property
    def height(self) -> float: ...
    @property
    def cross_sectional_area(self) -> float: ...
    @property
    def inner_volume(self) -> float: ...

class SquareBeam(RectangularExtrusion):
    def __init__(self, length_x: float, length_y: float, length_z: float, *, material: Material = ..., identifier: str = ...) -> None: ...

def points_are_coplanar(points: Sequence[Union[Point, Tuple[float, float, float]]]) -> bool: ...
def lines_in_same_plane(line1: Line, line2: Line) -> bool: ...
def calculate_distance_vector(start_point: Point, end_point: Point) -> np.ndarray: ...
def convert_points_for_lathe(points: Sequence[Point]) -> List[dict]: ...
def translation_matrix(direction: Union[Vector, Tuple[float, float, float]]) -> np.ndarray: ...
def scaling_matrix(scaling_vector: Union[Vector, Tuple[float, float, float]]) -> np.ndarray: ...
def rotation_matrix(angle: float, direction: Union[Vector, Tuple[float, float, float]], point: Union[Point, Tuple[float, float, float]] = ...) -> np.ndarray: ...
def reflection_matrix(point: Union[Point, Tuple[float, float, float]], normal: Union[Vector, Tuple[float, float, float]]) -> np.ndarray: ...
def unit_vector(data: Any, axis: int = ..., out: Any = ...) -> Optional[np.ndarray]: ...
def mirror_object(obj: TransformableObject, point: Point, normal: Union[Vector, Tuple[float, float, float]]) -> TransformableObject: ...
def volume_cone(r: float, h: float) -> float: ...
def surface_cone_without_base(r: float, h: float) -> float: ...
def surface_area_dome(theta1: float, theta2: float, r: float, R: float) -> float: ...
def circumference_is_clockwise(circumference: List[Point]) -> bool: ...
def add_point(unique_points: List[Point], point: Point) -> Tuple[List[Point], int]: ...
def get_vertices_faces(triangles: List[Triangle]) -> Tuple[list, list]: ...
def find_overlap(region_a: Tuple[float, float], region_b: Tuple[float, float], inclusive: bool = ...) -> Union[None, Tuple[float, float]]: ...

class Pattern(Group):
    base_object: Incomplete
    def __init__(self, base_object: TransformableObject, duplicate_translation_list: List[List[float]], *, identifier: str = ...) -> None: ...

class LinearPattern(Pattern):
    def __init__(self, base_object: TransformableObject, direction: List[float], number_of_elements: int, spacing: float, *, identifier: str = ...) -> None: ...

class BidirectionalPattern(Pattern):
    def __init__(self, base_object: TransformableObject, direction_1: List[float], direction_2: List[float], number_of_elements_1: int, number_of_elements_2: int, spacing_1: float, spacing_2: float, *, identifier: str = ...) -> None: ...

class Polygon(TransformableObject):
    points: Incomplete
    material: Incomplete
    def __init__(self, points: List[Point], *, surface_orientation: bool = ..., material: Material = ..., skip_duplicate_vertices_check: bool = ..., identifier: str = ...) -> None: ...
    def has_clockwise_circumference(self) -> bool: ...
    @property
    def cross_sectional_area(self) -> float: ...
    @property
    def centroid(self) -> Tuple[float, float]: ...
    @property
    def moment_of_inertia(self) -> Tuple[float, float]: ...
    def extrude(self, line: Line, *, profile_rotation: float = ..., material: Material = ..., identifier: str = ...) -> Extrusion: ...

class Polyline(TransformableObject):
    color: Incomplete
    def __init__(self, points: List[Point], *, color: Color = ..., identifier: str = ...) -> None: ...
    @property
    def points(self) -> List[Point]: ...
    @classmethod
    def from_lines(cls, lines: Sequence[Line]) -> Polyline: ...
    def is_equal_to(self, other: Polyline) -> bool: ...
    @property
    def start_point(self) -> Point: ...
    @property
    def end_point(self) -> Point: ...
    @property
    def lines(self) -> List[Line]: ...
    @property
    def x_min(self) -> Optional[float]: ...
    @property
    def x_max(self) -> Optional[float]: ...
    @property
    def y_min(self) -> Optional[float]: ...
    @property
    def y_max(self) -> Optional[float]: ...
    @property
    def z_min(self) -> Optional[float]: ...
    @property
    def z_max(self) -> Optional[float]: ...
    def get_reversed_polyline(self) -> Polyline: ...
    def serialize(self) -> List[dict]: ...
    def filter_duplicate_points(self) -> Polyline: ...
    def is_monotonic_ascending_x(self, strict: bool = ...) -> bool: ...
    def is_monotonic_ascending_y(self, strict: bool = ...) -> bool: ...
    def intersections_with_polyline(self, other_polyline: Polyline) -> List[Point]: ...
    def intersections_with_x_location(self, x: float) -> List[Point]: ...
    def point_is_on_polyline(self, point: Point) -> bool: ...
    def get_polyline_between(self, start_point: Point, end_point: Point, inclusive: bool = ...) -> Polyline: ...
    def find_overlaps(self, other: Polyline) -> List['Polyline']: ...
    def combine_with(self, other: Polyline) -> Polyline: ...
    def split(self, point: Point) -> Tuple['Polyline', 'Polyline']: ...
    @classmethod
    def get_lowest_or_highest_profile_x(cls, profile_1: Polyline, profile_2: Polyline, lowest: bool) -> Polyline: ...

class Cone(TransformableObject):
    material: Incomplete
    def __init__(self, diameter: float, height: float, *, origin: Point = ..., orientation: Vector = ..., material: Material = ..., identifier: str = ...) -> None: ...
    @classmethod
    def from_line(cls, diameter: float, line: Line, *, material: Material = ..., identifier: str = ...) -> Cone: ...

class Sphere(TransformableObject):
    centre_point: Incomplete
    radius: Incomplete
    width_segments: Incomplete
    height_segments: Incomplete
    material: Incomplete
    def __init__(self, centre_point: Point, radius: float, width_segments: float = ..., height_segments: float = ..., material: Material = ..., *, identifier: str = ...) -> None: ...
    def diameter(self) -> float: ...
    def circumference(self) -> float: ...
    def surface_area(self) -> float: ...
    def volume(self) -> float: ...

class Torus(Group):
    def __init__(self, radius_cross_section: float, radius_rotation_axis: float, rotation_angle: float = ..., *, material: Material = ..., identifier: str = ...) -> None: ...
    @property
    def children(self) -> None: ...
    @property
    def inner_volume(self) -> float: ...
    @property
    def material(self) -> Material: ...
    @material.setter
    def material(self, value: Material) -> None: ...

class TriangleAssembly(TransformableObject):
    material: Incomplete
    def __init__(self, triangles: List[Triangle], *, material: Material = ..., skip_duplicate_vertices_check: bool = ..., identifier: str = ...) -> None: ...

class GeoPoint:
    lat: Incomplete
    lon: Incomplete
    def __init__(self, lat: float, lon: float) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @classmethod
    def from_rd(cls, coords: Tuple[float, float]) -> GeoPoint: ...
    @property
    def rd(self) -> Tuple[float, float]: ...

class GeoPolyline:
    def __init__(self, *points: GeoPoint) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def points(self) -> List['GeoPoint']: ...

class GeoPolygon:
    def __init__(self, *points: GeoPoint) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def points(self) -> List['GeoPoint']: ...

class _Mesh(TransformableObject):
    material: Incomplete
    def __init__(self, vertices: List[List[float]], faces: List[List[int]], material: Material = ..., *, identifier: str = ...) -> None: ...
    @classmethod
    def from_obj(cls, file: TextIO, material: Material = ..., *, identifier: str = ...) -> _Mesh: ...

class _MeshAssembly(Group):
    def __init__(self, meshes: List[_Mesh], *, identifier: str = ...) -> None: ...
    @classmethod
    def from_obj(cls, file: TextIO, material_library: TextIO = ..., default_material: Material = ..., *, identifier: str = ...) -> _MeshAssembly: ...
