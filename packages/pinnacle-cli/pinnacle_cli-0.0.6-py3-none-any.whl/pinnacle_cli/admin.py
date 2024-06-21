from dotenv import load_dotenv, find_dotenv
import os
from pinnacle_cli.constants import PINNACLE_ADMIN_ENDPOINTS
import requests

load_dotenv(find_dotenv())


org_id = os.getenv("PINNACLE_ORG_ID")
if org_id is None:
    raise Exception("PINNACLE_ORG_ID is not set in the environment variables")

project_id = os.getenv("PINNACLE_PROJECT_ID")
if project_id is None:
    raise Exception("PINNACLE_PROJECT_ID is not set in the environment variables")


def get_lambda_s3_upload_url():
    response = requests.post(
        PINNACLE_ADMIN_ENDPOINTS["upload"],
        json={"org_id": org_id, "project_id": project_id},
        headers={
            "Content-Type": "application/json",
        },
    )
    return response.json()["body"]


def upload_lambda_code(lambda_dist_zip_path: str):
    upload_url = get_lambda_s3_upload_url()

    with open(lambda_dist_zip_path, "rb") as f:
        response = requests.put(upload_url, data=f)
        if response.status_code != 200:
            raise Exception(f"Failed to upload lambda code: {response.text}")


def create_lambda_function():
    response = requests.post(
        PINNACLE_ADMIN_ENDPOINTS["create"],
        json={"org_id": org_id, "project_id": project_id},
        headers={
            "Content-Type": "application/json",
        },
    )
    return response.json()["body"]
