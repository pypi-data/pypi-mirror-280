# pyright: reportUnusedExpression=false
import relationalai as rai
from relationalai.errors import RAIException
import pytest

model = rai.Model(name=globals().get("name", "test_out_of_context"), config=globals().get("config"))
Person = model.Type("Person")

# Raise an error for multiple identity vars
with pytest.raises(RAIException):
    with model.rule():
        p = Person()
        p2 = Person(p, p.name)