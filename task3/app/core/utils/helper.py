from app.core.exceptions.generic import GenericException


def errorIf(condition: bool, message: str):
    if condition:
        raise GenericException(message)
