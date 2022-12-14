# coding: utf-8

"""
    Flavorite - OpenAPI 3.0

    This is a Flavorite Server based on the OpenAPI 3.0 specification. 

    The version of the OpenAPI document: 1.1.2
    Generated by: https://openapi-generator.tech
"""

import os
import typing
import time

from httpx import AsyncClient
from httpx import Response

from fastapi import FastAPI, APIRouter

from openapi_server.apis.restaurants_api import router as RestaurantsApiRouter
from openapi_server.apis.reviews_api import router as ReviewsApiRouter
from openapi_server.apis.users_api import router as UsersApiRouter
from openapi_server.orms.dynamodb_setup import dynamodb_setup

app = FastAPI(
    title="Flavorite - OpenAPI 3.0",
    description="This is a Flavorite Server based on the OpenAPI 3.0 specification. ",
    version="1.1.2",
)
top_router = APIRouter(prefix="/api")
sub_router = APIRouter(prefix="/v1")

sub_router.include_router(RestaurantsApiRouter)
sub_router.include_router(ReviewsApiRouter)
sub_router.include_router(UsersApiRouter)

top_router.include_router(sub_router)
app.include_router(top_router)


# function to check if localstack server is accessible
async def is_localstack():
    async with AsyncClient(base_url=os.environ.get("AWS_DYNAMODB_HOST")) as ac:
        await ac.get("")


# function to get status of localstack server "ready" stage
async def localstack_status() -> typing.Dict[str, typing.Any]:
    async with AsyncClient(base_url=os.environ.get("AWS_DYNAMODB_HOST")) as ac:
        response: Response = await ac.get("/_localstack/init/ready")
    return response.json()


@app.on_event("startup")
async def startup_event():
    # loop to ping localstack server
    while True:
        try:
            await is_localstack()
            break
        # catch errors
        except Exception as e:
            time.sleep(2)  # try again after 2s
    # loop to refresh server stage completion status
    while True:
        status: typing.Dict[str, typing.Any] = await localstack_status()
        if status["completed"]:
            break
        else:
            time.sleep(2)  # try again after 2s
    dynamodb_setup()  # init dynamodb
