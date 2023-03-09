import json
import msgpack

if __name__ == "__main__":
    person = {
        "user_name": "Evgenia",
        "favourite_number": 1337,
        "interests": ["coding", "coffee"]
    }

    binary_str = msgpack.dumps(person)

    print(":".join("{:02x}".format(c) for c in binary_str))