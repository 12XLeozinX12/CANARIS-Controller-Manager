import pygame

from core.controller_detector import detectar_tipo
from core.controller_layouts import get_layout
from core.statistics_manager import StatisticsManager


class ControllerManager:

    def __init__(self):

        pygame.init()
        pygame.joystick.init()

        self.controller = None

        self.controller_id = None

        self.guid = ""

        self.nome = ""

        self.tipo = "Generic"

        self.devices = []

        self.atualizar()

    # ==================================================
    # ATUALIZAR
    # ==================================================

    def atualizar(self):

        pygame.event.pump()

        self.devices = self.get_devices()

        if pygame.joystick.get_count() == 0:
            self.controller = None
            self.controller_id = None
            self.guid = ""
            self.nome = ""
            self.tipo = "Generic"

            return

        if self.controller is None:
            self.selecionar_controle(0)

    # ==================================================
    # SELEÇÃO MANUAL
    # ==================================================

    def selecionar_controle(self, indice):

        try:

            joystick = pygame.joystick.Joystick(indice)

            joystick.init()

            self.controller = joystick

            self.controller_id = indice

            self.nome = joystick.get_name()

            self.guid = joystick.get_guid()

            self.tipo = detectar_tipo(

                self.nome,

                self.guid

            )

            return True



        except Exception as erro:

            print(
                "Erro selecionando controle:",
                erro
            )

            return False

    # ==================================================
    # DISPOSITIVOS
    # ==================================================

    def get_devices(self):

        dispositivos = []

        pygame.event.pump()

        for i in range(
                pygame.joystick.get_count()
        ):

            try:

                j = pygame.joystick.Joystick(i)

                j.init()

                nome = j.get_name()

                guid = j.get_guid()

                dispositivos.append({

                    "id": i,

                    "name": nome,

                    "nome": nome,

                    "guid": guid,

                    "type":
                        detectar_tipo(
                            nome,
                            guid
                        ),

                    "tipo":
                        detectar_tipo(
                            nome,
                            guid
                        ),

                    "buttons":
                        j.get_numbuttons(),

                    "axes":
                        j.get_numaxes()

                })



            except:

                pass

        return dispositivos

    def detectar_controles(self):

        return self.get_devices()

    # ==================================================
    # INFO PARA PAGE CONTROLES
    # ==================================================

    def get_controller_info(self):

        self.atualizar()

        if not self.controller:
            return {

                "connected": False,

                "name":
                    "Nenhum controle",

                "type":
                    "Generic",

                "buttons":
                    0,

                "axes":
                    0,

                "battery":
                    "N/A"

            }

        bateria = "N/A"

        try:

            if hasattr(
                    self.controller,
                    "get_power_level"
            ):
                bateria = str(
                    self.controller.get_power_level()
                )


        except:

            pass

        return {

            "connected":
                True,

            "name":
                self.nome,

            "type":
                self.tipo,

            "guid":
                self.guid,

            "buttons":
                self.controller.get_numbuttons(),

            "axes":
                self.controller.get_numaxes(),

            "battery":
                bateria

        }

    def get_connected_count(self):

        return pygame.joystick.get_count()

    # ==================================================
    # ESTADO COMPLETO
    # ==================================================

    def get_state(self):

        self.atualizar()

        estado = {

            "connected": False,

            "name": "",

            "type": "Generic",

            "guid": "",

            "buttons": {},

            "raw_buttons": {},

            "analogicos": {

                "LX": 0,
                "LY": 0,
                "RX": 0,
                "RY": 0

            },

            "axes": [0, 0, 0, 0, 0, 0],

            "eixos": [0, 0, 0, 0, 0, 0],

            "triggers": {

                "LT": 0,
                "RT": 0,

                "L2": 0,
                "R2": 0

            }

        }

        if not self.controller:
            return estado

        pygame.event.pump()

        raw = {}

        for i in range(
                self.controller.get_numbuttons()
        ):
            raw[i] = bool(
                self.controller.get_button(i)
            )

        botoes = {}

        try:

            layout = get_layout(
                self.tipo
            )

            for nome, indice in layout.items():
                botoes[nome] = raw.get(
                    indice,
                    False
                )



        except:

            botoes = raw

        eixos = []

        for i in range(
                self.controller.get_numaxes()
        ):

            try:

                valor = self.controller.get_axis(i)


            except:

                valor = 0

            eixos.append(
                round(valor, 3)
            )

        while len(eixos) < 6:
            eixos.append(0)

        analogicos = {

            "LX": eixos[0],

            "LY": eixos[1],

            "RX": eixos[2],

            "RY": eixos[3]

        }

        lt = round(
            ((eixos[4] + 1) / 2) * 100,
            1
        )

        rt = round(
            ((eixos[5] + 1) / 2) * 100,
            1
        )

        return {

            "connected": True,

            "name":
                self.nome,

            "type":
                self.tipo,

            "guid":
                self.guid,

            "buttons":
                botoes,

            "raw_buttons":
                raw,

            "analogicos":
                analogicos,

            "axes":
                eixos,

            "eixos":
                eixos,

            "triggers": {

                "LT": lt,

                "RT": rt,

                "L2": lt,

                "R2": rt

            }

        }

    # ==================================================
    # VIBRAÇÃO
    # ==================================================

    def vibrar(

            self,

            forca=0.5,

            tempo=300

    ):

        try:

            if self.controller and hasattr(

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