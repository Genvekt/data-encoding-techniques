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
Result is the next byte-string in hex format:

```
18:07:45:76:67:65:6e:69:61:16:f2:14:19:28:06:63:6f:64:69:6e:67:06:63:6f:66:66:65:65:00
```
It translates the following way according to the [specification](https://github.com/apache/thrift/blob/master/doc/specs/thrift-compact-protocol.md):
```
18 -> [0001 | 1000] - tag 1, type 8 (string)
07 -> len 7
45:76:67:65:6e:69:61 -> Evgenia in ASCII
16 -> [0001 | 0110] - tag 2 (+1), type 6 (i64)
f2:14 -> [1 111001 0 |  0 0010100] -> [111001 | 0010100] -> [0010100 111001] -> 1337 in binary
          ^        ^    ^
  next not end   sign  this is the last
 
19 -> [0001 | 1001] - tag 3 (+1), type 9 (list)
28 -> [0010 | 1000] - len 2, item type 8 (string)
06 - len 6
63:6f:64:69:6e:67 - coding in ASCII
06 - len 6
63:6f:66:66:65:65 - coffee in ASCII
00 - struct end
```
29 bytes long
