import scalify
from pydantic import BaseModel


class FooModel(BaseModel):
    identifier: str
    name: str


class BarModel(BaseModel):
    id: int
    first_name: str
    last_name: str


bar = scalify.cast(FooModel(identifier="42", name="Scalify Robot"), BarModel)

assert bar.model_dump() == {"id": 42, "first_name": "Scalify", "last_name": "Robot"}
