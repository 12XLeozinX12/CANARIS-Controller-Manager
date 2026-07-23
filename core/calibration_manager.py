import os
import json





class CalibrationManager:



    def __init__(self):


        self.folder = os.path.join(

            "profiles",

            "controllers"

        )


        self.criar_pasta()








    def criar_pasta(self):


        if not os.path.exists(

            self.folder

        ):


            os.makedirs(

                self.folder

            )









    def caminho(

        self,

        guid

    ):


        return os.path.join(

            self.folder,

            f"{guid}.json"

        )

    def salvar(

            self,

            guid,

            dados

    ):

        if not guid:
            print(
                "ERRO: GUID vazio"
            )

            return False

        arquivo = self.caminho(

            guid

        )

        print(
            "SALVANDO CALIBRAÇÃO EM:",
            arquivo
        )

        try:

            with open(

                    arquivo,

                    "w",

                    encoding="utf-8"

            ) as f:

                json.dump(

                    dados,

                    f,

                    indent=4,

                    ensure_ascii=False

                )

            print(
                "CALIBRAÇÃO SALVA COM SUCESSO"
            )

            return True



        except Exception as erro:

            print(
                "ERRO AO SALVAR:",
                erro
            )

            return False







    def carregar(

        self,

        guid

    ):


        arquivo = self.caminho(

            guid

        )



        if not os.path.exists(

            arquivo

        ):


            return self.padrao()





        try:


            with open(

                arquivo,

                "r",

                encoding="utf-8"

            ) as f:


                return json.load(

                    f

                )



        except:


            return self.padrao()







    def padrao(self):


        return {


            "deadzone_left":0.08,


            "deadzone_right":0.08,


            "trigger_deadzone":0.05,


            "sensitivity":1.0,


            "invert_y":False


        }








    def existe(

        self,

        guid

    ):


        return os.path.exists(

            self.caminho(

                guid

            )

        )







calibration = CalibrationManager()