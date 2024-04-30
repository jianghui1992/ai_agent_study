import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/check")
def check():
    # do something with query
    # print("query:", query)
    return "success"


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
