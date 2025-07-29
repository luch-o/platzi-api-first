from fastapi import FastAPI
import yaml
from pathlib import Path

app = FastAPI()

# Read and load the OpenAPI schema from openapi.yaml
def load_openapi_schema():
    openapi_path = Path(__file__).parent.parent / "openapi.yaml"
    with open(openapi_path, "r") as f:
        return yaml.safe_load(f)

app.openapi_schema = load_openapi_schema()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}