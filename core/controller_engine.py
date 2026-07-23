# ==========================================================
# CANARIS Controller Manager 21.0
# Controller Engine
# Core Controller System
# ==========================================================


import pygame
import time



class ControllerEngine:


    def __init__(self):


        pygame.init()

        pygame.joystick.init()


        self.controller = None

        self.connected = False

        self.name = None


        self.last_connection_check = 0


        self.state = {

            "name": None,

            "connected": False,

            "buttons": [],

            "axes": [],

            "triggers": {

                "L2": 0.0,

                "R2": 0.0

            },

            "hat": (0,0)

        }


        self.initialize()



    # ======================================================
    # INIT
    # ======================================================

    def initialize(self):

        self.scan_controllers()



    # ======================================================
    # DETECT CONTROLLER
    # ======================================================

    def scan_controllers(self):


        pygame.joystick.quit()

        pygame.joystick.init()



        count = pygame.joystick.get_count()



        if count > 0:


            joystick = pygame.joystick.Joystick(0)

            joystick.init()


            self.controller = joystick


            self.connected = True


            self.name = joystick.get_name()



            self.state["name"] = self.name

            self.state["connected"] = True



        else:


            self.controller = None

            self.connected = False


            self.name = None


            self.state["name"] = None

            self.state["connected"] = False




    # ======================================================
    # UPDATE LOOP
    # ======================================================

    def update(self):


        pygame.event.pump()



        # verifica conexão a cada 1 segundo

        if time.time() - self.last_connection_check > 1:


            self.last_connection_check = time.time()


            current = pygame.joystick.get_count()



            if current == 0 and self.connected:


                self.disconnect()



            elif current > 0 and not self.connected:


                self.scan_controllers()



        if not self.connected:

            return



        try:


            self.read_buttons()

            self.read_axes()

            self.read_hat()



        except Exception:


            self.disconnect()




    # ======================================================
    # BUTTONS
    # ======================================================

    def read_buttons(self):


        buttons = []


        total = self.controller.get_numbuttons()



        for i in range(total):


            value = self.controller.get_button(i)


            buttons.append(
                value
            )


        self.state["buttons"] = buttons




    # ======================================================
    # AXIS
    # ======================================================

    def read_axes(self):


        axes = []


        total = self.controller.get_numaxes()



        for i in range(total):


            value = self.controller.get_axis(i)


            axes.append(
                round(value,3)
            )



        self.state["axes"] = axes



        # padrão:

        # DualShock/Xbox

        # Axis 2 = LT

        # Axis 5 = RT


        if len(axes) > 2:


            self.state["triggers"]["L2"] = self.normalize_trigger(
                axes[2]
            )


        if len(axes) > 5:


            self.state["triggers"]["R2"] = self.normalize_trigger(
                axes[5]
            )




    # ======================================================
    # HAT / D-PAD
    # ======================================================

    def read_hat(self):


        if self.controller.get_numhats():


            self.state["hat"] = (
                self.controller.get_hat(0)
            )


        else:


            self.state["hat"] = (
                0,
                0
            )




    # ======================================================
    # TRIGGER NORMALIZATION
    # ======================================================

    def normalize_trigger(
        self,
        value
    ):


        # transforma -1/+1 em 0/100


        result = (
            value + 1
        ) / 2



        if result < 0:

            result = 0


        if result > 1:

            result = 1



        return round(
            result,
            2
        )




    # ======================================================
    # DISCONNECT
    # ======================================================

    def disconnect(self):


        self.controller = None


        self.connected = False


        self.name = None


        self.state = {

            "name": None,

            "connected": False,

            "buttons": [],

            "axes": [],

            "triggers": {

                "L2":0.0,

                "R2":0.0

            },

            "hat":(0,0)

        }



    # ======================================================
    # GET STATE
    # ======================================================

    def get_state(self):


        return self.state



    # ======================================================
    # GET NAME
    # ======================================================

    def get_name(self):


        return self.name



    # ======================================================
    # STATUS
    # ======================================================

    def is_connected(self):


        return self.connected