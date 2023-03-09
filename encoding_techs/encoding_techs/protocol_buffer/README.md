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

Result is the next byte-string in hex format:
```
0a:07:45:76:67:65:6e:69:61:10:b9:0a:1a:06:63:6f:64:69:6e:67:1a:06:63:6f:66:66:65:65
```

## Analysis

The resulting byte-string is 28 bytes long. It can be translated the next way:
```
0a                   -> [ 00001 | 010 ]  (tag 1, type 2 (str)) 
07                   -> [ 0000 0111 ] (len 7)
45:76:67:65:6e:69:61 -> Evgenia in ASCII
10                   -> [ 00010 | 000 ] (tag 2, type 0 (varint))
b9:0a                -> [ 1|011 1001 || 0|000 1010 ] -> [011 1001 || 000 1010] -> [ 000 1010 011 1001] -> 1337
1a                   -> [00011 | 010 ] (tag 3, type 2 (str))
06                   -> [ 0000 0110 ] (len 6)
63:6f:64:69:6e:67    -> coding in ASCII
1a                   -> [00011 | 010 ] (tag 3, type 2 (str))
06                   -> [ 0000 0110 ] (len 6)
63:6f:66:66:65:65    -> coffee in ASCII
```

Data is meaningful only with schema, which maps tags into actual field names.