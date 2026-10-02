from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.routes import router
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
app.include_router(router)
