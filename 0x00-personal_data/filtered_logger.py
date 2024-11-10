#!/usr/bin/env python3
"""This module provides a function to obfuscate sensitive fields in a log message."""


import re
from typing import List

def filter_datum(fields, redaction, message, separator):
    """
    Replaces values of specified fields with a redaction string in a message.

    Parameters:
    - fields (list): List of field fields to redact.
    - redaction (str): String to replace fields with.
    - message (str): The text message to filter.
    - separator (str): The separator between fields in the message (e.g., ';').

    Returns:
    - str: The filtered message with sensitive data redacted.
    """
    pattern = r'({})=([^{}]+)'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1=' + redaction, message)
