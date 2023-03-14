import capnp


capnp.remove_import_hook()
person_schema = capnp.load('person.capnp')


if __name__ == "__main__":
    person = person_schema.Person.new_message(
        userName="Evgenia",
        favoriteNumber=1337
    )

    interests = person.init("interests", 2)
    interests[0] = "coding"
    interests[1] = "coffee"

    result = person.to_bytes()

    print(":".join("{:02x}".format(c) for c in result))
    print(len(result))

    result = person.to_bytes_packed()

    print(":".join("{:02x}".format(c) for c in result))
    print(len(result))