import pygame

from core.config_manager import config


class ControllerManager:


    def __init__(self):

        pygame.init()
        pygame.joystick.init()

        self.controller = None

        self.atualizar()



    # ==========================
    # CONECTAR CONTROLE
    # ==========================

    def atualizar(self):

        pygame.event.pump()

        if pygame.joystick.get_count() > 0:

            if self.controller is None:

                self.controller = pygame.joystick.Joystick(0)
                self.controller.init()

        else:

            self.controller = None



    # ==========================
    # LISTAR CONTROLES
    # ==========================

    def detectar_controles(self):

        self.atualizar()


        if not self.controller:

            return []



        guid = self.controller.get_guid()


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
                guid,

                "guid":
                guid

            }

        ]



    # ==========================
    # ESTADO COMPLETO
    # ==========================

    def get_state(self):


        self.atualizar()


        estado = {

            "info":{

                "connected":False,
                "nome":"",
                "tipo":"",
                "guid":"",
                "botoes":0,
                "eixos":0

            },

            "buttons":{},


            "axes":[],


            "triggers":{

                "L2":0,
                "R2":0

            },


            "dpad":{

                "up":False,
                "down":False,
                "left":False,
                "right":False

            }

        }



        if not self.controller:

            return estado



        pygame.event.pump()



        # ======================
        # BOTÕES
        # ======================


        botoes = {}


        for i in range(
            self.controller.get_numbuttons()
        ):

            botoes[i] = bool(
                self.controller.get_button(i)
            )





        # ======================
        # EIXOS
        # ======================


        eixos = []


        for i in range(
            self.controller.get_numaxes()
        ):


            valor = self.controller.get_axis(i)


            if abs(valor) < 0.05:

                valor = 0


            eixos.append(
                round(valor,3)
            )





        # ======================
        # TRIGGERS
        # ======================


        triggers = {

            "L2":0,
            "R2":0

        }



        if len(eixos) >= 6:


            triggers["L2"] = self.converter_trigger(
                eixos[4]
            )


            triggers["R2"] = self.converter_trigger(
                eixos[5]
            )





        # ======================
        # DPAD
        # ======================


        dpad = {

            "up":False,
            "down":False,
            "left":False,
            "right":False

        }



        # DualShock usa botões

        if botoes.get(11):

            dpad["up"] = True


        if botoes.get(12):

            dpad["down"] = True


        if botoes.get(13):

            dpad["left"] = True


        if botoes.get(14):

            dpad["right"] = True




        estado["info"] = {

            "connected":True,

            "nome":
            self.controller.get_name(),

            "tipo":
            self.identificar_tipo(),

            "guid":
            self.controller.get_guid(),

            "botoes":
            self.controller.get_numbuttons(),

            "eixos":
            self.controller.get_numaxes()

        }



        estado["buttons"] = botoes

        estado["axes"] = eixos

        estado["triggers"] = triggers

        estado["dpad"] = dpad



        return estado




    # ==========================
    # TRIGGER
    # ==========================

    def converter_trigger(self,valor):

        valor=float(valor)


        if valor < -0.9:

            return 0


        if valor >= 0:

            return round(valor*100,1)


        return round(
            ((valor+1)/2)*100,
            1
        )




    # ==========================
    # TIPO
    # ==========================

    def identificar_tipo(self):


        if not self.controller:

            return "Unknown"



        nome = self.controller.get_name().lower()


        guid = self.controller.get_guid().lower()



        if any(x in nome for x in [

            "dualshock",
            "dualsense",
            "sony",
            "playstation"

        ]):

            return "PlayStation"



        if "054c" in guid:

            return "PlayStation"



        if "xbox" in nome or "xinput" in guid:

            return "Xbox"



        return "Generic"




    # ==========================
    # VIBRAÇÃO
    # ==========================

    def vibrar(self,forca=0.7,tempo=500):


        if not config.vibracao_ativa():

            return False



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


        except:

            pass


        return False