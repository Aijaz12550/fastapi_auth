from pydantic import BaseModel

class RegisterRequestData(BaseModel):
    name: str
    email: str
    password: str
