class AppBaseException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class GenericException(AppBaseException):
    def __init__(self, message: str = "Something went wrong"):
        self.message = message
        super().__init__(message=self.message, status_code=403)
