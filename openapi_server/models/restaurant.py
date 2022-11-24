# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Restaurant(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Restaurant - a model defined in OpenAPI

        id: The id of this Restaurant.
        name: The name of this Restaurant.
        longitude: The longitude of this Restaurant.
        latitude: The latitude of this Restaurant.
        address: The address of this Restaurant.
    """

    id: int = Field(alias="id")
    name: str = Field(alias="name")
    longitude: float = Field(alias="longitude")
    latitude: float = Field(alias="latitude")
    address: str = Field(alias="address")

Restaurant.update_forward_refs()
