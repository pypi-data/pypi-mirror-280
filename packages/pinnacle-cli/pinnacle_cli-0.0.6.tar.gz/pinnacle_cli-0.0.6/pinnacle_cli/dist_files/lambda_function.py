# This file is used to generate the lambda function that will be deployed to AWS Lambda. It is attached to each
# Lambda function zip file and is the entry point for the Lambda function.
from mangum import Mangum
import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from pydantic import create_model
from typing import Any
from fastapi import Depends
from typing import get_type_hints
from fastapi.middleware.cors import CORSMiddleware
from pinnacle_cli.py.import_modules import import_modules

load_dotenv(find_dotenv())
import_modules()
from pinnacle_python.endpoints import endpoints

org_id = os.getenv("PINNACLE_ORG_ID")
project_id = os.getenv("PINNACLE_PROJECT_ID")

app = FastAPI(
    root_path=f"/prod/{org_id}/{project_id}",
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def generate_model_from_function(func):
    annotations = get_type_hints(func)
    return_type = annotations.pop("return", Any)
    fields = {key: (value, ...) for key, value in annotations.items()}

    return return_type, create_model(f"Model_{func.__name__}", **fields)  # type: ignore


def route_factory(http_method, endpoint):
    route_name = endpoint.__name__
    params = endpoint.__annotations__.items()
    RouteReturnType, RouteModel = generate_model_from_function(endpoint)

    @app.api_route(f"/{route_name}", methods=[http_method])
    async def route_handler(data: RouteModel = (Depends() if http_method == "GET" else None)) -> RouteReturnType:  # type: ignore
        if data == None:
            return endpoint()
        return endpoint(**data.dict())

    return (route_name, params)


for http_method, endpoints in endpoints.items():
    for endpoint in endpoints:
        route_name, params = route_factory(http_method, endpoint)

lambda_handler = Mangum(
    app,
)
