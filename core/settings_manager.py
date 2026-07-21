import json
import os



class SettingsManager:


    def __init__(self):

        self.path = "settings.json"


        self.defaults = {


            "tema": "Escuro",

            "idioma": "Português",

            "som": True,

            "vibracao": True,

            "iniciar_windows": False,

            "taxa_atualizacao": 50


        }


        self.data = {}

        self.carregar()





    def carregar(self):


        if os.path.exists(self.path):

            try:

                with open(
                    self.path,
                    "r",
                    encoding="utf-8"
                ) as arquivo:

                    self.data = json.load(
                        arquivo
                    )


            except:

                self.data = {}



        for chave, valor in self.defaults.items():

            if chave not in self.data:

                self.data[chave] = valor



        self.salvar()






    def salvar(self):


        with open(

            self.path,

            "w",

            encoding="utf-8"

        ) as arquivo:


            json.dump(

                self.data,

                arquivo,

                indent=4,

                ensure_ascii=False

            )






    def get(
        self,
        chave
    ):


        return self.data.get(

            chave,

            self.defaults.get(chave)

        )






    def set(

        self,

        chave,

        valor

    ):


        self.data[chave] = valor

        self.salvar()





settings = SettingsManager()