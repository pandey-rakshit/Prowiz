from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.v1.router import router as v1_router
from app.core.exceptions.generic import AppBaseException
from app.core.exceptions.handler import app_exception_handler, validation_exception_handler

app = FastAPI(
    title="Task 3 | Fast API",
    version="1.0.0",
    description="""Write a python code to create the following API using fastAPI
                <br> a) To accept 2 numbers and return their sum.
                Ensure the API is able to give proper error value when string is entered in place of numbers
                <br> b) To accept lower case string and return the string in all capital letters""",
)


app.add_exception_handler(AppBaseException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
