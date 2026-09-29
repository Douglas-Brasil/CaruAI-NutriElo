from .connection_database import *

class AuthSupaBase():
     def authenticate_user_db(user: User):
          try:
               response = supabase.auth.sign_in_with_password({
                    "email": user.email,
                    "password": user.password
               })

               # Retorna os dados do usuário junto do token JWT criado
               return {
                    "success": True,
                    "user": response.user,
                    "email": response.user.email,
                    "id": response.user.id,
                    "session": response.session
               }

          except Exception as e:
               print(f"\033[41mErro ao fazer login: {e}\033[0m")
               return {
                    "success": False,
                    "error": str(e)
               }