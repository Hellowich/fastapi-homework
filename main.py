from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
global_list: List[str] = []

@app.get("/sum1n/{n}")
def sum1n(n: int):
    total = sum(range(1, n + 1))
    return {"result": total}

@app.get("/fibo")
def fibo(n: int):
    def fibonacci(num):
        a, b = 0, 1
        for _ in range(num - 1):
            a, b = b, a + b
        return a
    result = fibonacci(n)
    return {"result": result}

@app.post("/reverse")
def reverse(string: str = Header(...)):
    reversed_string = string[::-1]
    return {"result": reversed_string}

class Item(BaseModel):
    element: str

@app.put("/list")
def add_to_list(item: Item):
    global_list.append(item.element)
    return {"result": "Element added"}

@app.get("/list")
def get_list():
    return {"result": global_list}
class Expression(BaseModel):
    expr: str

@app.post("/calculator")
def calculator(expression: Expression):
    try:
        num1_str, operator, num2_str = expression.expr.split(',')
        num1 = float(num1_str)
        num2 = float(num2_str)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise HTTPException(status_code=403, detail={"error": "zerodiv"})
            result = num1 / num2
        else:
            raise ValueError
        return {"result": result}
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=400, detail={"error": "invalid"})
