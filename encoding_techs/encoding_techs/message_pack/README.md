
# MessagePack 
The way to encode JSON into binary string [[Spec]](https://msgpack.org)


## Installation
In Python, `msgpack` library provides the necessary functionality:

```pip install msgpack```


## Encoding

JSON to encode:
```json
person = {
  "user_name": "Evgenia",
  "favourite_number": 1337,
  "interests": ["coding", "coffee"]
}
```

#### Encoding process:
```python
import msgpack
result = msgpack.dumps(person)
```

#### Binary string analysis
The result of encoding is next binary string (in hex format):

```
83:a9:75:73:65:72:5f:6e:61:6d:65:a7:45:76:67:65:6e:69:61:b0:66:61:76:6f:75:72:69:74:65:5f:6e:75:6d:62:65:72:cd:05:39:a9:69:6e:74:65:72:65:73:74:73:92:a6:63:6f:64:69:6e:67:a6:63:6f:66:66:65:65
```
The string is 64 bytes long. It translates in the next way, according to [specification](https://github.com/msgpack/msgpack/blob/master/spec.md#map-format-family):

```
83 - fixmap type
a9 - fixstr len 9
75:73:65:72:5f:6e:61:6d:65 - user_name in ASCII
a7 - fixstr len 7
45:76:67:65:6e:69:61 - Evgenia in ASCII
b0 - fixstr len 16
66:61:76:6f:75:72:69:74:65:5f:6e:75:6d:62:65:72 - favourite_number in ASCII
cd - uint 16 ( 2 bytes )
05:39 - 1337 base 2
a9 - fixstr len 9
69:6e:74:65:72:65:73:74:73 - interests in ASCII
92 - fixarray len 2
a6 - fixstr len 6
63:6f:64:69:6e:67 - coding in ASCII
a6 - fixstr len 6 
63:6f:66:66:65:65 - coffee in ASCII
```