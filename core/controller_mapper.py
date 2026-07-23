import json
import os





class ControllerMapper:



    def __init__(self):


        self.pasta = "profiles/controllers"


        os.makedirs(
            self.pasta,
            exist_ok=True
        )





    # ======================================
    # CAMINHO DO PERFIL
    # ======================================


    def caminho(
        self,
        guid
    ):


        nome = guid.replace(
            "/",
            "_"
        )


        return os.path.join(

            self.pasta,

            f"{nome}.json"

        )






    # ======================================
    # PERFIL PADRÃO
    # ======================================


    def perfil_padrao(self):


        return {


            "buttons":{


                "A":0,

                "B":1,

                "X":2,

                "Y":3,


                "LB":4,

                "RB":5,


                "SELECT":6,

                "START":7,


                "HOME":8


            },



            "axes":{


                "LEFT_X":0,

                "LEFT_Y":1,


                "RIGHT_X":2,

                "RIGHT_Y":3,


                "L2":4,

                "R2":5


            },



            "invert":{


                "LEFT_Y":False,

                "RIGHT_Y":False


            },


            "deadzone":0.08



        }









    # ======================================
    # CARREGAR
    # ======================================


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


            perfil = self.perfil_padrao()


            self.salvar(
                guid,
                perfil
            )


            return perfil






        try:


            with open(
                arquivo,
                "r",
                encoding="utf-8"
            ) as f:


                return json.load(f)



        except:


            return self.perfil_padrao()







    # ======================================
    # SALVAR
    # ======================================


    def salvar(
        self,
        guid,
        dados
    ):



        arquivo = self.caminho(
            guid
        )



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









    # ======================================
    # ALTERAR BOTÃO
    # ======================================


    def mapear_botao(

        self,

        guid,

        nome,

        codigo

    ):



        perfil = self.carregar(
            guid
        )


        perfil["buttons"][nome]=codigo



        self.salvar(

            guid,

            perfil

        )








    # ======================================
    # ALTERAR EIXO
    # ======================================


    def mapear_eixo(

        self,

        guid,

        nome,

        codigo

    ):


        perfil = self.carregar(
            guid
        )


        perfil["axes"][nome]=codigo



        self.salvar(

            guid,

            perfil

        )








    # ======================================
    # RESETAR
    # ======================================


    def resetar(

        self,

        guid

    ):



        arquivo = self.caminho(
            guid
        )



        if os.path.exists(
            arquivo
        ):

            os.remove(
                arquivo
            )
