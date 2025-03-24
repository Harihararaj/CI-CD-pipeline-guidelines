from fastapi import FastAPI
from src.business_logic import add, subtract

app = FastAPI()


@app.get("/")
def read_root():
    print('Test runs')
    return {"message": "Hello, FastAPI!"}


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": add(a, b)}


@app.get("/subtract/{a}/{b}")
def subtract_numbers(a: int, b: int):
    return {"result": subtract(a, b)}
