from fastapi import FastAPI
from fastapi.routing import APIRoute

app = FastAPI(
    title="Authentication App",
    openapi_url="/openapi.json", # it will return the open api schema in json format,
    docs_url="/v1/docs"
)

# enable cors



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", port=5000, log_level="info", reload=True)
