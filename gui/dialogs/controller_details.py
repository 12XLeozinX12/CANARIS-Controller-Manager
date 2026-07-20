from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame
)

from PySide6.QtCore import QTimer

import pygame

from gui.widgets.analog_stick import AnalogStick
from gui.widgets.button_indicator import ButtonIndicator
from gui.widgets.trigger_bar import TriggerBar
from gui.widgets.dpad import DPadButton


class ControllerDetails(QDialog):

    def __init__(self, controle, joystick):
        super().__init__()

        self.joystick = joystick


        self.setWindowTitle(
            "CANARIS • Controller Monitor"
        )

        self.setMinimumSize(
            900,
            800
        )


        self.setStyleSheet("""
            QDialog {
                background:#09090b;
            }

            QLabel {
                color:white;
            }

            #titulo {
                font-size:24px;
                font-weight:bold;
            }

            #info {
                color:#a1a1aa;
            }
        """)


        layout = QVBoxLayout(self)


        titulo = QLabel(
            "🎮 CANARIS Real Time Monitor"
        )

        titulo.setObjectName(
            "titulo"
        )


        self.info = QLabel()

        self.info.setObjectName(
            "info"
        )


        layout.addWidget(titulo)
        layout.addWidget(self.info)



        # ANALÓGICOS

        sticks = QHBoxLayout()


        self.left_stick = AnalogStick(
            "LEFT STICK"
        )

        self.right_stick = AnalogStick(
            "RIGHT STICK"
        )


        sticks.addWidget(
            self.left_stick
        )

        sticks.addWidget(
            self.right_stick
        )


        layout.addLayout(sticks)



        # TRIGGERS

        triggers = QHBoxLayout()


        self.l2 = TriggerBar("L2")
        self.r2 = TriggerBar("R2")


        triggers.addWidget(self.l2)
        triggers.addWidget(self.r2)


        layout.addLayout(triggers)



        # D PAD

        dpad_frame = QFrame()

        dpad_layout = QGridLayout(
            dpad_frame
        )


        self.dpad = {

            "UP": DPadButton("+"),
            "DOWN": DPadButton("-"),
            "LEFT": DPadButton("<"),
            "RIGHT": DPadButton(">")

        }


        dpad_layout.addWidget(
            self.dpad["UP"],
            0,
            1
        )

        dpad_layout.addWidget(
            self.dpad["LEFT"],
            1,
            0
        )

        dpad_layout.addWidget(
            self.dpad["RIGHT"],
            1,
            2
        )

        dpad_layout.addWidget(
            self.dpad["DOWN"],
            2,
            1
        )


        layout.addWidget(
            dpad_frame
        )



        # BOTÕES

        botoes = QFrame()

        grid = QGridLayout(
            botoes
        )


        self.buttons = {}


        mapa = {

            "1":0,
            "2":1,
            "3":2,
            "4":3,

            "SHARE":4,
            "OPTIONS":6,

            "L3":7,
            "R3":8,

            "LB":9,
            "RB":10
        }


        for nome, indice in mapa.items():

            self.buttons[indice] = ButtonIndicator(
                nome
            )


        posicoes = [

            (3,0,1),
            (2,1,0),
            (1,1,2),
            (0,2,1),

            (9,3,0),
            (10,3,2),

            (4,4,0),
            (6,4,2),

            (7,5,0),
            (8,5,2)

        ]


        for botao, linha, coluna in posicoes:

            grid.addWidget(
                self.buttons[botao],
                linha,
                coluna
            )


        layout.addWidget(
            botoes
        )



        self.timer = QTimer()

        self.timer.timeout.connect(
            self.atualizar
        )

        self.timer.start(16)



    def atualizar(self):

        pygame.event.pump()


        # STICKS

        if self.joystick.get_numaxes() >= 4:

            self.left_stick.atualizar(
                self.joystick.get_axis(0),
                self.joystick.get_axis(1)
            )

            self.right_stick.atualizar(
                self.joystick.get_axis(2),
                self.joystick.get_axis(3)
            )



        # TRIGGERS

        if self.joystick.get_numaxes() >= 6:

            self.l2.atualizar(
                self.joystick.get_axis(4)
            )

            self.r2.atualizar(
                self.joystick.get_axis(5)
            )



        # BOTÕES

        pressionados = []


        for indice, botao in self.buttons.items():

            estado = self.joystick.get_button(indice)

            botao.atualizar(
                estado
            )

            if estado:
                pressionados.append(
                    botao.nome
                )



        # ======================
        # D-PAD
        # ======================


        cima = False
        baixo = False
        esquerda = False
        direita = False



        # tenta HAT

        if self.joystick.get_numhats() > 0:

            hat = self.joystick.get_hat(0)

            esquerda = hat[0] == -1
            direita = hat[0] == 1
            cima = hat[1] == 1
            baixo = hat[1] == -1



        # fallback para botões
        # DualShock 4 Windows costuma usar esses

        else:

            botoes = self.joystick.get_numbuttons()


            if botoes >= 16:

                esquerda = self.joystick.get_button(13)
                baixo = self.joystick.get_button(12)
                direita = self.joystick.get_button(14)
                cima = self.joystick.get_button(11)



        self.dpad["UP"].atualizar(cima)
        self.dpad["DOWN"].atualizar(baixo)
        self.dpad["LEFT"].atualizar(esquerda)
        self.dpad["RIGHT"].atualizar(direita)



        self.info.setText(
            f"""
STATUS: ONLINE

Controle:
{self.joystick.get_name()}

Botões pressionados:
{', '.join(pressionados) if pressionados else 'Nenhum'}
"""
        )