import sys

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(BASE_DIR)
)



from database.session import SessionManager





print("\n==============================")
print(" TESTE SESSION CANARIS ")
print("==============================\n")




session = SessionManager()



usuario = {


    "id":2,

    "username":"luiz_gamer",

    "email":"luizgamer@email.com"


}




print("Salvando sessão...")


session.login(

    usuario

)



print(

    session.get_user()

)




print("\nVerificando login...")


print(

    session.is_logged()

)





print("\nFinalizado!")