from fastapi import APIRouter

from app.api.v1.endpoints import task

router = APIRouter()

router.include_router(task.router, prefix="/tasks", tags=["tasks"])
