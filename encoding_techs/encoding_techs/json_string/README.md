# JSON string

Json is a textual format for data transfer and storage. 

## Encoding 

To send the following JSON over network, it may be encoded into byte-string characterwise.

```json
{
    "user_name": "Evgenia",
    "favorite_number": 1337,
    "interests": ["coding", "coffee"]
}
```

Python code for encoding is short:

```python
import json

person = {
    "user_name": "Evgenia",
    "favorite_number": 1337,
    "interests": ["coding", "coffee"]
}
result = json.dumps(person).encode("utf-8")
```

As the result, the JSON above encodes as 84 bytes sequence:

![](https://raw.githubusercontent.com/Genvekt/data-encoding-techniques/main/images/json_string.png)

Noticeable, how useful information (yellow) owercrouded with repetitive info (purple and green)
