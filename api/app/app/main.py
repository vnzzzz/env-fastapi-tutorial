# fastapiのインポート
from fastapi import FastAPI

# モジュールのインポート
from .routers import users
from .routers import items
from .routers import files

# fastapiインスタンスを生成
app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(files.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
