from typing import Union
from fastapi import FastAPI
from routes.userRoutes import userRouter
from routes.chat_routes import router as chat_router
# from configs.langchain_config import model

app = FastAPI()

# reply = model.invoke("Hello, world!")
# print(reply)
app.include_router(userRouter, prefix="/api/user", tags=["user"])
app.include_router(chat_router, prefix="/api/chat", tags=["chat"])
@app.get("/")
def read_root():
    return {"Hello": "World"}