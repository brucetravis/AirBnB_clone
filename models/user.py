#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): Users email.
        password (str): Users password.
        first_name (str): Users first name.
        last_name (str): Users last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
