import sys
from pathlib import Path


# adiciona a raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(BASE_DIR)
)


from database.users import UserManager




users = UserManager()



print(
    "Criando usuário..."
)



resultado = users.create_user(

    "luiz",

    "1234",

    "luiz@email.com"

)



print(
    "Criado:",
    resultado
)




print(
    "\nTentando login..."
)



login = users.login(

    "luiz",

    "1234"

)



print(
    "Resultado:",
    login
)