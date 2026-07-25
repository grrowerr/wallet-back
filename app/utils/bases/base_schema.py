from marshmallow import Schema, fields


class BaseSchema(Schema):
    class Meta:
        ordered = True

    ref = fields.UUID(
        required=True,
        dump_only=True,
        allow_none=False

    )
    created_at = fields.DateTime(
        required=True,
        dump_only=True,
        allow_none=False
    )
    updated_at = fields.DateTime(
        required=True,
        dump_only=True,
        allow_none=True
    )