from core.app_data import app_data



class SettingsManager:



    def __init__(self):


        self.defaults = {


            "tema":

            "Escuro",


            "idioma":

            "Português",


            "language":

            "pt",


            "som":

            True,


            "vibracao":

            True,


            "iniciar_windows":

            False,


            "taxa_atualizacao":

            50

        }



        self.data = {}


        self.carregar()







    def carregar(self):


        self.data = app_data.load_settings()



        alterado = False



        for chave, valor in self.defaults.items():


            if chave not in self.data:


                self.data[chave] = valor


                alterado = True





        if alterado:


            self.salvar()







    def salvar(self):


        app_data.save_settings(

            self.data

        )







    def get(

        self,

        chave

    ):


        return self.data.get(

            chave,

            self.defaults.get(
                chave
            )

        )








    def set(

        self,

        chave,

        valor

    ):


        self.data[chave] = valor


        self.salvar()







    def resetar(self):


        self.data = self.defaults.copy()


        self.salvar()








settings = SettingsManager()