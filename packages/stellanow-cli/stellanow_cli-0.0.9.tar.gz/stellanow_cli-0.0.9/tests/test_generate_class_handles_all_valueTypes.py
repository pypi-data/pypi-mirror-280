"""
Copyright (C) 2022-2024 Stella Technologies (UK) Limited.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""

from datetime import datetime
import pytest
from loguru import logger

from stellanow_cli.core.datatypes import StellaEventDetailed, StellaEntity, StellaField
from stellanow_cli.code_generators import CsharpCodeGenerator


@pytest.fixture
def test_event():
    return StellaEventDetailed(
        id="1",
        name="test_event",
        entities=[
            StellaEntity(id='', name="entity1"),
            StellaEntity(id='', name="entity2"),
        ],
        fields=[
            StellaField(id='', name="field1", fieldType={"value": "Decimal"}, required=True),
            StellaField(id='', name="field2", fieldType={"value": "Integer"}, required=True),
            StellaField(id='', name="fieldValue3", fieldType={"value": "Boolean"}, required=True),
            StellaField(id='', name="field4", fieldType={"value": "String"}, required=True),
            StellaField(id='', name="field5", fieldType={"value": "Date"}, required=True),
            StellaField(id='', name="field6", fieldType={"value": "DateTime"}, required=True),
        ],
        isActive=True,
        createdAt=datetime(2022, 1, 1).strftime("%Y-%m-%dT%H:%M:%S"),
        updatedAt=datetime(2022, 1, 2).strftime("%Y-%m-%dT%H:%M:%S"),
        description="Test event"
    )


def test_generate_class_handles_all_valueTypes(test_event):
    # Generate the class
    generated_class = CsharpCodeGenerator.generate_class(test_event)
    logger.info(generated_class)

    # Assertions
    assert '[property: Newtonsoft.Json.JsonIgnore] string entity1Id,' in generated_class
    assert '[property: Newtonsoft.Json.JsonIgnore] string entity2Id,' in generated_class
    assert '[property: Newtonsoft.Json.JsonProperty("field1")] decimal Field1,' in generated_class
    assert '[property: Newtonsoft.Json.JsonProperty("field2")] int Field2,' in generated_class
    assert '[property: Newtonsoft.Json.JsonProperty("fieldValue3")] bool FieldValue3,' in generated_class
    assert '[property: Newtonsoft.Json.JsonProperty("field4")] string Field4,' in generated_class
    assert '[property: Newtonsoft.Json.JsonProperty("field4")] string Field4,' in generated_class
    assert '[property: Newtonsoft.Json.JsonProperty("field5")] DateOnly Field5,' in generated_class
    assert '[property: Newtonsoft.Json.JsonProperty("field6")] DateTime Field6' in generated_class
    assert ') : StellaNowMessageBase("test_event", new List<EntityType>{ new EntityType("entity1", entity1Id), new EntityType("entity2", entity2Id) });' in generated_class
