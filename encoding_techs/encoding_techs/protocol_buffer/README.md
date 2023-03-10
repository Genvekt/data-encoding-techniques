# Protocol Buffer
Data encoding format from Google. 
It uses schema specification files to emit field names and shrink down the size of result. 

## Installing
For MacOS:
```bash
brew install protobuf
```
Other guides [here](https://github.com/protocolbuffers/protobuf).

## Encoding
To encode data in Python, special code must be generated from .proto schema specification file.

1. Person schema we want will be defined as next person.proto file:
```protobuf
syntax = "proto3";

message Person {
  string user_name = 1;
  optional int64 favorite_number = 2;
  repeated string interests = 3;
}
```
2. Special .py file must be generated from defined person.proto with next command (from current dir):
```bash
protoc -I=. --python_out=. ./person.proto
```
3. `Person` class then can be imported from resulted `person_pb2.py`. 
It is not present there, but will be in runtime:

```python
import person_pb2
person = person_pb2.Person()  # may be highlighted as not defined, it is ok
person.user_name = "Evgenia"
person.favorite_number = 1337
person.interests.extend(["coding", "coffee"])

result = person.SerializeToString()
```

Result is the following 28 bytes sequence in hex format:

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/protobuffer_string.png)

Decomposition according to [specification]():

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/protobuffer.png)

Data is meaningful only with schema, which maps tags into actual field names.