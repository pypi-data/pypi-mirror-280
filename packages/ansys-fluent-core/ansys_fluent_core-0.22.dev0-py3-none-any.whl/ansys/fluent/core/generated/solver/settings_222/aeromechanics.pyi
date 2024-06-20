#
# This is an auto-generated file.  DO NOT EDIT!
#


from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import (
    _ChildNamedObjectAccessorMixin,
    CreatableNamedObjectMixin,
    _NonCreatableNamedObjectMixin,
    AllowedValuesMixin,
    _InputFile,
    _OutputFile,
    _InOutFile,
)

from typing import Union, List, Tuple

from .aeromechanics_child import aeromechanics_child


class aeromechanics(NamedObject[aeromechanics_child], CreatableNamedObjectMixin[aeromechanics_child]):
    fluent_name = ...
    child_object_type = ...
    return_type = ...
