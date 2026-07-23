import json
import os

from core.controller_profile import ControllerProfiles

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

        modelo = ControllerProfiles.detectar(

            controller.get(
                "name",
                ""
            ),

            controller.get(
                "guid",
                ""
            )

        )

        perfil = {

            "name":

                controller.get(

                    "name",

                    controller.get(

                        "nome",

                        "Novo Controle"

                    )

                ),

            "id":

                controller.get(

                    "id",

                    ""

                ),

            "guid":

                controller.get(

                    "guid",

                    ""

                ),

            "type":

                controller.get(

                    "type",

                    controller.get(

                        "tipo",

                        "Generic"

                    )

                ),

            "controller": {

                "buttons":

                    controller.get(

                        "buttons",

                        0

                    ),

                "axes":

                    controller.get(

                        "axes",

                        0

                    )

            },

            "calibration": {

                "deadzone_left":

                    0.08,

                "deadzone_right":

                    0.08,

                "trigger_deadzone":

                    0.05

            },

            "mapping": {},

            "settings": {

                "vibration":

                    True,

                "sensitivity":

                    100

            },

            "statistics": {

                "hours":

                    0

            }

        }

        self.profiles.append(

            perfil

        )

        self.save()

        return perfil



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



            "buttons":

    modelo["buttons"],


"axes":

    modelo["axes"],


"dpad":

    modelo["dpad"],



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

    def update_profile(
            self,
            index,
            dados
    ):

        if index < 0:
            return False

        if index >= len(
                self.profiles
        ):
            return False

        self.profiles[index].update(
            dados
        )

        self.save()

        return True


    # =========================
    # BUSCAR PERFIL PELO GUID
    # =========================

    def find_by_guid(
            self,
            guid
    ):

        if not guid:

            return None


        for perfil in self.profiles:

            if perfil.get(
                "guid"
            ) == guid:

                return perfil


        return None



    # =========================
    # ATUALIZAR DADOS DO CONTROLE
    # =========================

    def update_controller_data(
            self,
            guid,
            categoria,
            dados
    ):


        perfil = self.find_by_guid(
            guid
        )


        if not perfil:

            return False



        if categoria not in perfil:

            perfil[categoria] = {}



        perfil[categoria].update(
            dados
        )


        self.save()


        return True


    def clear_all(self):


        self.profiles = []


        self.save()