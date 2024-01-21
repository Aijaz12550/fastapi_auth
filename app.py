from distutils.command.config import config
from sys import prefix
from fastapi import FastAPI
from fastapi.routing import APIRoute
from projectInfo import configs
from starlette.middleware.cors import CORSMiddleware
from routes.auth import main as AuthRoute
app = FastAPI(
    title=configs.project_name,
    openapi_url="/openapi.json", # it will return the open api schema in json format,
    docs_url="/v1/docs"
)

# enable cors
app.add_middleware(
    CORSMiddleware,
    allow_origins= configs.cors_origins
)

app.include_router(AuthRoute.router, prefix="/auth")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", port=5000, log_level="info", reload=True)
