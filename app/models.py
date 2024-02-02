from pydantic import BaseModel, constr


class Data(BaseModel):
    phone: str
    address: constr(min_length=1)
