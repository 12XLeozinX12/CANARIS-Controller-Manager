import json
import os



class ProfileManager:


    def __init__(self):


        self.file = self.get_file_path()


        self.profiles = []


        self.load()





    def get_file_path(self):


        # Pasta de dados do usuário
        # Não grava dentro do EXE


        base = os.getenv(

            "APPDATA"

        )


        folder = os.path.join(

            base,

            "CANARIS CM"

        )


        os.makedirs(

            folder,

            exist_ok=True

        )


        return os.path.join(

            folder,

            "profiles.json"

        )







    def load(self):


        if not os.path.exists(

            self.file

        ):


            self.profiles = []


            self.save()


            return




        try:


            with open(

                self.file,

                "r",

                encoding="utf-8"

            ) as arquivo:


                self.profiles = json.load(

                    arquivo

                )



        except:


            self.profiles = []

            self.save()







    def save(self):


        with open(

            self.file,

            "w",

            encoding="utf-8"

        ) as arquivo:


            json.dump(

                self.profiles,

                arquivo,

                indent=4,

                ensure_ascii=False

            )








    def create_profile(

        self,

        controller

    ):



        perfil = {


            "name":

            controller.get(

                "nome",

                "Novo Controle"

            ),



            "id":

            controller.get(

                "id",

                ""

            ),



            "type":

            controller.get(

                "tipo",

                "Generic"

            ),



            "buttons":{},



            "axes":{},



            "vibration":True,



            "sensitivity":100


        }



        self.profiles.append(

            perfil

        )


        self.save()



        return perfil







    def get_profiles(self):


        return self.profiles





    def delete_profile(

        self,

        index

    ):


        if index < 0:

            return



        if index >= len(

            self.profiles

        ):

            return



        self.profiles.pop(

            index

        )


        self.save()






    def clear_all(self):


        self.profiles = []


        self.save()