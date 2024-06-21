from typing import List
import grpc
from google.protobuf import empty_pb2

from services.algservice.alg_service import AlgorithmService
from services.algservice.models import Mission, DetectResponse, PreprocessResponse, AlgorithmInfos
from services.grpc.alg_service_pb2 import AlgorithmsRequest_

from services.grpc.alg_service_pb2_grpc import AlgServiceStub

from services.algservice.grpcutils import pb2_to_local, local_to_pb2
from services.algservice.pb2utils import wrapper_rpc_error


_EMPTY = empty_pb2.Empty()

class GrpcChannel:
    def __init__(self, host='localhost', port=49001):
        addr = f'{host}:{port}'

        self.channel = grpc.insecure_channel(addr)


class AlgServiceClient(AlgorithmService):

    def __init__(self, channel: GrpcChannel):
        self._stub = AlgServiceStub(channel.channel)



    @wrapper_rpc_error
    def get_version(self) -> str :

        response = self._stub.GetVersion(_EMPTY) # AlgorithmsResponse
        return response.version



    @wrapper_rpc_error
    def get_algorithms(self) -> AlgorithmInfos:
        """返回 当前支持的所有算法
        """
        # 对 输入 输出编解码
        req = AlgorithmsRequest_(name="")
        response = self._stub.GetAlgorithms(req) # AlgorithmsResponse
        return pb2_to_local.to_AlgorithmInfos(response)

    @wrapper_rpc_error
    def pre_process(self,   name:str  , image:bytes,   missions: List[Mission]   ) -> PreprocessResponse :
        """预处理，在注册阶段， 背景图+ 图形+算法+参数 需要获取一段兹定于数据
        ： 输入 注册图像，检测任务列表，算法参数， 返回 预处理数据，这个数据应该调用者保存，将来在检测时
        使用
        """

        req = local_to_pb2.to_DetectRequest_(name, image, missions)
        response = self._stub.Preprocess( req )
        return pb2_to_local.to_PreprocessResponse( response )

    @wrapper_rpc_error
    def detect(self,  name:str ,image:bytes,   missions: List[Mission]   ) -> DetectResponse :
        """检测： 输入 实时图像，检测任务列表， 返回 检测结果列表

        """
        req = local_to_pb2.to_DetectRequest_(name, image, missions)
        response = self._stub.Detect(req)
        return pb2_to_local.to_DetectResponse(response)


def create_alg_service_api(host, port) -> AlgServiceClient:
    c = GrpcChannel(host, port)
    return AlgServiceClient(c)
