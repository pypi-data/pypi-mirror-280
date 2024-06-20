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

from .single_val_expression_child import single_val_expression_child


class single_val_expression(NamedObject[single_val_expression_child], CreatableNamedObjectMixin[single_val_expression_child]):
    fluent_name = ...
    child_object_type = ...
    return_type = ...
