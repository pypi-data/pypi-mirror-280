import os
from typing import Any, Callable, Literal, NoReturn, TypeAlias, overload

from .errors import (
    AttributeMutabilityError,
    EnvVarNameEmptyError,
    EnvVarNameTypeError,
    EnvVarNotFoundError,
    NonCallableConverterError,
)

ConverterType: TypeAlias = Callable[[str], Any]


class _EnvVar:
    def __init__(self, envvar_name: str, converter: ConverterType | None) -> None:
        self.envvar_name = envvar_name
        self.converter = converter

    def __set_name__(self, owner, name) -> None:
        self.attr_name = name

    def __get__(self, obj, obj_type=None):
        try:
            env_val = os.environ[self.envvar_name]
        except KeyError:
            raise EnvVarNotFoundError(self.envvar_name)

        if not self.converter:
            return env_val

        return self.converter(env_val)

    def __set__(self, obj, value: str):
        raise AttributeMutabilityError(self.attr_name)


@overload
def EnvVar(
    envvar_name: Literal[""], *, converter: ConverterType | None = None
) -> NoReturn: ...
@overload
def EnvVar(envvar_name: str, *, converter: ConverterType | None = None) -> Any: ...


def EnvVar(envvar_name, *, converter=None):
    """
    Function intended to be used as a default value for class
    attributes in classes that inherit from `ClassyEnv` class.

    When used, it validates the provided arguments and returns the `_EnvVar` descriptor.

    Example:
    ```python
    from classyenv import ClassyEnv, EnvVar

    class Settings(ClassyEnv):
        path: str = EnvVar("PATH")
        debug: bool = EnvVar("DEBUG", converter=bool)
    ```
    """

    if not isinstance(envvar_name, str):
        raise EnvVarNameTypeError(envvar_name)

    if envvar_name == "":
        raise EnvVarNameEmptyError

    if converter and not callable(converter):
        raise NonCallableConverterError

    return _EnvVar(envvar_name, converter)
