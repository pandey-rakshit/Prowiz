from pydantic import BaseModel, ConfigDict


class TwoSum(BaseModel):
    model_config = ConfigDict(strict=True)
    num1: float
    num2: float
