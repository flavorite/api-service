# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, EmailStr, Field, validator  # noqa: F401
from fastapi_camelcase import CamelModel


class CreateUser(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateUser - a model defined in OpenAPI

        username: The username of this CreateUser.
        first_name: The first_name of this CreateUser.
        last_name: The last_name of this CreateUser.
        email: The email of this CreateUser.
        password: The password of this CreateUser.
    """

    username: str = Field(alias="username")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str = Field(alias="email")
    password: str = Field(alias="password")


CreateUser.update_forward_refs()
