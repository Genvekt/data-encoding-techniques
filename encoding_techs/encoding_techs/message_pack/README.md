
# MessagePack 
The way to encode JSON into binary string [[Spec]](https://msgpack.org)


## Installation
In Python, `msgpack` library provides the necessary functionality:

```pip install msgpack```


## Encoding

JSON to encode:
```json
{
  "user_name": "Evgenia",
  "favourite_number": 1337,
  "interests": ["coding", "coffee"]
}
```

#### Encoding process:
```python
import msgpack
person = {
  "user_name": "Evgenia",
  "favourite_number": 1337,
  "interests": ["coding", "coffee"]
}
result = msgpack.dumps(person)
```

#### Binary string analysis
The result of encoding is next 63 bytes long sequence:

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/message_pack_string.png)

Decomposition according to [specification](https://github.com/msgpack/msgpack/blob/master/spec.md#map-format-family):

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/message_pack.png)
