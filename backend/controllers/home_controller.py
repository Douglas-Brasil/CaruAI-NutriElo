from fastapi.responses import FileResponse
from pathlib import Path
CONTROLLERS_DIR = Path(__file__).resolve().parent
def get_home_page():
    print(f"\033[44m REDIRECIONANDO PRA HOME PAGE \033[0m")
    
    # Subindo de /controllers para /backend (1º ..) e depois para a raiz (2º ..)
    html_path = CONTROLLERS_DIR.parent.parent / "frontend" / "home.html"
    
    return FileResponse(html_path.resolve())