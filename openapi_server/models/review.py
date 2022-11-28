# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Review(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Review - a model defined in OpenAPI

        id: The id of this Review.
        user_id: The user_id of this Review.
        restaurant_id: The restaurant_id of this Review.
        rating: The rating of this Review.
        content: The content of this Review [Optional].
        photo_url: The photo_url of this Review [Optional].
    """

    id: int = Field(alias="id")
    user_id: int = Field(alias="userId")
    restaurant_id: int = Field(alias="restaurantId")
    rating: int = Field(alias="rating")
    content: Optional[str] = Field(alias="content", default=None)
    photo_url: Optional[str] = Field(alias="photoUrl", default=None)


Review.update_forward_refs()
