# Apache Thrift
Data encoding instrument from Facebook. Uses schema definition files to get rid of field names.

## Installing
Thrift driver for MacOS to generate python code:
```bash
brew install thrift
```
Other guides [here](https://thrift.apache.org).

To use in python:
```bash
pip install thrift
```

## Encoding
To encode data in Python, special code must be generated from .thrift schema specification file.

1. Person schema we want will be defined as next person.thrift file:
```
struct Person {
    1: required string user_name,
    2: optional i64 favorite_number,
    3: optional list<string> interests
}
```
2. Special .py files must be generated from defined person.thrift with next command (from current dir):
```bash
thrift -r --gen py person.thrift 
```

3. `Person` class then can be imported from resulted `gen-py/person/ttypes.py`. Rename `gen-py` to smth like `gen_py`, otherwise import brakes)))

### BinaryProtocol

```python
from gen_py.person.ttypes import Person
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

person = Person(
    user_name="Evgenia",
    favorite_number=1337,
    interests=["coding", "coffee"]
)

trans = TTransport.TMemoryBuffer()
protocol = TBinaryProtocol.TBinaryProtocol(trans)
person.write(protocol)
result = trans.getvalue()
```

Result is the next 54 byte sequence in hex format:

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/thrift_binary_string.png)

Decomposition according to [specification](https://github.com/apache/thrift/blob/master/doc/specs/thrift-binary-protocol.md):

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/thrift_binary.png)

### CompactProtocol
```python
from gen_py.person.ttypes import Person
from thrift.protocol import TCompactProtocol
from thrift.transport import TTransport

person = Person(
    user_name="Evgenia",
    favorite_number=1337,
    interests=["coding", "coffee"]
)

trans = TTransport.TMemoryBuffer()
protocol = TCompactProtocol.TCompactProtocol(trans)
person.write(protocol)
result = trans.getvalue()
```
Result is the next 29 bytes sequence in hex format:

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/thrift_compact_string.png)

Decomposition according to the [specification](https://github.com/apache/thrift/blob/master/doc/specs/thrift-compact-protocol.md):

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/thrift_compact.png)

