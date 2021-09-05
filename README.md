# Mug

Mug is a dumb binary hierarchical scene file format.

## Description

`mug` expose two main class, one enum object and two functions:

* `Entity` is a named object that can have children and attributes.
* `Attribute` is a named and typed attributed having a value.
* `AttributeType` is the enum class with attribute type code.
* `read()` and `write()` are respectively use to read and write a mug hierarchy.

## Example

```python3
import mug

root = mug.Entity("foo")
child = mug.Entity("bar")
root.children.append(child)

# Create an attribute named "my_attr" of 1 byte unsigned integer type with a
# value of 42 and set it an attribute of child 
attr = mug.Attribute("my_attr", mug.AttributeType.U8, 42)
child.attributes.append(attr)

# Write the hierarchy and read it.
with open("my_scene.mug", "wb") as fd:
    mug.write(fd, root)
    
with open("my_scene.mug", "wb") as fd:
    root_read = mug.read(fd, root)
```
