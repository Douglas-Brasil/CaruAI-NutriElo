from fastapi import FastAPI
from backend.routes import router
from fastapi.responses import FileResponse

app = FastAPI()

app.include_router(router)