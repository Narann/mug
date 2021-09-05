# Mug file format specifications

Little-endian (default for x86 and x86-64).

Extension: .mug

## Primitive format

### Shortest Uint format (Suint)

value = read(u8)
if value == MAX_U8:  # 255
  value = read(u16)
  if value == MAX_U16:  # 65536
    value = read(u32)
    if value == MAX_U32:  # 4294967296
      value = read(u64)

### String format (Str)

Sint: byte_count.
...BYTES...

### AttributeType format (AttrType)

A u8.

* 1,2,3,4,9,16 and N (U6) sized.
* u8-64/i8-64/f16-64/Str


### Attribute format

Str: name.
AttType: attribute type
...ATTRIBUTEVALUE...

### Entity format

Str: name.
Suint: attribute_count.
...ATTRIBUTES...
Suint: child_count.
...ENTITIES...

## File format

u64: Magic number: Mug Scene -> MUGS -> 4D 55 47 53 (55 4D 47 53 in little-endian, 1397183821 as u32).
...ROOT_ENTITY...
