#!/usr/bin/env python3
"""
filtered logging
"""

import re

def filter_datum(fields, redaction, message, separator):
    """
    Filters a log message by obfuscating certain field values.

    Args:
        fields: A list of strings representing all fields to obfuscate.
        redaction: A string representing by what the field will be obfuscated.
        message: A string representing the log line.
        separator: A string representing by which character is separating all fields in the log line (message).

    Returns:
        A string representing the obfuscated log line.
    """

    # Create a regex pattern to match all occurrences of the fields to be obfuscated.
    regex_pattern = r'(?P<field>{})=[^{}]+{}'.format('|'.join(fields), separator, separator)

    # Replace all occurrences of the fields to be obfuscated with the redaction string.
    obfuscated_message = re.sub(regex_pattern, r'\g<field>={}{}'.format(redaction, separator), message)

    return obfuscated_message
