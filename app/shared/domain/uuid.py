import typing

from uuid6 import uuid7, UUID


class Uuid:
    def __init__(self, uuid: UUID) -> None:
        self._uuid = uuid

    @classmethod
    def create(cls) -> typing.Self:
        return cls(uuid=uuid7())

    @property
    def value(self) -> UUID:
        return self._uuid

    def to_string(self) -> str:
        return str(self.value)
