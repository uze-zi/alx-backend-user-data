#!/urs/bin/env python3
""" Module of Auth
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage the API authentication

    public methods:
      - require_auth
      - authorization_header
      - current_user
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from a request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        """
        return None

