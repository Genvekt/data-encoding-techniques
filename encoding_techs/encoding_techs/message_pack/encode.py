import json
import msgpack

if __name__ == "__main__":
    person = {
        "user_name": "Evgenia",
        "favorite_number": 1337,
        "interests": ["coding", "coffee"]
    }

    result = msgpack.dumps(person)

    print(" ".join("{:02x}".format(c) for c in result))