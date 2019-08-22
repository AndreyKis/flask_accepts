from marshmallow import Schema, fields as ma
from flask import Flask
from flask_restplus import Resource, Api, fields as fr

from .utils import unpack_list, unpack_nested


def test_unpack_list():
    app = Flask(__name__)
    api = Api(app)
    result = unpack_list(ma.List(ma.Integer()), api=api)

    assert result


def test_unpack_nested():
    app = Flask(__name__)
    api = Api(app)
    result = unpack_nested(ma.Nested(ma.Integer()), api=api)

    assert result


def test__default_model_name():
    from .utils import _default_model_name

    class TestSchema(Schema):
        pass

    result = _default_model_name(TestSchema)

    expected = "Test"
    assert result == expected


def test__default_model_name_works_with_multiple_schema_in_name():
    from .utils import _default_model_name

    class TestSchemaSchema(Schema):
        pass

    result = _default_model_name(TestSchemaSchema)

    expected = "TestSchema"
    assert result == expected


def test__default_model_name_that_does_not_end_in_schema():
    from .utils import _default_model_name

    class SomeOtherName(Schema):
        pass

    result = _default_model_name(SomeOtherName)

    expected = "SomeOtherName"
    assert result == expected
