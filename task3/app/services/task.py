from app.core.utils.helper import errorIf
from app.schema.dto import TwoSum


class TaskService:

    def add_numbers(self, params: TwoSum):
        num1 = params.num1
        num2 = params.num2
        return num1 + num2

    def _is_lower(self, param: str) -> bool:
        return not param.islower()

    def change_case(self, param: str) -> str:
        errorIf(self._is_lower(param), "Input String is not in lowercase")
        return param.upper()
