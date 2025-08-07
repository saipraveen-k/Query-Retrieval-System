from fastapi import FastAPI
from app.routes.hackrx import router
from app.routes.webhook import router as webhook_router

app = FastAPI()
app.include_router(router)
