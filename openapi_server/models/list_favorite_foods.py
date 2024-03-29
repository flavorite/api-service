# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, EmailStr, Field, validator  # noqa: F401
from fastapi_camelcase import CamelModel
from openapi_server.models.favorite_food import FavoriteFood


class ListFavoriteFoods(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ListFavoriteFoods - a model defined in OpenAPI

        favorite_foods: The favorite_foods of this ListFavoriteFoods.
    """

    favorite_foods: List[FavoriteFood] = Field(alias="favoriteFoods")


ListFavoriteFoods.update_forward_refs()
