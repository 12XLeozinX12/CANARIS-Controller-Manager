from core.settings_manager import settings



class AppSettings:



    def __init__(self):

        self.manager = settings






    def get(

        self,

        chave

    ):


        return self.manager.get(

            chave

        )







    def set(

        self,

        chave,

        valor

    ):


        self.manager.set(

            chave,

            valor

        )







    def resetar(self):


        self.manager.resetar()







app_settings = AppSettings()