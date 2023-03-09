# Apache Avro
Encoding protocol for Hadoop

## Installing
No need for installing specific driver, just python library:
```bash
pip install avro
```

## Encoding
Avro uses special .avsc files for schema specification. Field types are defined in schema as well,
so encoded string contains only value.

1. Person schema we want will be defined as next person.avsc file in JSON style:
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
import avro.schema
import avro.io
import io

schema = avro.schema.parse(open("person.avsc", "rb").read())

writer = avro.io.DatumWriter(schema)
bytes_writer = io.BytesIO()

encoder = avro.io.BinaryEncoder(bytes_writer)
writer.write(
    {
        "user_name": "Evgenia",
        "favorite_number": 1337,
        "interests": ["coding", "coffee"]
    },
    encoder
)
result = bytes_writer.getvalue()
```
The resulting byte-string:
```
0e:45:76:67:65:6e:69:61:00:f2:14:04:0c:63:6f:64:69:6e:67:0c:63:6f:66:66:65:65:00
```

It is 27 bytes long and translates as follows according to [specification](https://avro.apache.org/docs/1.10.2/spec.html#binary_encoding)

```
0e - [0 0001110] -> [1110] -> 7 len (Zigzag notation)
      ^ 
  this is the last byte of varint
45:76:67:65:6e:69:61 - Evgenia in ASCII
00 - 0th type in union specification (int according to out schema)
f2:14 - [1 1110010 | 0 0010100] -> [00101001110010] -> 1337 (ZigZag notation)
04 - [0 0000100] -> [100] -> 2 len (Zigzag notation)
0c - [0 0001100] -> [1100] -> 6 len (Zigzag notation)
63:6f:64:69:6e:67 - coding in ASCII
0c - [0 0001100] -> [1100] -> 6 len (Zigzag notation)
63:6f:66:66:65:65 - coffee in ASCII
00 - end of array
```