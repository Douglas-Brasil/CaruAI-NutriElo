from fastapi.responses import FileResponse, Response, RedirectResponse
from fastapi import HTTPException
from backend.models.user import User
from backend.models.login import Login

def get_login_page():
    print(f"\033[44m CARREGANDO PAGINA DE LOGIN[0m")
    return FileResponse("frontend/login.html")

def register_user(email: str, password: str) -> RedirectResponse:
    new_user = User(email=email, password=password)
    result = Login.register(new_user)

    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))

    # Instancia o redirecionamento
    response = RedirectResponse(url="/", status_code=303)

    # Define o cookie caso haja sessão no cadastro (auto-login)
    if result.get("session"):
        print("\033[41m CRIOU O USUARIO \033[0m")
        access_token = result["session"].access_token
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            max_age=3600,
            samesite="lax",
            secure=True
        )

    return response


def login_user(email: str, password: str) -> RedirectResponse:
    # 1. Tenta autenticar o usuário no Supabase
    user = User(email=email, password=password)
    result = Login.authenticate(user)  # Ajuste o método conforme sua classe Login

    if not result.get("success"):
        raise HTTPException(
            status_code=400, 
            detail=result.get("error", "Credenciais inválidas.")
        )

    # 2. Cria a resposta de redirecionamento
    response = RedirectResponse(url="/", status_code=303)
    print("\033[41m LOGOU O USUARIO \033[0m")
    # 3. Define o cookie de acesso na resposta de redirecionamento
    access_token = result.get("session").access_token
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=3600,
        samesite="lax",
        secure=True  # Recomendado em produção com HTTPS
    )

    return response