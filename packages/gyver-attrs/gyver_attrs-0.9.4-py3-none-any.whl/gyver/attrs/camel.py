from collections.abc import Callable
from typing import Any, Literal, Optional, TypeVar, Union, overload

import typing_extensions

from gyver.attrs.main import define

from .field import Field, FieldInfo, info
from .utils.functions import to_camel, to_pascal, to_upper_camel
from .utils.typedef import DisassembledType

T = TypeVar('T')


@typing_extensions.deprecated('Use the `alias_generator` parameter instead instead')
class ToCamelField(Field):
    def __init__(
        self,
        name: str,
        type_: DisassembledType,
        kw_only: bool,
        default: Any,
        alias: str,
        eq: Union[bool, Callable[[Any], Any]],
        order: Union[bool, Callable[[Any], Any]],
        inherited: bool = False,
    ) -> None:
        super().__init__(
            name,
            type_,
            kw_only,
            default,
            alias if alias != name else to_camel(name),
            eq,
            order,
            inherited,
            False,
            True,
            None,
            None,
        )


@typing_extensions.deprecated('Use the `alias_generator` parameter instead instead')
class ToUpperCamelField(Field):
    def __init__(
        self,
        name: str,
        type_: DisassembledType,
        kw_only: bool,
        default: Any,
        alias: str,
        eq: Union[bool, Callable[[Any], Any]],
        order: Union[bool, Callable[[Any], Any]],
        inherited: bool = False,
    ) -> None:
        super().__init__(
            name,
            type_,
            kw_only,
            default,
            alias if alias != name else to_upper_camel(name),
            eq,
            order,
            inherited,
            False,
            True,
            None,
            None,
        )


@overload
def define_camel(
    maybe_cls: None = None,
    /,
    *,
    style: Literal['upper', 'pascal', 'lower'] = 'lower',
    frozen: bool = True,
    kw_only: bool = False,
    slots: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = True,
    hash: Optional[bool] = None,
    pydantic: bool = True,
    dataclass_fields: bool = False,
) -> Callable[[type[T]], type[T]]: ...


@overload
def define_camel(
    maybe_cls: type[T],
    /,
    *,
    style: Literal['upper', 'pascal', 'lower'] = 'lower',
    frozen: bool = True,
    kw_only: bool = False,
    slots: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = True,
    hash: Optional[bool] = None,
    pydantic: bool = True,
    dataclass_fields: bool = False,
) -> type[T]: ...


@typing_extensions.dataclass_transform(
    order_default=True,
    frozen_default=True,
    kw_only_default=False,
    field_specifiers=(FieldInfo, info),
)
def define_camel(
    maybe_cls: Optional[type[T]] = None,
    /,
    *,
    style: Literal['pascal', 'upper', 'lower'] = 'lower',
    frozen: bool = True,
    kw_only: bool = False,
    slots: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = True,
    hash: Optional[bool] = None,
    pydantic: bool = True,
    dataclass_fields: bool = False,
) -> Union[Callable[[type[T]], type[T]], type[T]]:
    alias_generator = to_camel if style == 'lower' else to_pascal
    return define(
        maybe_cls,
        frozen=frozen,
        kw_only=kw_only,
        slots=slots,
        repr=repr,
        eq=eq,
        order=order,
        hash=hash,
        pydantic=pydantic,
        dataclass_fields=dataclass_fields,
        alias_generator=alias_generator,
    )
