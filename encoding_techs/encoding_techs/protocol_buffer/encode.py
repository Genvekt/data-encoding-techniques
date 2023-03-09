from encoding_techs.protocol_buffer import person_pb2


if __name__ == "__main__":
    person = person_pb2.Person()
    person.user_name = "Evgenia"
    person.favorite_number = 1337
    person.interests.extend(["coding", "coffee"])

    result = person.SerializeToString()
    print(":".join("{:02x}".format(c) for c in result))
