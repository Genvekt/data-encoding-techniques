# Data encoding techniques
Here are collected popular instruments for data encoding. 

## Structure
In each method-dedicated directory inside 
[this](https://github.com/Genvekt/data-encoding-techniques/tree/main/encoding_techs/encoding_techs) 
folder are:
- `README.md` - full description of method usage in python and its internal structure
- `encode.py` - actual Python code to encode data. There is no decoding, 
because all I needed is binary result to analyse.
- `+` method specific files, including generated ones.

## Method comparison

For each method, I took fairly complex but simple JSON record:
```json
{
    "user_name": "Evgenia",
    "favorite_number": 1337,
    "interests": ["coding", "coffee"]
}
```

The lenth of the result and relative simplicity of usage are crucial factors:

| Method          | Result lenght | Python library only | No extra code generation | Comment                       | Directory |
|-----------------|---------------|---------------------|--------------------------|-------------------------------|-----------|
| JSON string     | 84 bytes      | ✅                    | ✅                        | Tricky data evolution         | [link](https://github.com/Genvekt/data-encoding-techniques/tree/main/encoding_techs/encoding_techs/json_string)  |
| Message Pack    | 63 bytes      | ✅                    | ✅                        | Little win compared with JSON | [link](https://github.com/Genvekt/data-encoding-techniques/tree/main/encoding_techs/encoding_techs/message_pack)         |
| Thrift Binary   | 54 bytes      | ❌                    | ❌                        | Java-like code                | [link](https://github.com/Genvekt/data-encoding-techniques/tree/main/encoding_techs/encoding_techs/apache_thrift)          |
| Thrift Compact  | 29 bytes      | ❌                    | ❌                        | Java-like code                | [link](https://github.com/Genvekt/data-encoding-techniques/tree/main/encoding_techs/encoding_techs/apache_thrift)          |
| Protocol Buffer | 28 bytes      | ❌                    | ❌                        | Cool array structure          | [link](https://github.com/Genvekt/data-encoding-techniques/tree/main/encoding_techs/encoding_techs/protocol_buffer)          |
| Avro            | 27 bytes      | ✅                    | ✅                        | Need writer schema            | [link](https://github.com/Genvekt/data-encoding-techniques/tree/main/encoding_techs/encoding_techs/apache_avro)          |

## Results visualisation

It is helpful to visualise the resulting strings. The following pictures shows 
the ratio of useful data to technical details and unnecessary repetitive parts.

Color distribution is as follows:
- 🟨 - important data we store/send
- 🟥 - structural info, such as chunk length
- 🟪 - method specific info
- 🟩 - unnecessary repetitive part

### JSON string

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/json_string.png)

### Message Pack

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/message_pack_string.png)

### Thrift Binary

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/thrift_binary_string.png)

### Thrift Compact

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/thrift_compact_string.png)

### Protocol Buffer

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/protobuffer_string.png)

### Avro

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/avro_string.png)