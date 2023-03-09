import avro.schema
import avro.io
import io

if __name__ == "__main__":
    # Generate writer schema
    schema = avro.schema.parse(open("person.avsc", "rb").read())

    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()

    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(
        {
            "user_name": "Evgenia",
            "favorite_number": 1337,
            "interests": ["coding", "coffee"]
        },
        encoder
    )

    raw_bytes = bytes_writer.getvalue()
    print(":".join("{:02x}".format(c) for c in raw_bytes))
    print(len(raw_bytes))
