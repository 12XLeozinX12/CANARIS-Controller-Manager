import json

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent


SESSION_FILE = BASE_DIR / "session.json"





class SessionManager:



    def __init__(self):

        self.user = None


        self.load()





    # ==================================
    # SALVAR SESSÃO
    # ==================================


    def login(self, user):


        self.user = user


        self.save()





    # ==================================
    # SAIR
    # ==================================


    def logout(self):


        self.user = None


        if SESSION_FILE.exists():

            SESSION_FILE.unlink()





    # ==================================
    # USUÁRIO ATUAL
    # ==================================


    def get_user(self):


        return self.user





    # ==================================
    # VERIFICAR LOGIN
    # ==================================


    def is_logged(self):


        return self.user is not None





    # ==================================
    # SALVAR ARQUIVO
    # ==================================


    def save(self):


        if self.user:


            with open(

                SESSION_FILE,

                "w",

                encoding="utf-8"

            ) as arquivo:


                json.dump(

                    self.user,

                    arquivo,

                    indent=4,

                    ensure_ascii=False

                )





    # ==================================
    # CARREGAR
    # ==================================


    def load(self):


        if SESSION_FILE.exists():


            try:


                with open(

                    SESSION_FILE,

                    "r",

                    encoding="utf-8"

                ) as arquivo:


                    self.user = json.load(

                        arquivo

                    )


            except:


                self.user = None