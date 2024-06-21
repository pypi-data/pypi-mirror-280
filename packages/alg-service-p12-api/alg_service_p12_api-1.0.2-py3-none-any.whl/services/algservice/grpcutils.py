
from typing import List, Union, Dict

from google.protobuf.internal.containers import ScalarMap

from services.algservice.models import AlgorithmInfos, Algorithm, Mission, Rect, Point, AlgRequest, \
    PreprocessResponse, \
    DetectResponse, MissionResponse, AlgResponse, MissionPreprocessResponse, PreprocessData, AlgorithmProp
from services.algservice.pb2utils import value_or_empty, bytes_or_empty, array_or_empty
from services.grpc.alg_service_pb2 import AlgorithmsResponse_, AlgorithmInfo_, Shape_, Point_, Mission_, AlgRequest_, \
    DetectRequest_, PreprocessResponse_, MissionPreprocessResponse_, DetectResponse_, MissionResponse_, \
    PreprocessData_, AlgResponse_, AlgorithmProp_
from util.exceptions import ErrorException, ErrorCode

ALG_PARAM_COLOR = "color"
ALG_PARAM_DETECT = "detect"


class pb2_to_local:
    """

    # 将 GRPC 数据转换为 Python Models

    """

    @staticmethod
    def to_AlgorithmInfos(s: AlgorithmsResponse_) -> AlgorithmInfos:
        x = AlgorithmInfos(s.name)
        for alg in s.algs:
            a = Algorithm(alg.algId, alg.algName)
            if alg.props is not None:
                for prop in alg.props:
                    pp = pb2_to_local.to_AlgorithmProp(prop)
                    a.alg_props.append(pp)

            x.add(a)

        return x

    @staticmethod
    def to_AlgorithmProp(prop: AlgorithmProp_) -> AlgorithmProp:
        out = AlgorithmProp(prop.name, prop.fieldType, prop.defaultValue, prop.label, prop.required)
        return out

    ###################################

    @staticmethod
    def to_MissionPreprocessResponse(s: MissionPreprocessResponse_) -> MissionPreprocessResponse:
        x = MissionPreprocessResponse(s.missionId )
        for alg in s.algs:
            x.add(PreprocessData(alg.algId, alg.algData,alg.result, alg.message))
        return x

    @staticmethod
    def to_PreprocessResponse(s: PreprocessResponse_) -> PreprocessResponse:
        x = PreprocessResponse(s.name, s.result, s.message)
        for mission in s.missions:
            m = pb2_to_local.to_MissionPreprocessResponse(mission)
            x.add(m)

        x.exts  = pb2_to_local.to_Dict_Str_Str(s.exts)
        return x

    @staticmethod
    def to_Dict_Str_Str(exts: ScalarMap[str, str]) -> Union[Dict[str, str], None]:

        size = len(exts)
        if size == 0:
            return None

        out: Dict[str, str] = dict()
        for key in exts.keys():
            val = exts.get(key)
            out[key] = val

        return out

    #################################

    @staticmethod
    def to_Shape(shape: Shape_) -> Union[Rect, List[Point]]:

        if shape.HasField("box"):
            b = Rect()
            b.top = shape.box.top
            b.left = shape.box.left
            b.width = shape.box.width
            b.height = shape.box.height
            return b

        if shape.HasField("polygon"):
            c: List[Point] = []
            for one in shape.polygon.points:
                c.append(Point(one.x, one.y))
            return c

        raise ErrorException(ErrorCode.invalid_argument, f"Unknown type - {type(shape)} , {shape.ListFields()}")

    @staticmethod
    def to_MissionResponse(s: MissionResponse_) -> MissionResponse:

        ns = pb2_to_local.to_Shape(s.shape)
        x = MissionResponse(s.missionId,   ns)
        for alg in s.algs:
            x.add(AlgResponse(alg.algId, alg.result, alg.resp , alg.data ))
        return x

    @staticmethod
    def to_DetectResponse(s: DetectResponse_) -> DetectResponse:
        x = DetectResponse(s.name, s.result, s.message)
        for mission in s.missions:
            m = pb2_to_local.to_MissionResponse(mission)
            x.add(m)
        x.exts = pb2_to_local.to_Dict_Str_Str(s.exts)
        return x

    #####################################################

    @staticmethod
    def to_AlgRequest(a: AlgRequest_) -> AlgRequest:
        b = AlgRequest()
        b.alg_id = a.algId
        b.alg_data = a.algData
        b.alg_params = a.algParams

        return b

    @staticmethod
    def to_Mission(m: Mission_) -> Mission:
        mission_id = m.missionID
        o = Mission(mission_id)
        o.shape = pb2_to_local.to_Shape(m.shape)
        for one in m.algs:
            alg = pb2_to_local.to_AlgRequest(one)
            o.add_alg(alg)
        return o

    @staticmethod
    def parse_DetectRequest(r: DetectRequest_) -> (str, bytes, List[Mission]):
        name = r.name
        image = r.image,
        missions: List[Mission] = []

        for mission in r.missions:
            nm = pb2_to_local.to_Mission(mission)
            missions.append(nm)

        return name, image, missions


#####################################################################################################################


class local_to_pb2:
    """

    # 将 Python Models  数据转换为 GRPC

    """

    @staticmethod
    def to_AlgorithmProp(prop: AlgorithmProp) -> AlgorithmProp_:
        out = AlgorithmProp_(name=value_or_empty(prop.name), fieldType=value_or_empty(prop.field_type),
                             defaultValue=value_or_empty(prop.default_value),
                             label=value_or_empty(prop.label), required=prop.required)
        return out

    @staticmethod
    def to_AlgorithmInfo(s: Algorithm) -> AlgorithmInfo_:
        x = AlgorithmInfo_(algId=value_or_empty(s.alg_id), algName=value_or_empty(s.alg_name))

        if s.alg_props is not None:
            for prop in s.alg_props:
                pp = local_to_pb2.to_AlgorithmProp(prop)
                x.props.append(pp)

        return x

    @staticmethod
    def to_AlgorithmsResponse(name: str, algs: List[Algorithm]) -> AlgorithmsResponse_:
        newalgs = [local_to_pb2.to_AlgorithmInfo(alg) for alg in algs]
        return AlgorithmsResponse_(name=value_or_empty(name), algs=newalgs)

    @staticmethod
    def to_ScalarMap_Str_Str(exts: Dict[str, str], out: ScalarMap[str, str]) -> ScalarMap[str, str]:

        if exts is None:
            return out
        for key in exts.keys():
            val = exts.get(key)
            out[key] = val

        return out

    @staticmethod
    def to_Shape_(shape) -> Shape_:

        if isinstance(shape, Rect):
            a = Shape_()
            b: Rect = shape
            a.box.top = b.top
            a.box.left = b.left
            a.box.width = b.width
            a.box.height = b.height
            return a

        if isinstance(shape, list):
            # should be List[Point]
            a = Shape_()
            b: List[Point] = shape
            for one in b:
                a.polygon.points.append(Point_(x=one.x, y=one.y))

        raise ErrorException(ErrorCode.invalid_argument, f"Unknown type - {type(shape)} , {shape}")

    @staticmethod
    def to_AlgRequest_(a: AlgRequest) -> AlgRequest_:

        c = AlgRequest_(algId=value_or_empty(a.alg_id), algData=bytes_or_empty(a.alg_data),
                        algParams=value_or_empty(a.alg_params))
        return c

    @staticmethod
    def to_Mission_(m: Mission) -> Mission_:
        shape = local_to_pb2.to_Shape_(m.shape)

        mission = Mission_(missionID=value_or_empty(m.mission_id), shape=shape)

        for one in m.algs:
            alg = local_to_pb2.to_AlgRequest_(one)
            mission.algs.append(alg)

        return mission

    @staticmethod
    def to_DetectRequest_(name: str, image: bytes, missions: List[Mission]) -> DetectRequest_:
        req = DetectRequest_(name=value_or_empty(name), image=bytes_or_empty(image))
        # local_to_pb2.to_ScalarMap_Str_Str(m.exts, req.exts)
        for mission in missions:
            nm = local_to_pb2.to_Mission_(mission)
            req.missions.append(nm)

        return req

    ##################################################

    @staticmethod
    def to_MissionPreprocessResponse_(m: MissionPreprocessResponse) -> MissionPreprocessResponse_:

        o = MissionPreprocessResponse_(missionId=value_or_empty(m.mission_id) )
        for one in m.algs:
            o.algs.append(PreprocessData_(algId=value_or_empty(one.alg_id), algData=bytes_or_empty(one.alg_data)))
        return o

    @staticmethod
    def to_PreprocessResponse_(p: PreprocessResponse) -> PreprocessResponse_:
        req = PreprocessResponse_(name=value_or_empty(p.name), result=p.result, message=value_or_empty(p.message))
        for mission in p.missions:
            nm = local_to_pb2.to_MissionPreprocessResponse_(mission)
            req.missions.append(nm)
        local_to_pb2.to_ScalarMap_Str_Str(p.exts, req.exts)
        return req

    ##################################################

    @staticmethod
    def to_MissionResponse_(m: MissionResponse) -> MissionResponse_:
        shape = local_to_pb2.to_Shape_(m.shape)

        o = MissionResponse_(missionId=value_or_empty(m.mission_id),
                             shape=shape)

        for one in m.algs:
            o.algs.append(
                AlgResponse_(algId=value_or_empty(one.alg_id), result=one.result, resp=value_or_empty(one.resp),
                             data=bytes_or_empty(one.data)))
        return o

    @staticmethod
    def to_DetectResponse_(p: DetectResponse) -> DetectResponse_:
        req = DetectResponse_(name=value_or_empty(p.name), result=p.result, message=value_or_empty(p.message))
        for mission in p.missions:
            nm = local_to_pb2.to_MissionResponse_(mission)
            req.missions.append(nm)
        return req
