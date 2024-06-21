from pydantic import BaseModel, model_validator, field_validator, ConfigDict
from typing import List, Optional, Mapping
from importlib import import_module
from copy import copy


class MachineConfig(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: Optional[str] = None
    type: str
    states: Optional[List[str | Mapping[str, str | Mapping[str, str]]]] = None
    transitions: Optional[List[str] | List[Mapping[str, str]]] = None
    initial: Optional[str] = None

    @field_validator("type")
    @classmethod
    def get_class(cls, type: str):
        package_name = ".".join(type.split(".")[:-1])
        class_name = type.split(".")[-1]
        package = import_module(package_name)
        return getattr(package, class_name)

    @model_validator(mode="after")
    def default_name(self):
        if self.name is None:
            self.name = self.type.__name__
        return self

    @property
    def _as_dict(self):
        d = copy(self.__dict__)
        d.update(self.__pydantic_extra__)
        return {k:v for k, v in d.items() if v is not None}


class PigeonTransitionsConfig(BaseModel):
    machines: List[MachineConfig]
