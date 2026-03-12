from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.schema.dto import TwoSum
from app.services.task import TaskService

router = APIRouter()


@cbv(router)
class TaskController:
    repo = TaskService()

    @router.post("/add", response_model=float)
    def add_numbers(self, params: TwoSum) -> float:
        return self.repo.add_numbers(params)

    @router.post("/upper", response_model=str)
    def alter_case(self, param: str) -> str:
        return self.repo.change_case(param)
