import abc
import os
import pandas as pd
import matplotlib.pyplot as plt
from .core import Color as Color, File as File, ISCLOSE_ATOL as ISCLOSE_ATOL, ISCLOSE_RTOL as ISCLOSE_RTOL
from .errors import GEFClassificationError as GEFClassificationError, GEFParsingError as GEFParsingError
from .geometry import CircularExtrusion as CircularExtrusion, Group as Group, Line as Line, Material as Material, Point as Point, Polygon as Polygon, Polyline as Polyline, TransformableObject as TransformableObject
from .views import Label as Label
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from io import BytesIO, StringIO
from munch import Munch as Munch
from typing import Dict, List, Tuple, Union

GEFParsingException = GEFParsingError

class _ClassificationMethod(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_method_params(self) -> dict: ...

class RobertsonMethod(_ClassificationMethod):
    soil_properties: Incomplete
    def __init__(self, soil_properties: List[dict]) -> None: ...
    def get_method_params(self) -> dict: ...

class TableMethod(_ClassificationMethod):
    qualification_table: Incomplete
    ground_water_level: Incomplete
    def __init__(self, qualification_table: List[dict], ground_water_level: float) -> None: ...
    def get_qualification_table_plot(self, fileformat: str) -> Union[BytesIO, StringIO]: ...
    def get_method_params(self) -> dict: ...

class NormalizedSoilBehaviourTypeIndexMethod(_ClassificationMethod):
    ic_table: Incomplete
    ground_water_level: Incomplete
    specific_weight_soil: Incomplete
    resolution: Incomplete
    def __init__(self, ic_table: List[dict], ground_water_level: float, specific_weight_soil: float, resolution: float = ...) -> None: ...
    def get_method_params(self) -> dict: ...

class _QualificationTablePlot:
    filename: Incomplete
    qualification_table: Incomplete
    def __init__(self, filename: str, qualification_table: list) -> None: ...
    @property
    def body(self) -> bytes: ...

class GEFData:
    classification_data: Incomplete
    name: Incomplete
    Rf: Incomplete
    qc: Incomplete
    elevation: Incomplete
    num_of_measurements: Incomplete
    max_measurement_depth_wrt_reference: Incomplete
    ground_level_wrt_reference: Incomplete
    height_system: Incomplete
    def __init__(self, gef_dict: Union[dict, Munch]) -> None: ...
    def classify(self, method: _ClassificationMethod, return_soil_layout_obj: bool = ...) -> Union[dict, 'SoilLayout']: ...
    def serialize(self) -> Union[dict, Munch]: ...
    def get_cone_visualization(self, axes: plt.Axes) -> None: ...
    def get_resistance_visualization(self, axes: plt.Axes) -> None: ...
    def get_plotted_denotation_large_qc_values(self, axes: plt.Axes, x_loc_text: float) -> None: ...

class GEFFile:
    file_content: Incomplete
    def __init__(self, file_content: str) -> None: ...
    @classmethod
    def from_file(cls, file_path: Union[str, bytes, os.PathLike], encoding: str = ...) -> GEFFile: ...
    def parse(self, additional_columns: List[str] = ..., verbose: bool = ..., return_gef_data_obj: bool = ...) -> Union[dict, GEFData]: ...

def gef_visualization(gef_data: GEFData, soil_layout_original: SoilLayout, soil_layout_user: SoilLayout, *, as_file: bool = ...) -> Union[str, File]: ...

class Soil:
    name: Incomplete
    properties: Incomplete
    def __init__(self, name: str, color: Color, properties: Union[dict, Munch] = ...) -> None: ...
    @classmethod
    def from_dict(cls, d: Union[dict, Munch]) -> Soil: ...
    def __eq__(self, other) -> bool: ...
    @property
    def color(self) -> Color: ...
    def update_properties(self, properties: Union[dict, Munch]) -> None: ...
    def serialize(self) -> dict: ...

class UndefinedSoil(Soil):
    def __init__(self) -> None: ...

class PiezoLine(Polyline):
    phreatic: Incomplete
    def __init__(self, points: List[Point], phreatic: bool = ...) -> None: ...
    def serialize(self) -> dict: ...
    @classmethod
    def from_dict(cls, piezo_line_dict: Union[dict, Munch]) -> PiezoLine: ...
    @classmethod
    def from_lines(cls, lines: List[Union[Line, Polyline]], phreatic: bool = ...) -> PiezoLine: ...

class SoilLayer:
    soil: Incomplete
    top_of_layer: Incomplete
    bottom_of_layer: Incomplete
    properties: Incomplete
    def __init__(self, soil: Soil, top_of_layer: float, bottom_of_layer: float, properties: Union[dict, Munch] = ...) -> None: ...
    @classmethod
    def from_dict(cls, soil_layer_dict: Union[dict, Munch]) -> SoilLayer: ...
    @property
    def thickness(self) -> float: ...
    def serialize(self) -> dict: ...
    def update_soil_properties(self, properties: Union[dict, Munch]) -> None: ...
    def update_properties(self, properties: Union[dict, Munch]) -> None: ...

class SoilLayer2D:
    soil: Incomplete
    top_profile: Incomplete
    bottom_profile: Incomplete
    piezo_line_top: Incomplete
    piezo_line_bottom: Incomplete
    properties: Incomplete
    def __init__(self, soil: Soil, top_profile: Polyline, bottom_profile: Polyline, properties: Union[dict, Munch] = ..., piezo_line_top: PiezoLine = ..., piezo_line_bottom: PiezoLine = ...) -> None: ...
    def serialize(self) -> dict: ...
    @classmethod
    def from_dict(cls, soil_layer_dict: Union[dict, Munch]) -> SoilLayer2D: ...
    @property
    def left_boundary(self) -> float: ...
    @property
    def right_boundary(self) -> float: ...
    def update_soil_properties(self, properties: Union[dict, Munch]) -> None: ...
    def update_properties(self, properties: Union[dict, Munch]) -> None: ...
    def polygons(self) -> List[Polygon]: ...
    def visualize_geometry(self, visualize_border: bool = ..., opacity: float = ..., material: Material = ...) -> Tuple[Group, List[Label]]: ...
    def height_at_x(self, x: float) -> float: ...
    def top_y_coordinate(self, x: float) -> float: ...
    def bottom_y_coordinate(self, x: float) -> float: ...

class SoilLayout:
    layers: Incomplete
    def __init__(self, soil_layers: List[SoilLayer]) -> None: ...
    @classmethod
    def from_dict(cls, soil_layout_dict: Union[Dict[str, List], Munch]) -> SoilLayout: ...
    def update_soil_properties(self, df: pd.DataFrame) -> None: ...
    def serialize(self) -> dict: ...
    def get_visualization(self, axes: plt.Axes) -> None: ...
    @property
    def top(self) -> float: ...
    @property
    def bottom(self) -> float: ...
    @property
    def number_of_layers(self) -> int: ...
    def update_layers(self) -> None: ...
    def append(self, layer: SoilLayer) -> None: ...
    def filter_layers_on_thickness(self, min_layer_thickness: float, merge_adjacent_same_soil_layers: bool = ...) -> SoilLayout: ...
    def filter_unique_soils(self) -> List[Soil]: ...

class PositionalSoilLayout(SoilLayout):
    x: Incomplete
    def __init__(self, x: float, soil_layers: List[SoilLayer]) -> None: ...
    @classmethod
    def from_dict(cls, positional_soil_layout_dict: Union[dict, Munch]) -> PositionalSoilLayout: ...
    def serialize(self) -> dict: ...

class SoilLayout2D:
    left_boundary: Incomplete
    right_boundary: Incomplete
    piezo_lines: Incomplete
    layers: Incomplete
    def __init__(self, soil_layers: List[SoilLayer2D], piezo_lines: List[PiezoLine] = ...) -> None: ...
    @classmethod
    def from_positional_soil_layouts(cls, positional_soil_layouts: List[PositionalSoilLayout], top_profile: Polyline, piezo_lines: List[PiezoLine] = ...) -> SoilLayout2D: ...
    @classmethod
    def from_single_soil_layout(cls, soil_layout: SoilLayout, left_boundary: float, right_boundary: float, top_profile: Polyline, piezo_lines: List[PiezoLine] = ...) -> SoilLayout2D: ...
    @classmethod
    def combine_soil_layouts_2d(cls, *soil_layouts_2d: SoilLayout2D) -> SoilLayout2D: ...
    @classmethod
    def from_dict(cls, soil_layout_2d_dict: Union[dict, Munch]) -> SoilLayout2D: ...
    def serialize(self) -> dict: ...
    @property
    def top_profile(self) -> Polyline: ...
    @property
    def bottom_profile(self) -> Polyline: ...
    def visualize_geometry(self, visualize_border: bool = ..., opacity: float = ...) -> Tuple[Group, List[Label]]: ...
    def split(self, *split_lines: Polyline) -> List['SoilLayout2D']: ...
    def get_left_boundary_polyline(self) -> Polyline: ...
    def get_right_boundary_polyline(self) -> Polyline: ...
