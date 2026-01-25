"""
Type validators for Skypydb schema.
"""

from typing import Any


# main class to validate values
class Validator:
    """
    Base class for type validators.
    """

    def validate(self, value: Any) -> bool:
        """
        Validate a value.

        Args:
            value: Value to validate

        Returns:
            True if value is valid
        """

        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


# main class to validate a string value
class StringValidator(Validator):
    """
    Validator for string values.
    """

    def validate(self, value: Any) -> bool:
        """
        Check if value is a string.
        """

        return isinstance(value, str)

    def __repr__(self) -> str:
        return "v.string()"


# main class to validate a integer value
class Int64Validator(Validator):
    """
    Validator for integer values.
    """

    def validate(self, value: Any) -> bool:
        """
        Check if value is an integer.
        """

        return isinstance(value, int) and not isinstance(value, bool)

    def __repr__(self) -> str:
        return "v.int64()"


# main class to validate a float value
class Float64Validator(Validator):
    """
    Validator for float values.
    """

    def validate(self, value: Any) -> bool:
        """
        Check if value is a float or integer.
        """

        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def __repr__(self) -> str:
        return "v.float64()"


# main class to validate a boolean value
class BooleanValidator(Validator):
    """
    Validator for boolean values.
    """

    def validate(self, value: Any) -> bool:
        """
        Check if value is a boolean.
        """

        return isinstance(value, bool)

    def __repr__(self) -> str:
        return "v.boolean()"


# main class to validate a optional value
class OptionalValidator(Validator):
    """
    Validator for optional values (can be None or the wrapped type).
    """

    def __init__(self, validator: Validator):
        """
        Initialize optional validator.

        Args:
            validator: The validator for the non-null type
        """

        self.validator = validator
        self.optional = True


    def validate(self, value: Any) -> bool:
        """
        Check if value is None or valid according to wrapped validator.
        """

        if value is None:
            return True
        return self.validator.validate(value)


    def __repr__(self) -> str:
        return f"v.optional({self.validator})"


# main class for creating type validators
class Values:
    """
    Factory for creating type validators.
    """


    # create a string validator
    @staticmethod
    def string() -> Validator:
        """
        Create a string validator.
        """

        return StringValidator()


    # create an integer validator
    @staticmethod
    def int64() -> Validator:
        """
        Create an integer validator.
        """

        return Int64Validator()


    # create a float validator
    @staticmethod
    def float64() -> Validator:
        """
        Create a float validator.
        """

        return Float64Validator()


    # create a boolean validator
    @staticmethod
    def boolean() -> Validator:
        """
        Create a boolean validator.
        """

        return BooleanValidator()


    # create an optional validator
    @staticmethod
    def optional(validator: Validator) -> Validator:
        """
        Create an optional validator.

        Args:
            validator: The validator to make optional

        Returns:
            An optional validator
        """

        return OptionalValidator(validator)


# Create singleton instance for easy import
v = Values()
