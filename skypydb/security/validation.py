"""
Input validation and sanitization module for Skypydb.
"""

from skypydb.security.constants import (
    TABLE_NAME_PATTERN,
    COLUMN_NAME_PATTERN,
    MAX_TABLE_NAME_LENGTH,
    MAX_COLUMN_NAME_LENGTH,
    MAX_STRING_LENGTH,
    SQL_INJECTION_PATTERNS
)
from skypydb.security.mixins.validation.syscheck import SysCheck
from skypydb.security.mixins.validation.syssanitize import SysSanitize
from skypydb.security.mixins.validation.sysvalidation import SysValidation

class InputValidator(
    SysCheck,
    SysSanitize,
    SysValidation
):
    """
    Validates and sanitizes user inputs to prevent security vulnerabilities.
    """

    # patterns for validation
    TABLE_NAME_PATTERN = TABLE_NAME_PATTERN
    COLUMN_NAME_PATTERN = COLUMN_NAME_PATTERN

    # maximum lengths
    MAX_TABLE_NAME_LENGTH = MAX_TABLE_NAME_LENGTH
    MAX_COLUMN_NAME_LENGTH = MAX_COLUMN_NAME_LENGTH
    MAX_STRING_LENGTH = MAX_STRING_LENGTH

    # SQL injection patterns to detect
    SQL_INJECTION_PATTERNS = SQL_INJECTION_PATTERNS
