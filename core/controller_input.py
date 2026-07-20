import pygame


class ControllerInput:

    def __init__(self):

        pygame.init()

        pygame.joystick.init()


        self.controller = None


        self._botoes = []

        self._eixos = []


        self.detectar()



    def detectar(self):

        quantidade = pygame.joystick.get_count()


        if quantidade > 0:

            self.controller = pygame.joystick.Joystick(0)

            self.controller.init()



    def conectado(self):

        return self.controller is not None



    def atualizar(self):

        self._botoes = []

        self._eixos = []


        if not self.controller:

            return



        pygame.event.pump()



        # Botões

        for i in range(
            self.controller.get_numbuttons()
        ):


            if self.controller.get_button(i):

                self._botoes.append(
                    i
                )



        # Analógicos

        for i in range(
            self.controller.get_numaxes()
        ):


            valor = self.controller.get_axis(i)


            self._eixos.append(
                round(valor, 2)
            )



    def botoes(self):

        return self._botoes



    def eixos(self):

        return self._eixos



    def nome(self):

        if self.controller:

            return self.controller.get_name()


        return "Nenhum controle"