import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Action(BaseModel):
    action: str | None = None


@app.post("/check")
async def create_item(request: Request):
    data = await request.json()
    # 判断data是否包含action字段
    if "action" in data and data["action"] == "CheckContainerPath":
        return "success"
    else:
        print("query:", data)
        return data


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
