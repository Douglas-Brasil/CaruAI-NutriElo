from fastapi.responses import FileResponse

async def get_home_page():
     
     return FileResponse("frontend/home.html")