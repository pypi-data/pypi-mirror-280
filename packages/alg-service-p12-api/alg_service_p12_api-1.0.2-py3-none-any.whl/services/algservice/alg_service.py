from typing import Protocol, List

from services.algservice.models import AlgorithmInfos, Mission, PreprocessResponse, DetectResponse, Algorithm, \
    AlgorithmProp


class AlgorithmService(Protocol):
    def get_version(self) -> str:
        ...

    def get_algorithms(self) -> List[Algorithm]:
        ...

    def pre_process(self, name: str, image: bytes, missions: List[Mission]) -> PreprocessResponse:
        ...

    def detect(self, name: str, image: bytes, missions: List[Mission]) -> DetectResponse:
        ...
