from fastapi import APIRouter, Depends, Request, Response, status, Form
from fastapi.responses import FileResponse, RedirectResponse
from backend.controllers.home_controller import get_home_page
from backend.controllers.login_controller import get_login_page, register_user, login_user
from backend.controllers.auth_controller import Controller_Auth
from backend.models.base_model import UserRegisterSchema

print("\033[42m [BOOT] Arquivo de rotas carregado na memória \033[0m")

router = APIRouter()
auth_controller = Controller_Auth()

def verify_authentication(request: Request) -> bool:
    print("\033[41m [REQUEST] Entrou na verificação de autenticação \033[0m")
    return auth_controller.auth_jwt(request)

@router.get("/")
def home(is_authenticated: bool = Depends(verify_authentication)):
    print(f"\033[44m [REQUEST] Rota Home chamada. Autenticado? {is_authenticated} \033[0m")
    if is_authenticated:
        return get_home_page()
    return RedirectResponse(url="/login", status_code=303)

@router.get("/login")
def login(is_authenticated: bool = Depends(verify_authentication)):
    print(f"\033[44m [REQUEST] Rota Login chamada. Autenticado? {is_authenticated} \033[0m")

    return get_login_page()


@router.post("/register/user")
def register(email: str = Form(...), password: str = Form(...)):
    return register_user(email=email, password=password)



@router.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    print("\033[41m ROTA POST DE LOGAR \033[0m")
    return login_user(email=email, password=password)
