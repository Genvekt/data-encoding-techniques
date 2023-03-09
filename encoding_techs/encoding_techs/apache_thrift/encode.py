from encoding_techs.apache_thrift.gen_py.person.ttypes import Person
from thrift.protocol import TBinaryProtocol, TCompactProtocol
from thrift.transport import TTransport

if __name__ == "__main__":
    person = Person(
        user_name="Evgenia",
        favorite_number=1337,
        interests=["coding", "coffee"]
    )

    trans = TTransport.TMemoryBuffer()
    protocol = TBinaryProtocol.TBinaryProtocol(trans)
    person.write(protocol)
    encoded_list = trans.getvalue()
    print("Binary protocol:")
    print(":".join("{:02x}".format(c) for c in encoded_list))

    print(len(":".join("{:02x}".format(c) for c in encoded_list).split(":")))

    trans = TTransport.TMemoryBuffer()
    protocol = TCompactProtocol.TCompactProtocol(trans)
    person.write(protocol)
    encoded_list = trans.getvalue()

    print("Compact protocol:")
    print(":".join("{:02x}".format(c) for c in encoded_list))

    print(len(":".join("{:02x}".format(c) for c in encoded_list).split(":")))
