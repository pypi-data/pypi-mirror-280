# Gyver Attrs

Gyver-attrs is a Python library that provides a more flexible and feature-rich alternative to the built-in attrs and dataclasses libraries for defining classes. The main function provided by Gyver-attrs is define, which allows users to define classes with a range of options and features.

## Installation

To install Gyver-attrs, you can use pip:

```console
pip install gyver-attrs
```

## Usage

The primary function in Gyver-attrs is define. It takes a list of field definitions and returns a new class with those fields defined as attributes. Here is a basic example:

```python
from gyver_attrs import define, info

@define
class Person:
    name: str
    age: int = info(default=18)
```
This defines a new class `Person` with two attributes, `name` and `age`.

## Features

Gyver-attrs provides a range of features that can be used to customize how classes are defined. These features include:

- maybe_cls: This option allows you to optionally specify the class to be created with the features applied. If it is None, it returns a callable that can wrap classes in the same way.
- frozen: This option replaces **`__setattr__`** and **`__getattr__`** of the class with frozen versions that raise AttributeError when attributes are accessed or modified. This can be useful for creating immutable objects.
- kw_only: This option makes the class's **`__init__`** not accept positional arguments, forcing all arguments to be passed as keyword arguments.
- slots: This option adds a **`__slots__`** to the class with the necessary validations and compliances with inheritance. It also validates possible descriptors with **`__set_name__`** to add the expected name to the **`__slots__`**.
- repr: This option adds a **`__repr__`** method to the resulting class.
- eq: This option provides **`__eq__`** and **`__ne__`** methods for the resulting class, comparing all values against each other. Each field can have a parser or opt-out using field(eq=False) or field(eq=my_converter).
- order: This option adds rich comparison support and supports the same mechanism of opt-out/converter as eq.
- hash: This option adds a hash function if all values are hashable and considers the converter from eq as well.
- pydantic: This option adds **`__get_validators__`** to the class to make Pydantic support the classes by default.
- dataclass_support: This option adds **`__dataclass_fields__`** with each field converted to a dataclass.Field before returning it on a dict. This way, the class becomes a drop-in replacement for dataclasses.

**Warning**: dataclass_fields with pydantic=False will fail when trying to use with pydantic.

## Methods

Gyver-attrs will add the following methods to your class.

__gyver_attrs__: This is a dictionary that maps each attribute name to its corresponding Field object. The Field object contains metadata about the attribute such as its name, type, default value, etc.
__parse_dict__(): This is a method that is used to parse the instance into a dict, recursively. Don't use it directly, instead call `asdict(self)`.
__iter__(): This will yield (key, value) for all fields directly included in the class, and not any fields of nested objects. You can use as `dict(self)`
__gserialize__(): This is a class method that is used to serialize a dict into an instance of the class. Don't use it directly, instead call `fromdict(self)`.
__pydantic_validate__(): This will validate inputs to support pydantic integration.
__get_validators__(): This is a classmethod to make your class pydantic-compatible.
__modify_schema__(): This is a class method that create schemas for your class when using Pydantic/FastAPI.

Also Gyver-attrs will not override custom defined functions instead, on conflict, you can still find them with the prefix `__gattrs_`.
Examples:
    `__init__` => `__gattrs_init__`
    `__hash__` => `__gattrs_hash__`
    `__parse_dict__` => `__gattrs_parse_dict__`

## Helper Functions

Gyver-attrs provides helpers to integrate easily with your project

- Shortcuts
  - `mutable`: same as `define` but with frozen=True
  - `kw_only`: same as `define` but with kw_only=True
- Camel
  - `define_camel`: same as `define` but with alias automatically as camel case. This can be either lower or upper camel which can be done by `style="upper"` or `style="lower`. By default `define_camel` uses lower.
- Helpers:
  - `call_init`: calls `__gattrs_init__` without mypy or pyright complaining
  - `fields`: returns a `dict[str, Field]` of the class, by returning `__gyver_attrs__`
- Factory:
  - `mark_factory`: decorator to mark function as factory
- Converters:
  - `fromdict`/`fromjson`: creates instance of class based on a dict/json(using orjson). Use as `fromdict(YourClass, mapping)` or `fromjson(YourClass, yourjson)`
  - `asdict`/`asjson`: returns your instance as dict/json(using orjson) recursively. Use as `asdict(instance, by_alias=True)` or `asdict(instance, by_alias=False)`

## Conclusion
Gyver-attrs provides a powerful and flexible way to define classes in Python, with a range of options and features that can be used to customize the behavior of the resulting classes. Whether you're building small scripts or large applications, Gyver-attrs can help you create classes that are tailored to your specific needs.
