import logging

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Action(BaseModel):
    action: str | None = None


@app.post("/check")
def check(query: Action):
    # do something with query
    print("query:", query)
    return "success"


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
