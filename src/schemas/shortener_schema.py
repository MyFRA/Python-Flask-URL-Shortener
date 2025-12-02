from marshmallow import Schema, fields

class ShortenerSchema(Schema):
    url = fields.URL(
        required=True,
    )