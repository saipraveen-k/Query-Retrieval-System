from fastapi import FastAPI
from app.routes.hackrx import router

app = FastAPI()
app.include_router(router)
