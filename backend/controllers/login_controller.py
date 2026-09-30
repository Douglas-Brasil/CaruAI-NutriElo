from fastapi.responses import FileResponse, Response
from fastapi import HTTPException
from backend.models.user import User
from backend.models.login import Login

def get_login_page():
     print(f"\033[44m CARREGANDO PAGINA DE LOGIN[0m")
     return FileResponse("frontend/login.html")


def register_user(email: str, password: str, response: Response):
    # 1. Cria a instância de User
    new_user = User(email=email, password=password)
    
    # 2. Registra o usuário no Supabase
    result = Login.register(new_user)

    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))

    # 3. Se houver sessão (login automático), define o cookie
    if result.get("session"):
        access_token = result["session"].access_token
        
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            max_age=3600,
            samesite="lax"
        )
        return {"status": "ok", "logged_in": True, "message": "Usuário cadastrado com sucesso!"}

    return {"status": "ok", "logged_in": False, "message": "Usuário cadastrado com sucesso!"}