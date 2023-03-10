import json

if __name__ == "__main__":
    person = {
        "user_name": "Evgenia",
        "favorite_number": 1337,
        "interests": ["coding", "coffee"]
    }
    result = json.dumps(person).encode("utf-8")
    print(result)

    print(" ".join("{:02x}".format(c) for c in result))
    print(len(result))
