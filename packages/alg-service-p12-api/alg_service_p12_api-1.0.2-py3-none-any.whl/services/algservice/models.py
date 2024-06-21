from typing import List, Union, Dict


class ExecuteContext:
    def __init__(self):
        pass


class AlgParam:

    def set_var(self, name, val):
        setattr(self, name, val);

    def has(self, name):
        return hasattr(self, name)

    def get(self, name):
        return getattr(self, name)

    def __init__(self, **kwargs):
        for name in kwargs:
            setattr(self, name, kwargs[name])

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        return None

    def __eq__(self, other):
        if not isinstance(other, AlgParam):
            return NotImplemented
        return vars(self) == vars(other)

    def __contains__(self, key):
        return key in self.__dict__


class AlgorithmProp:
    def __init__(self, name: str = "", field_type: str = "", default_value: str = "", label: str = "",
                 required: bool = False):
        self.name = name
        self.field_type = field_type
        self.default_value = default_value
        self.label = label
        self.required = required


class Algorithm:

    def __init__(self, alg_id: str, alg_name: str):
        self.alg_id = alg_id
        self.alg_name = alg_name
        self.alg_props: List[AlgorithmProp] = []

    def add(self, a: AlgorithmProp):
        self.alg_props.append(a)

    def add_props(self, a: List[AlgorithmProp]):
        if a is not None and len(a) > 0:
            self.alg_props.extend(a)


class AlgorithmInfos:
    def __init__(self, name):
        self.name = name
        self.algs: List[Algorithm] = []

    def add(self, one: Algorithm):
        self.algs.append(one)

    def get_alg_size(self):
        return len(self.algs)


class Rect:
    def __init__(self, left=0, top=0, width=0, height=0):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __str__(self):
        return f'left:{self.left} ,top:{self.top} ,width:{self.width} ,height:{self.height} '


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x:{self.x} ,y:{self.y}'


class AlgRequest:
    def __init__(self):
        self.alg_id = ""
        self.alg_params = ""
        self.alg_data: Union[bytes, None] = None

        self._alg_params_obj: Union[AlgParam, None] = None

    def set_params_obj(self, obj: AlgParam):
        self._alg_params_obj = obj

    def get_params_obj(self) -> Union[AlgParam, None]:
        """
        :return: 保存了，缓冲的  alg props 转换后的数值
        """
        return self._alg_params_obj


class Mission:

    def __init__(self, mission_id: str):
        self.mission_id = mission_id
        self.shape: Union[Rect, List[Point], None] = None
        self.algs: List[AlgRequest] = []

    def set_shape_rect(self, rect: Rect):
        self.shape = rect

    def set_shape_points(self, pts: List[Point]):
        self.shape = pts

    def add_alg(self, alg: AlgRequest):
        self.algs.append(alg)


class PreprocessData:
    def __init__(self, alg_id: str, alg_data: bytes, result: int, message: str):
        self.alg_id = alg_id
        self.alg_data = alg_data
        self.result = result
        self.message = message


class MissionPreprocessResponse:  # MissionPreprocessResponse_
    def __init__(self, mission_id: str):
        self.mission_id = mission_id
        self.algs: List[PreprocessData] = []

    def add(self, ad: PreprocessData):
        self.algs.append(ad)


class PreprocessResponse:  # PreprocessResponse_
    def __init__(self, name: str = "", result: int = 0, message: str = ""):
        self.name = name
        self.result = result
        self.message = message
        self.missions: List[MissionPreprocessResponse] = []
        self.exts: Union[Dict[str, str], None] = None

    def add(self, ad: MissionPreprocessResponse):
        self.missions.append(ad)


###################################################################################

class AlgResponse:
    def __init__(self, alg_id: str, result: int, resp: str, data: bytes):
        self.alg_id = alg_id
        self.result = result
        self.resp = resp
        self.data = data


class MissionResponse:
    def __init__(self, mission_id: str, shape: List[Point]):
        self.mission_id = mission_id

        self.shape = shape
        self.algs: List[AlgResponse] = []

    def add(self, ad: AlgResponse):
        self.algs.append(ad)


class DetectResponse:
    def __init__(self, name, result: int, message: str):
        self.name = name
        self.result = result
        self.message = message
        self.missions: List[MissionResponse] = []
        self.exts: Union[Dict[str, str], None] = None

    def add(self, ad: MissionResponse):
        self.missions.append(ad)
