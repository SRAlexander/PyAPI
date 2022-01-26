from marshmallow import Schema, fields, ValidationError, pre_load

class TestDefinitionSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()