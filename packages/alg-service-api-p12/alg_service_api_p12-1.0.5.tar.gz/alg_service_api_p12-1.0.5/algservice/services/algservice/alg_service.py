from typing import Protocol, List

from algservice.services.algservice.models import Mission, PreprocessResponse, DetectResponse, Algorithm


class AlgorithmService(Protocol):
    def get_version(self) -> str:
        ...

    def get_algorithms(self) -> List[Algorithm]:
        ...

    def pre_process(self, name: str, image: bytes, missions: List[Mission]) -> PreprocessResponse:
        ...

    def detect(self, name: str, image: bytes, missions: List[Mission]) -> DetectResponse:
        ...
