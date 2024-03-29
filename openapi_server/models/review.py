# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, EmailStr, Field, validator  # noqa: F401
from fastapi_camelcase import CamelModel
from openapi_server.models.restaurant import Restaurant
from openapi_server.models.user import User


class Review(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Review - a model defined in OpenAPI

        id: The id of this Review.
        user: The user of this Review.
        restaurant: The restaurant of this Review.
        rating: The rating of this Review.
        content: The content of this Review [Optional].
        photo_url: The photo_url of this Review [Optional].
        favorite_food: The favorite_food of this Review.
        starred: The starred of this Review.
        created_at: The created_at of this Review.
        updated_at: The updated_at of this Review.
    """

    id: str = Field(alias="id")
    user: User = Field(alias="user")
    restaurant: Restaurant = Field(alias="restaurant")
    rating: int = Field(alias="rating")
    content: Optional[str] = Field(alias="content", default=None)
    photo_url: Optional[str] = Field(alias="photoUrl", default=None)
    favorite_food: str = Field(alias="favoriteFood")
    starred: bool = Field(alias="starred")
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")


Review.update_forward_refs()
