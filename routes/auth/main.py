from fastapi import APIRouter
from dataModels.pydantic.auth import RegisterRequestData
from utils.jwt import generateToken

router = APIRouter()

@router.post("/login")
def login(email:str, password:str):
    print("hello", email, password)

    return {}


@router.post("/register" )
def register(data:RegisterRequestData):
    
    token = generateToken(data.__dict__)
    return {"token": token}