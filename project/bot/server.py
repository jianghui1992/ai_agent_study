import time

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Request
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/check")
async def create_item(request: Request):
    data = await request.json()
    print("收到消息:", data)
    # 判断data是否包含action字段
    if "action" in data and data["action"] == "CheckContainerPath":
        return "success"
    else:

        response = {
            "ToUserName": data["FromUserName"],
            "FromUserName": data["ToUserName"],
            "CreateTime": int(round(time.time())),
            "MsgType": "text",
            "Content": "收到了," + data["Content"]
        }
        # 将Python对象转换为JSON字符串
        json_string = json.dumps(response, ensure_ascii=False).encode('utf-8').decode()
        print("响应结果:", json_string)
        return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
