from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceVersion_(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class Size_(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: float
    height: float
    def __init__(self, width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class Point_(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Rect_(_message.Message):
    __slots__ = ("left", "top", "width", "height")
    LEFT_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    left: float
    top: float
    width: float
    height: float
    def __init__(self, left: _Optional[float] = ..., top: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class Polygon_(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[Point_]
    def __init__(self, points: _Optional[_Iterable[_Union[Point_, _Mapping]]] = ...) -> None: ...

class Shape_(_message.Message):
    __slots__ = ("polygon", "box")
    POLYGON_FIELD_NUMBER: _ClassVar[int]
    BOX_FIELD_NUMBER: _ClassVar[int]
    polygon: Polygon_
    box: Rect_
    def __init__(self, polygon: _Optional[_Union[Polygon_, _Mapping]] = ..., box: _Optional[_Union[Rect_, _Mapping]] = ...) -> None: ...

class AlgRequest_(_message.Message):
    __slots__ = ("algId", "algParams", "algData")
    ALGID_FIELD_NUMBER: _ClassVar[int]
    ALGPARAMS_FIELD_NUMBER: _ClassVar[int]
    ALGDATA_FIELD_NUMBER: _ClassVar[int]
    algId: str
    algParams: str
    algData: bytes
    def __init__(self, algId: _Optional[str] = ..., algParams: _Optional[str] = ..., algData: _Optional[bytes] = ...) -> None: ...

class Mission_(_message.Message):
    __slots__ = ("missionID", "shape", "algs")
    MISSIONID_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    ALGS_FIELD_NUMBER: _ClassVar[int]
    missionID: str
    shape: Shape_
    algs: _containers.RepeatedCompositeFieldContainer[AlgRequest_]
    def __init__(self, missionID: _Optional[str] = ..., shape: _Optional[_Union[Shape_, _Mapping]] = ..., algs: _Optional[_Iterable[_Union[AlgRequest_, _Mapping]]] = ...) -> None: ...

class AlgResponse_(_message.Message):
    __slots__ = ("algId", "result", "resp", "data")
    ALGID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    algId: str
    result: int
    resp: str
    data: bytes
    def __init__(self, algId: _Optional[str] = ..., result: _Optional[int] = ..., resp: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class MissionResponse_(_message.Message):
    __slots__ = ("missionId", "shape", "algs")
    MISSIONID_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    ALGS_FIELD_NUMBER: _ClassVar[int]
    missionId: str
    shape: Shape_
    algs: _containers.RepeatedCompositeFieldContainer[AlgResponse_]
    def __init__(self, missionId: _Optional[str] = ..., shape: _Optional[_Union[Shape_, _Mapping]] = ..., algs: _Optional[_Iterable[_Union[AlgResponse_, _Mapping]]] = ...) -> None: ...

class AlgorithmsRequest_(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AlgorithmProp_(_message.Message):
    __slots__ = ("name", "fieldType", "defaultValue", "required", "label")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDTYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    fieldType: str
    defaultValue: str
    required: bool
    label: str
    def __init__(self, name: _Optional[str] = ..., fieldType: _Optional[str] = ..., defaultValue: _Optional[str] = ..., required: bool = ..., label: _Optional[str] = ...) -> None: ...

class AlgorithmInfo_(_message.Message):
    __slots__ = ("algId", "algName", "props")
    ALGID_FIELD_NUMBER: _ClassVar[int]
    ALGNAME_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    algId: str
    algName: str
    props: _containers.RepeatedCompositeFieldContainer[AlgorithmProp_]
    def __init__(self, algId: _Optional[str] = ..., algName: _Optional[str] = ..., props: _Optional[_Iterable[_Union[AlgorithmProp_, _Mapping]]] = ...) -> None: ...

class AlgorithmsResponse_(_message.Message):
    __slots__ = ("name", "algs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    algs: _containers.RepeatedCompositeFieldContainer[AlgorithmInfo_]
    def __init__(self, name: _Optional[str] = ..., algs: _Optional[_Iterable[_Union[AlgorithmInfo_, _Mapping]]] = ...) -> None: ...

class DetectRequest_(_message.Message):
    __slots__ = ("name", "image", "missions", "exts")
    class ExtsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    MISSIONS_FIELD_NUMBER: _ClassVar[int]
    EXTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    image: bytes
    missions: _containers.RepeatedCompositeFieldContainer[Mission_]
    exts: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., image: _Optional[bytes] = ..., missions: _Optional[_Iterable[_Union[Mission_, _Mapping]]] = ..., exts: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DetectResponse_(_message.Message):
    __slots__ = ("name", "result", "message", "missions", "exts")
    class ExtsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MISSIONS_FIELD_NUMBER: _ClassVar[int]
    EXTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    result: int
    message: str
    missions: _containers.RepeatedCompositeFieldContainer[MissionResponse_]
    exts: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., result: _Optional[int] = ..., message: _Optional[str] = ..., missions: _Optional[_Iterable[_Union[MissionResponse_, _Mapping]]] = ..., exts: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PreprocessData_(_message.Message):
    __slots__ = ("algId", "result", "message", "algData")
    ALGID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ALGDATA_FIELD_NUMBER: _ClassVar[int]
    algId: str
    result: int
    message: str
    algData: bytes
    def __init__(self, algId: _Optional[str] = ..., result: _Optional[int] = ..., message: _Optional[str] = ..., algData: _Optional[bytes] = ...) -> None: ...

class MissionPreprocessResponse_(_message.Message):
    __slots__ = ("missionId", "algs")
    MISSIONID_FIELD_NUMBER: _ClassVar[int]
    ALGS_FIELD_NUMBER: _ClassVar[int]
    missionId: str
    algs: _containers.RepeatedCompositeFieldContainer[PreprocessData_]
    def __init__(self, missionId: _Optional[str] = ..., algs: _Optional[_Iterable[_Union[PreprocessData_, _Mapping]]] = ...) -> None: ...

class PreprocessResponse_(_message.Message):
    __slots__ = ("name", "result", "message", "missions", "exts")
    class ExtsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MISSIONS_FIELD_NUMBER: _ClassVar[int]
    EXTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    result: int
    message: str
    missions: _containers.RepeatedCompositeFieldContainer[MissionPreprocessResponse_]
    exts: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., result: _Optional[int] = ..., message: _Optional[str] = ..., missions: _Optional[_Iterable[_Union[MissionPreprocessResponse_, _Mapping]]] = ..., exts: _Optional[_Mapping[str, str]] = ...) -> None: ...
