import json
from .api_v1 import API as API, FileResource as FileResource
from .core import Color as Color, File as File
from .errors import ExecutionError as ExecutionError
from .geometry import GeoPoint as GeoPoint, GeoPolygon as GeoPolygon, GeoPolyline as GeoPolyline
from .parametrization import ColorField as ColorField, DateField as DateField, FileField as FileField, GeoPointField as GeoPointField, GeoPolygonField as GeoPolygonField, GeoPolylineField as GeoPolylineField
from _typeshed import Incomplete
from munch import Munch as Munch
from typing import Any, BinaryIO, Callable, Iterator, Union

logger: Incomplete
Serializable = Union[bool, dict, float, int, list, None, tuple]

class _CacheMiss: ...

class _ParamsEncoder(json.JSONEncoder):
    def iterencode(self, o: Union[dict, Munch], _one_shot: bool = ...) -> Iterator[str]: ...

class _ParamsDecoder(json.JSONDecoder):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def object_hook(data: dict) -> Any: ...

def memoize(fun: Callable) -> Callable: ...
def render_jinja_template(template: BinaryIO, variables: dict) -> File: ...
def merge_pdf_files(*files: BinaryIO) -> File: ...
def convert_word_to_pdf(file: BinaryIO) -> File: ...
def convert_excel_to_pdf(file: BinaryIO) -> File: ...
def convert_svg_to_pdf(file: BinaryIO) -> File: ...
