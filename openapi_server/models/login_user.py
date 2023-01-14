# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, EmailStr, Field, validator  # noqa: F401
from fastapi_camelcase import CamelModel


class LoginUser(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LoginUser - a model defined in OpenAPI

        email: The email of this LoginUser.
        password: The password of this LoginUser.
    """

    email: str = Field(alias="email")
    password: str = Field(alias="password")


LoginUser.update_forward_refs()
