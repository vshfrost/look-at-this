import abc
from abc import abstractmethod
from typing import BinaryIO


class ClotheImageAdapter(abc.ABC):
    @abstractmethod
    def filename(self) -> str: ...

    @abstractmethod
    def content_type(self) -> str: ...

    @abstractmethod
    def file(self) -> BinaryIO: ...
