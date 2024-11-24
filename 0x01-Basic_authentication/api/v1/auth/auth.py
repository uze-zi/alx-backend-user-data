#!/urs/bin/env python3
"""
Auth
This module contains the Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage API authentication

    public methods:
      - require_auth
      - authorization_header
      - current_user
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method must be slash tolerant: path=/api/v1/status
        and path=/api/v1/status/ must be returned False
        if excluded_paths contains /api/v1/status/

        It determines if a given path requires authentication.
        assuming excluded_paths contains strings always ending by a '/'

        Args:
            path (str): The path to the resource
            excluded_paths (List[str]): A list of paths that
            do not require authentication

        Returns True if the path is not in the excluded_paths list
        True if path is None
        True if excluded_paths is None
        False if path is in the excluded_paths
        """
        if path is None or excluded_paths is None:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

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
