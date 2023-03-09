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
The resulting byte-string (27 bytes long):

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/avro_string.png)


Decomposition according to [specification](https://avro.apache.org/docs/1.10.2/spec.html#binary_encoding):

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/avro.png)
