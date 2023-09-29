from abc import ABC, abstractmethod
from typing import List, Optional, Type, TypeVar

from pydeus.types.base import Base
from pydeus.types.responses.base import BaseResponse

HumanModel = TypeVar('HumanModel', bound=Base)
ModeusJsonResponse = TypeVar('ModeusJsonResponse', bound=BaseResponse)


class ABCConverter(ABC):
    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def convert_list(cls, *args, **kwargs) -> Optional[List[Type[HumanModel]]]:
        ...
