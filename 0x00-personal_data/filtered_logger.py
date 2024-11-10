#!/usr/bin/env python3

import re


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
    # Build regex pattern to match each field
    for field in fields:
        # Match 'field=value' pattern and replace value with redaction
        pattern = f"{field}=[^;{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
