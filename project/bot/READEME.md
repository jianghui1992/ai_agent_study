
服务器端：接口 -》langchain-》openai\ollama。。
客户端：电报机器人、微信机器人、website。
接口：http,https,websocket

# 服务器接口
1. 接口访问，python选型fastapi  
2. /chat的接口，post请求
3. /add_urls 从url中学习知识
4. /add_pdfs 从pdf里学习知识
5. /add_texts 从txt文本里学习

# 人性化
1. 用户输入 -> AI判断一下当前问题的情绪倾向->添加到prompt中->调用agent 
2. 工具调用： 用户发起请求->agent判断使用哪个工具->带着相关的参数去请求工具 -> 得到观察结果

## 截止目前：
1. api
2. angent框架
3. tools:搜索、查询信息、专业知识库
4. 记忆，长时记忆
5. 学习能力

## 从url来学习，实现增强
1. 输入URL
2. 地址的HTML变成文本
3. 向量化
4. 检索出相关文本块做为prompt中的上下文内容
5. LLM回答
