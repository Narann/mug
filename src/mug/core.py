"""
Main internal module.
"""
from enum import IntEnum
from typing import BinaryIO, List, Any
import struct

MAX_U8 = 255
MAX_U16 = 65535
MAX_U32 = 4294967295
MAX_U64 = 9223372036854775808

BYTE_ORDER = 'little'


class AttributeType(IntEnum):
    # 1 component
    U8 = 0
    U16 = 1
    U32 = 2
    U64 = 3
    I8 = 4
    I16 = 5
    I32 = 6
    I64 = 7
    F16 = 8
    F32 = 9
    F64 = 10
    STR = 11

    # 2 components
    U8X2 = 12
    U16X2 = 13
    U32X2 = 14
    U64X2 = 15
    I8X2 = 16
    I16X2 = 17
    I32X2 = 18
    I64X2 = 19
    F16X2 = 20
    F32X2 = 21
    F64X2 = 22

    # 3 components
    U8X3 = 23
    U16X3 = 24
    U32X3 = 25
    U64X3 = 26
    I8X3 = 27
    I16X3 = 28
    I32X3 = 29
    I64X3 = 30
    F16X3 = 31
    F32X3 = 32
    F64X3 = 33

    # 4 components
    U8X4 = 34
    U16X4 = 35
    U32X4 = 36
    U64X4 = 37
    I8X4 = 38
    I16X4 = 39
    I32X4 = 40
    I64X4 = 41
    F16X4 = 42
    F32X4 = 43
    F64X4 = 44

    # 9 components
    U8X9 = 45
    U16X9 = 46
    U32X9 = 47
    U64X9 = 48
    I8X9 = 49
    I16X9 = 50
    I32X9 = 51
    I64X9 = 52
    F16X9 = 53
    F32X9 = 54
    F64X9 = 55

    # 16 components
    U8X16 = 56
    U16X16 = 57
    U32X16 = 58
    U64X16 = 59
    I8X16 = 60
    I16X16 = 61
    I32X16 = 62
    I64X16 = 63
    F16X16 = 64
    F32X16 = 65
    F64X16 = 66

    # N components
    U8_ARRAY = 67
    U16_ARRAY = 68
    U32_ARRAY = 69
    U64_ARRAY = 70
    I8_ARRAY = 71
    I16_ARRAY = 72
    I32_ARRAY = 73
    I64_ARRAY = 74
    F16_ARRAY = 75
    F32_ARRAY = 76
    F64_ARRAY = 77
    STR_ARRAY = 78


def attr_type_read(fd: BinaryIO) -> AttributeType:
    return AttributeType.from_bytes(fd.read(1), BYTE_ORDER, signed=False)


def as_attr_value_bytes(attr_type: AttributeType, value: Any):
    if attr_type == AttributeType.U8:
        return value.to_bytes(1, BYTE_ORDER, signed=False)
    elif attr_type == AttributeType.U16:
        return value.to_bytes(2, BYTE_ORDER, signed=False)
    elif attr_type == AttributeType.U32:
        return value.to_bytes(4, BYTE_ORDER, signed=False)
    elif attr_type == AttributeType.U64:
        return value.to_bytes(8, BYTE_ORDER, signed=False)
    elif attr_type == AttributeType.I8:
        return value.to_bytes(1, BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.I16:
        return value.to_bytes(2, BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.I32:
        return value.to_bytes(4, BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.I64:
        return value.to_bytes(8, BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.F16:
        return struct.pack('<e', value)
    elif attr_type == AttributeType.F32:
        return struct.pack('<f', value)
    elif attr_type == AttributeType.F64:
        return struct.pack('<d', value)
    elif attr_type == AttributeType.STR:
        return as_str_bytes(value)
    elif attr_type == AttributeType.U8X2:
        return struct.pack('<2B', *value)
    elif attr_type == AttributeType.U16X2:
        return struct.pack('<2H', *value)
    elif attr_type == AttributeType.U32X2:
        return struct.pack('<2I', *value)
    elif attr_type == AttributeType.U64X2:
        return struct.pack('<2Q', *value)
    elif attr_type == AttributeType.I8X2:
        return struct.pack('<2b', *value)
    elif attr_type == AttributeType.I16X2:
        return struct.pack('<2h', *value)
    elif attr_type == AttributeType.I32X2:
        return struct.pack('<2i', *value)
    elif attr_type == AttributeType.I64X2:
        return struct.pack('<2q', *value)
    elif attr_type == AttributeType.F16X2:
        return struct.pack('<2e', *value)
    elif attr_type == AttributeType.F32X2:
        return struct.pack('<2f', *value)
    elif attr_type == AttributeType.F64X2:
        return struct.pack('<2d', *value)
    elif attr_type == AttributeType.U8X3:
        return struct.pack('<3B', *value)
    elif attr_type == AttributeType.U16X3:
        return struct.pack('<3H', *value)
    elif attr_type == AttributeType.U32X3:
        return struct.pack('<3I', *value)
    elif attr_type == AttributeType.U64X3:
        return struct.pack('<3Q', *value)
    elif attr_type == AttributeType.I8X3:
        return struct.pack('<3b', *value)
    elif attr_type == AttributeType.I16X3:
        return struct.pack('<3h', *value)
    elif attr_type == AttributeType.I32X3:
        return struct.pack('<3i', *value)
    elif attr_type == AttributeType.I64X3:
        return struct.pack('<3q', *value)
    elif attr_type == AttributeType.F16X3:
        return struct.pack('<3e', *value)
    elif attr_type == AttributeType.F32X3:
        return struct.pack('<3f', *value)
    elif attr_type == AttributeType.F64X3:
        return struct.pack('<3d', *value)
    elif attr_type == AttributeType.U8X4:
        return struct.pack('<4B', *value)
    elif attr_type == AttributeType.U16X4:
        return struct.pack('<4H', *value)
    elif attr_type == AttributeType.U32X4:
        return struct.pack('<4I', *value)
    elif attr_type == AttributeType.U64X4:
        return struct.pack('<4Q', *value)
    elif attr_type == AttributeType.I8X4:
        return struct.pack('<4b', *value)
    elif attr_type == AttributeType.I16X4:
        return struct.pack('<4h', *value)
    elif attr_type == AttributeType.I32X4:
        return struct.pack('<4i', *value)
    elif attr_type == AttributeType.I64X4:
        return struct.pack('<4q', *value)
    elif attr_type == AttributeType.F16X4:
        return struct.pack('<4e', *value)
    elif attr_type == AttributeType.F32X4:
        return struct.pack('<4f', *value)
    elif attr_type == AttributeType.F64X4:
        return struct.pack('<4d', *value)
    elif attr_type == AttributeType.U8X9:
        return struct.pack('<9B', *value)
    elif attr_type == AttributeType.U16X9:
        return struct.pack('<9H', *value)
    elif attr_type == AttributeType.U32X9:
        return struct.pack('<9I', *value)
    elif attr_type == AttributeType.U64X9:
        return struct.pack('<9Q', *value)
    elif attr_type == AttributeType.I8X9:
        return struct.pack('<9b', *value)
    elif attr_type == AttributeType.I16X9:
        return struct.pack('<9h', *value)
    elif attr_type == AttributeType.I32X9:
        return struct.pack('<9i', *value)
    elif attr_type == AttributeType.I64X9:
        return struct.pack('<9q', *value)
    elif attr_type == AttributeType.F16X9:
        return struct.pack('<9e', *value)
    elif attr_type == AttributeType.F32X9:
        return struct.pack('<9f', *value)
    elif attr_type == AttributeType.F64X9:
        return struct.pack('<9d', *value)
    elif attr_type == AttributeType.U8X16:
        return struct.pack('<16B', *value)
    elif attr_type == AttributeType.U16X16:
        return struct.pack('<16H', *value)
    elif attr_type == AttributeType.U32X16:
        return struct.pack('<16I', *value)
    elif attr_type == AttributeType.U64X16:
        return struct.pack('<16Q', *value)
    elif attr_type == AttributeType.I8X16:
        return struct.pack('<16b', *value)
    elif attr_type == AttributeType.I16X16:
        return struct.pack('<16h', *value)
    elif attr_type == AttributeType.I32X16:
        return struct.pack('<16i', *value)
    elif attr_type == AttributeType.I64X16:
        return struct.pack('<16q', *value)
    elif attr_type == AttributeType.F16X16:
        return struct.pack('<16e', *value)
    elif attr_type == AttributeType.F32X16:
        return struct.pack('<16f', *value)
    elif attr_type == AttributeType.F64X16:
        return struct.pack('<16d', *value)
    elif attr_type == AttributeType.U8_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}B'.format(len(value)), *value)
    elif attr_type == AttributeType.U16_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}H'.format(len(value)), *value)
    elif attr_type == AttributeType.U32_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}I'.format(len(value)), *value)
    elif attr_type == AttributeType.U64_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}Q'.format(len(value)), *value)
    elif attr_type == AttributeType.I8_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}b'.format(len(value)), *value)
    elif attr_type == AttributeType.I16_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}h'.format(len(value)), *value)
    elif attr_type == AttributeType.I32_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}i'.format(len(value)), *value)
    elif attr_type == AttributeType.I64_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}q'.format(len(value)), *value)
    elif attr_type == AttributeType.F16_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}e'.format(len(value)), *value)
    elif attr_type == AttributeType.F32_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}f'.format(len(value)), *value)
    elif attr_type == AttributeType.F64_ARRAY:
        return as_suint_bytes(len(value)) + \
               struct.pack('<{}d'.format(len(value)), *value)
    elif attr_type == AttributeType.STR_ARRAY:
        return as_suint_bytes(len(value)) + \
               b''.join((as_str_bytes(s) for s in value))
    else:
        raise ValueError("unknown attribute type")


def attr_value_read(fd: BinaryIO, attr_type: AttributeType):
    if attr_type == AttributeType.U8:
        return int.from_bytes(fd.read(1), BYTE_ORDER, signed=False)
    elif attr_type == AttributeType.U16:
        return int.from_bytes(fd.read(2), BYTE_ORDER, signed=False)
    elif attr_type == AttributeType.U32:
        return int.from_bytes(fd.read(4), BYTE_ORDER, signed=False)
    elif attr_type == AttributeType.U64:
        return int.from_bytes(fd.read(8), BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.I8:
        return int.from_bytes(fd.read(1), BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.I16:
        return int.from_bytes(fd.read(2), BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.I32:
        return int.from_bytes(fd.read(4), BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.I64:
        return int.from_bytes(fd.read(8), BYTE_ORDER, signed=True)
    elif attr_type == AttributeType.F16:
        return struct.unpack('<e', fd.read(2))[0]
    elif attr_type == AttributeType.F32:
        return struct.unpack('<f', fd.read(4))[0]
    elif attr_type == AttributeType.F64:
        return struct.unpack('<d', fd.read(8))[0]
    elif attr_type == AttributeType.STR:
        return str_read(fd)
    elif attr_type == AttributeType.U8X2:
        return struct.unpack('<2B', fd.read(2))
    elif attr_type == AttributeType.U16X2:
        return struct.unpack('<2H', fd.read(4))
    elif attr_type == AttributeType.U32X2:
        return struct.unpack('<2I', fd.read(8))
    elif attr_type == AttributeType.U64X2:
        return struct.unpack('<2Q', fd.read(16))
    elif attr_type == AttributeType.I8X2:
        return struct.unpack('<2b', fd.read(2))
    elif attr_type == AttributeType.I16X2:
        return struct.unpack('<2h', fd.read(4))
    elif attr_type == AttributeType.I32X2:
        return struct.unpack('<2i', fd.read(8))
    elif attr_type == AttributeType.I64X2:
        return struct.unpack('<2q', fd.read(16))
    elif attr_type == AttributeType.F16X2:
        return struct.unpack('<2e', fd.read(4))
    elif attr_type == AttributeType.F32X2:
        return struct.unpack('<2f', fd.read(8))
    elif attr_type == AttributeType.F64X2:
        return struct.unpack('<2d', fd.read(16))
    elif attr_type == AttributeType.U8X3:
        return struct.unpack('<3B', fd.read(3))
    elif attr_type == AttributeType.U16X3:
        return struct.unpack('<3H', fd.read(6))
    elif attr_type == AttributeType.U32X3:
        return struct.unpack('<3I', fd.read(12))
    elif attr_type == AttributeType.U64X3:
        return struct.unpack('<3Q', fd.read(24))
    elif attr_type == AttributeType.I8X3:
        return struct.unpack('<3b', fd.read(3))
    elif attr_type == AttributeType.I16X3:
        return struct.unpack('<3h', fd.read(6))
    elif attr_type == AttributeType.I32X3:
        return struct.unpack('<3i', fd.read(12))
    elif attr_type == AttributeType.I64X3:
        return struct.unpack('<3q', fd.read(24))
    elif attr_type == AttributeType.F16X3:
        return struct.unpack('<3e', fd.read(6))
    elif attr_type == AttributeType.F32X3:
        return struct.unpack('<3f', fd.read(12))
    elif attr_type == AttributeType.F64X3:
        return struct.unpack('<3d', fd.read(24))
    elif attr_type == AttributeType.U8X4:
        return struct.unpack('<4B', fd.read(4))
    elif attr_type == AttributeType.U16X4:
        return struct.unpack('<4H', fd.read(8))
    elif attr_type == AttributeType.U32X4:
        return struct.unpack('<4I', fd.read(16))
    elif attr_type == AttributeType.U64X4:
        return struct.unpack('<4Q', fd.read(32))
    elif attr_type == AttributeType.I8X4:
        return struct.unpack('<4b', fd.read(4))
    elif attr_type == AttributeType.I16X4:
        return struct.unpack('<4h', fd.read(8))
    elif attr_type == AttributeType.I32X4:
        return struct.unpack('<4i', fd.read(16))
    elif attr_type == AttributeType.I64X4:
        return struct.unpack('<4q', fd.read(32))
    elif attr_type == AttributeType.F16X4:
        return struct.unpack('<4e', fd.read(8))
    elif attr_type == AttributeType.F32X4:
        return struct.unpack('<4f', fd.read(16))
    elif attr_type == AttributeType.F64X4:
        return struct.unpack('<4d', fd.read(32))
    elif attr_type == AttributeType.U8X9:
        return struct.unpack('<9B', fd.read(9))
    elif attr_type == AttributeType.U16X9:
        return struct.unpack('<9H', fd.read(18))
    elif attr_type == AttributeType.U32X9:
        return struct.unpack('<9I', fd.read(36))
    elif attr_type == AttributeType.U64X9:
        return struct.unpack('<9Q', fd.read(72))
    elif attr_type == AttributeType.I8X9:
        return struct.unpack('<9b', fd.read(9))
    elif attr_type == AttributeType.I16X9:
        return struct.unpack('<9h', fd.read(18))
    elif attr_type == AttributeType.I32X9:
        return struct.unpack('<9i', fd.read(36))
    elif attr_type == AttributeType.I64X9:
        return struct.unpack('<9q', fd.read(72))
    elif attr_type == AttributeType.F16X9:
        return struct.unpack('<9e', fd.read(18))
    elif attr_type == AttributeType.F32X9:
        return struct.unpack('<9f', fd.read(36))
    elif attr_type == AttributeType.F64X9:
        return struct.unpack('<9d', fd.read(72))
    elif attr_type == AttributeType.U8X16:
        return struct.unpack('<16B', fd.read(16))
    elif attr_type == AttributeType.U16X16:
        return struct.unpack('<16H', fd.read(32))
    elif attr_type == AttributeType.U32X16:
        return struct.unpack('<16I', fd.read(64))
    elif attr_type == AttributeType.U64X16:
        return struct.unpack('<16Q', fd.read(128))
    elif attr_type == AttributeType.I8X16:
        return struct.unpack('<16b', fd.read(16))
    elif attr_type == AttributeType.I16X16:
        return struct.unpack('<16h', fd.read(32))
    elif attr_type == AttributeType.I32X16:
        return struct.unpack('<16i', fd.read(64))
    elif attr_type == AttributeType.I64X16:
        return struct.unpack('<16q', fd.read(128))
    elif attr_type == AttributeType.F16X16:
        return struct.unpack('<16e', fd.read(32))
    elif attr_type == AttributeType.F32X16:
        return struct.unpack('<16f', fd.read(64))
    elif attr_type == AttributeType.F64X16:
        return struct.unpack('<16d', fd.read(128))
    elif attr_type == AttributeType.U8_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}B'.format(value_count),
                             fd.read(1 * value_count))
    elif attr_type == AttributeType.U16_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}H'.format(value_count),
                             fd.read(2 * value_count))
    elif attr_type == AttributeType.U32_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}I'.format(value_count),
                             fd.read(4 * value_count))
    elif attr_type == AttributeType.U64_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}Q'.format(value_count),
                             fd.read(8 * value_count))
    elif attr_type == AttributeType.I8_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}b'.format(value_count),
                             fd.read(1 * value_count))
    elif attr_type == AttributeType.I16_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}h'.format(value_count),
                             fd.read(2 * value_count))
    elif attr_type == AttributeType.I32_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}i'.format(value_count),
                             fd.read(4 * value_count))
    elif attr_type == AttributeType.I64_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}q'.format(value_count),
                             fd.read(8 * value_count))
    elif attr_type == AttributeType.F16_ARRAY:
        value_count = suint_read(fd)
        print(value_count)
        return struct.unpack('<{}e'.format(value_count),
                             fd.read(2 * value_count))
    elif attr_type == AttributeType.F32_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}f'.format(value_count),
                             fd.read(4 * value_count))
    elif attr_type == AttributeType.F64_ARRAY:
        value_count = suint_read(fd)
        return struct.unpack('<{}d'.format(value_count),
                             fd.read(8 * value_count))
    elif attr_type == AttributeType.STR_ARRAY:
        value_count = suint_read(fd)
        return [str_read(fd) for _ in range(value_count)]

    else:
        raise ValueError("unknown attribute type")


def suint_read(fd: BinaryIO):
    value = int.from_bytes(fd.read(1), BYTE_ORDER)
    if value == MAX_U8:
        value = int.from_bytes(fd.read(2), BYTE_ORDER)
        if value == MAX_U16:
            value = int.from_bytes(fd.read(4), BYTE_ORDER)
            if value == MAX_U32:
                value = int.from_bytes(fd.read(8), BYTE_ORDER)

    return value


def as_suint_bytes(value):
    if value < MAX_U8:
        return value.to_bytes(1, BYTE_ORDER)
    elif value < MAX_U16:
        return bytes((MAX_U8,)) + value.to_bytes(2, BYTE_ORDER)
    elif value < MAX_U32:
        return bytes((MAX_U8, MAX_U8, MAX_U8)) + value.to_bytes(4, BYTE_ORDER)
    elif value < MAX_U64:
        return bytes((MAX_U8, MAX_U8, MAX_U8, MAX_U8, MAX_U8, MAX_U8, MAX_U8)) \
               + value.to_bytes(8, BYTE_ORDER)
    else:
        raise ValueError("invalid shortest uint value")


def suint_write(fd: BinaryIO, value: int):
    fd.write(as_suint_bytes(value))


def as_str_bytes(value: str):
    byte_value = value.encode()
    return as_suint_bytes(len(byte_value)) + byte_value


def str_read(fd: BinaryIO) -> str:
    value_len = suint_read(fd)
    byte_value = fd.read(value_len)
    return byte_value.decode('utf-8')


class Attribute:
    """Named object that store a typed value.

    Examples:
        >>> entity = Entity("my_entity")
        >>> attr = Attribute("my_attr", AttributeType.U8, 42)
        >>> entity.attributes.append(attr)

    Attributes:
        name (str): Attribute name.
        type_ (AttributeType): Attribute type.
        value (Any): Attribute value.
    """

    def __init__(self, name: str, type_: AttributeType, value: Any):
        """Initialize attribute.

        Args:
            name (str): Attribute name.
            type_ (AttributeType): Attribute type.
            value (Any): Attribute value.
        """
        self.name: str = name
        self.type_: AttributeType = type_
        self.value: Any = value


class Entity:
    """Named object that can have children and attributes.

    Examples:
        >>> a = Entity("foo")
        >>> b = Entity("bar")
        >>> a.children.append(b)  # Set "bar" a child of "foo".

    Attributes:
        name (str): Entity name.
        attributes (List[Attribute]): Entity attributes.
        children (List[Enitity]): Entity children.
    """

    def __init__(self, name: str):
        """Initialize entity.

        Args:
            name (str): Entity name.
        """
        self.name = name
        self.attributes: List[Attribute] = []
        self.children: List[Entity] = []


def write_recursive(fd: BinaryIO, entity: Entity):
    """A recursive version of `write`

    Args:
        fd: File object to write in.
        entity: Entity to write.
    """
    fd.write(as_str_bytes(entity.name))

    fd.write(as_suint_bytes(len(entity.attributes)))  # attribute count

    for attr in entity.attributes:
        fd.write(as_str_bytes(attr.name))
        fd.write(attr.type_.to_bytes(1, BYTE_ORDER, signed=False))
        fd.write(as_attr_value_bytes(attr.type_, attr.value))

    fd.write(as_suint_bytes(len(entity.children)))

    for child_entity in entity.children:
        write_recursive(fd, child_entity)


def write(fd: BinaryIO, entity: Entity):
    """Write mug scene to `fd` file object.

    Args:
        fd: File object to write in.
        entity: Root entity to write.
    """
    fd.write(b'MUGS')
    write_recursive(fd, entity)


def read_recursive(fd: BinaryIO):
    """

    Args:
        fd: File object to read from.

    Returns:
        Read entity.
    """
    entity_name = str_read(fd)

    entity = Entity(entity_name)

    attribute_count = suint_read(fd)

    for _ in range(attribute_count):
        attr_name = str_read(fd)
        attr_type = attr_type_read(fd)
        attr_value = attr_value_read(fd, attr_type)

        attr = Attribute(attr_name, attr_type, attr_value)

        entity.attributes.append(attr)

    child_count = suint_read(fd)

    for _ in range(child_count):
        child = read_recursive(fd)

        entity.children.append(child)

    return entity


def read(fd: BinaryIO) -> Entity:
    """Read mug scene from `fd` file object.

    Args:
        fd: File object to read from.

    Returns:
        Root entity.
    """
    if fd.read(4) != b'MUGS':
        raise ValueError("not a valid mug file format")

    return read_recursive(fd)
