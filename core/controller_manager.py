import pygame



class ControllerManager:

    def detectar_controles(self):


        self.atualizar()


        if not self.controller:


            return []



        return [

            {

                "nome":
                self.controller.get_name(),


                "tipo":
                self.identificar_tipo(),


                "botoes":
                self.controller.get_numbuttons(),


                "eixos":
                self.controller.get_numaxes(),


                "id":
                self.controller.get_guid()

            }

        ]


    def __init__(self):


        pygame.init()

        pygame.joystick.init()


        self.controller = None


        self.atualizar()





    def atualizar(self):


        pygame.event.pump()


        quantidade = pygame.joystick.get_count()



        if quantidade > 0:


            if self.controller is None:


                self.controller = pygame.joystick.Joystick(0)

                self.controller.init()



        else:


            self.controller = None






    def get_state(self):


        self.atualizar()


        estado = {


            "info": {


                "connected": False,

                "nome": "",

                "tipo": "",

                "guid": "",

                "botoes": 0,

                "eixos": 0

            },


            "buttons": [],


            "axes": [],


            "dpad": {}

        }





        if not self.controller:


            return estado






        pygame.event.pump()



        nome = self.controller.get_name()


        guid = self.controller.get_guid()



        tipo = self.identificar_tipo()






        # =====================
        # BOTÕES
        # =====================


        botoes = []



        try:


            quantidade = (
                self.controller
                .get_numbuttons()
            )



            for i in range(quantidade):


                if self.controller.get_button(i):


                    botoes.append(i)



        except pygame.error:


            pass







        # =====================
        # EIXOS
        # =====================


        eixos = []



        try:


            quantidade = (
                self.controller
                .get_numaxes()
            )



            for i in range(quantidade):


                valor = (
                    self.controller
                    .get_axis(i)
                )



                if abs(valor) < 0.05:

                    valor = 0



                eixos.append(
                    round(
                        valor,
                        2
                    )
                )



        except pygame.error:


            pass






        estado["info"] = {


            "connected": True,


            "nome": nome,


            "tipo": tipo,


            "guid": guid,


            "botoes": self.controller.get_numbuttons(),


            "eixos": self.controller.get_numaxes()

        }





        estado["buttons"] = botoes


        estado["axes"] = eixos





        return estado







    def identificar_tipo(self):


        if not self.controller:


            return "Unknown"




        nome = (
            self.controller
            .get_name()
            .lower()
        )


        guid = (
            self.controller
            .get_guid()
            .lower()
        )



        # PLAYSTATION


        palavras = [

            "dualshock",

            "dualsense",

            "sony",

            "playstation",

            "wireless controller"

        ]



        for p in palavras:


            if p in nome:


                return "PlayStation"




        if "054c" in guid:


            return "PlayStation"





        # XBOX


        if (

            "xbox" in nome

            or

            "xinput" in guid

        ):


            return "Xbox"





        return "Generic"

    def vibrar(
        self,
        forca=0.7,
        tempo=500
    ):


        if not self.controller:

            return False



        try:


            if hasattr(
                self.controller,
                "rumble"
            ):


                self.controller.rumble(
                    forca,
                    forca,
                    tempo
                )


                return True



        except Exception:


            pass



        return False