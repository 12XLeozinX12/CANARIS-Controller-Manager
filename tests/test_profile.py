import sys

from pathlib import Path



# adicionar raiz do projeto

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(BASE_DIR)
)



from database.users import UserManager
from database.profile import GamerProfile




print("\n==============================")
print(" TESTE PERFIL GAMER CANARIS ")
print("==============================\n")



# =================================
# USUARIO
# =================================


users = UserManager()



username = "luiz_gamer"

senha = "1234"

email = "luizgamer@email.com"



print("Criando usuário...")



criado = users.create_user(

    username,

    senha,

    email

)



print(
    "Usuário criado:",
    criado
)




usuario = users.get_user(

    username

)



print(
    "\nUsuário encontrado:"
)


print(
    usuario
)




# =================================
# PERFIL GAMER
# =================================


perfil = GamerProfile()



print(
    "\nCriando perfil gamer..."
)



criar_perfil = perfil.create_profile(

    usuario["id"],

    "Nerd"

)



print(

    "Perfil criado:",

    criar_perfil

)




# =================================
# BUSCAR PERFIL
# =================================


print(
    "\nBuscando perfil..."
)



dados = perfil.get_profile(

    usuario["id"]

)



print(
    dados
)