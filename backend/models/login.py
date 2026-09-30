from backend.models.user import User
from .connection_database import supabase  # Certifique-se de que a instância do Supabase é importada daqui

# backend/models/login.py
class Login:
     @staticmethod
     def register(user: User) -> dict:
          try:
               response = supabase.auth.sign_up({
                    "email": user.get_email(),
                    "password": user.get_password()
               })

               if response.user:
                    print(f"\033[44m CRIOU USER \033[0m")
                    
                    return {
                    "success": True,
                    "user": response.user,
                    "session": response.session,  # Pode ser None se o e-mail exigir confirmação
                    "message": "Usuário cadastrado com sucesso!"
                    }
               

               return {"success": False, "error": "Não foi possível criar o usuário."}

          except Exception as e:
               print(f"\033[44m {str(e)} \033[0m")
               return {"success": False, "error": str(e)}