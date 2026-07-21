import pygame


class ControllerDebug:


    def __init__(self):

        pygame.init()
        pygame.joystick.init()

        self.controller = None

        self.atualizar()



    def atualizar(self):

        pygame.event.pump()


        if pygame.joystick.get_count() > 0:


            if self.controller is None:

                self.controller = pygame.joystick.Joystick(0)
                self.controller.init()


        else:

            self.controller=None




    def ler(self):

        self.atualizar()


        if not self.controller:

            return None



        pygame.event.pump()



        dados={


            "nome":
            self.controller.get_name(),


            "botoes":{},


            "eixos":{},


            "hats":{}

        }




        # =========================
        # BOTÕES
        # =========================

        total=self.controller.get_numbuttons()


        for i in range(total):


            dados["botoes"][i]={


                "pressionado":
                bool(
                    self.controller.get_button(i)
                )


            }






        # =========================
        # EIXOS
        # =========================

        total=self.controller.get_numaxes()


        for i in range(total):


            dados["eixos"][i]=round(

                self.controller.get_axis(i),

                3

            )






        # =========================
        # DPAD / HAT
        # =========================


        if self.controller.get_numhats()>0:


            dados["hats"][0]=self.controller.get_hat(0)




        return dados