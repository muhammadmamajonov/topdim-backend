from pydantic import BaseModel


class IDNameSchema(BaseModel):
    id: int
    name: str
