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
    print("query:", data)
    # 判断data是否包含action字段
    if "action" in data and data["action"] == "CheckContainerPath":
        return "success"
    else:
        response = {
            "ToUserName": "用户OPENID",
            "FromUserName": "公众号/小程序原始ID",
            "CreateTime": "发送时间",
            "MsgType": "text",
            "Content": "文本消息"
        }
        # 将Python对象转换为JSON字符串
        json_string = json.dumps(response)
        print(json_string)
        return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
