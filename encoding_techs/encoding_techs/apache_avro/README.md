# Apache Avro
Encoding protocol for Hadoop

## Installing
No need for installing specific driver, just python library:
```bash
pip install avro
```

## Encoding
Avro uses JSON schema specification, that can be written into .avsc file. 
Field types are defined in schema as well, so encoded string contains only values and
meaningful only with reading schema.

1. Person schema we want will be defined as next person.avsc file in JSON style:
```
{
    "type": "record",
    "name": "Person",
    "fields": [
        {"name": "user_name", "type": "string"},
        {"name": "favorite_number",  "type": ["int", "null"]},
        {"name": "interests", "type": {"type": "array", "items": "string"}}
    ]
}
```

2. Schema may be then used inside python code to encode data:

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
