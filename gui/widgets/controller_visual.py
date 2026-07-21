from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush,
    QFont
)
from PySide6.QtCore import Qt



class ControllerVisual(QWidget):


    def __init__(self):

        super().__init__()


        self.setMinimumSize(
            650,
            420
        )


        self.buttons = {}


        self.axes = [
            0,
            0,
            0,
            0
        ]


        self.triggers = {

            "L2":0,
            "R2":0

        }


        self.dpad = {

            "up":False,
            "down":False,
            "left":False,
            "right":False

        }





    # ==========================
    # RECEBER BOTÕES
    # ==========================


    def set_buttons(self,buttons):


        self.buttons = buttons


        self.update()





    def set_axes(self,axes):


        if len(axes)>=4:

            self.axes = [

                axes[0],
                axes[1],
                axes[2],
                axes[3]

            ]


        self.update()





    def set_triggers(self,triggers):


        self.triggers = triggers


        self.update()





    def set_dpad(self,dpad):


        self.dpad = dpad


        self.update()





    # ==========================
    # BOTÃO
    # ==========================


    def pressed(self,id):

        return self.buttons.get(id,False)




    def button(
        self,
        painter,
        x,
        y,
        text,
        id,
        size=25
    ):


        ativo = self.pressed(id)



        if ativo:

            painter.setBrush(
                QColor("#8B5CF6")
            )

        else:

            painter.setBrush(
                QColor("#202020")
            )



        painter.setPen(
            QPen(
                QColor("#777"),
                2
            )
        )


        painter.drawEllipse(
            x-size,
            y-size,
            size*2,
            size*2
        )



        painter.setPen(
            QColor("#FFFFFF")
        )


        painter.setFont(
            QFont(
                "Arial",
                12,
                QFont.Bold
            )
        )


        painter.drawText(
            x-10,
            y+5,
            text
        )





    # ==========================
    # TRIGGER BAR
    # ==========================


    def trigger_bar(
        self,
        painter,
        x,
        y,
        value,
        name
    ):


        painter.setPen(
            QColor("#555")
        )


        painter.setBrush(
            QColor("#151515")
        )


        painter.drawRoundedRect(
            x,
            y,
            100,
            15,
            7,
            7
        )



        painter.setBrush(
            QColor("#8B5CF6")
        )


        painter.drawRoundedRect(
            x,
            y,
            value,
            15,
            7,
            7
        )


        painter.setPen(
            QColor("#FFFFFF")
        )


        painter.drawText(
            x,
            y-8,
            f"{name} {int(value)}%"
        )






    # ==========================
    # DESENHO
    # ==========================


    def paintEvent(self,event):


        painter = QPainter(self)


        painter.setRenderHint(
            QPainter.Antialiasing
        )



        # Fundo


        painter.fillRect(
            self.rect(),
            QColor("#090909")
        )




        # Corpo controle


        painter.setBrush(
            QColor("#151515")
        )


        painter.setPen(
            QPen(
                QColor("#333"),
                3
            )
        )


        painter.drawRoundedRect(
            120,
            80,
            410,
            260,
            90,
            90
        )




        # =====================
        # BOTÕES DIREITOS
        # =====================


        self.button(
            painter,
            450,
            150,
            "△",
            3
        )


        self.button(
            painter,
            500,
            200,
            "○",
            1
        )


        self.button(
            painter,
            400,
            200,
            "□",
            2
        )


        self.button(
            painter,
            450,
            250,
            "X",
            0
        )





        # =====================
        # STICKS
        # =====================


        painter.setBrush(
            QColor("#222")
        )


        painter.drawEllipse(
            190,
            170,
            70,
            70
        )


        painter.drawEllipse(
            330,
            240,
            70,
            70
        )



        painter.setBrush(
            QColor("#8B5CF6")
        )



        painter.drawEllipse(
            215+self.axes[0]*20,
            195+self.axes[1]*20,
            20,
            20
        )



        painter.drawEllipse(
            355+self.axes[2]*20,
            265+self.axes[3]*20,
            20,
            20
        )




        # L3 / R3


        self.button(
            painter,
            225,
            205,
            "L3",
            7,
            14
        )


        self.button(
            painter,
            365,
            275,
            "R3",
            8,
            14
        )






        # =====================
        # OMBROS
        # =====================


        self.button(
            painter,
            170,
            90,
            "L1",
            9,
            22
        )


        self.button(
            painter,
            480,
            90,
            "R1",
            10,
            22
        )




        # =====================
        # SHARE OPTIONS TOUCH
        # =====================


        self.button(
            painter,
            270,
            120,
            "SH",
            4,
            18
        )


        self.button(
            painter,
            380,
            120,
            "OP",
            6,
            18
        )


        self.button(
            painter,
            325,
            160,
            "TP",
            15,
            22
        )




        # =====================
        # TRIGGERS
        # =====================


        self.trigger_bar(
            painter,
            170,
            45,
            self.triggers.get("L2",0),
            "L2"
        )


        self.trigger_bar(
            painter,
            420,
            45,
            self.triggers.get("R2",0),
            "R2"
        )





        # =====================
        # DPAD
        # =====================


        self.button(
            painter,
            250,
            300,
            "↑",
            11,
            15
        )


        self.button(
            painter,
            250,
            340,
            "↓",
            12,
            15
        )


        self.button(
            painter,
            210,
            320,
            "←",
            13,
            15
        )


        self.button(
            painter,
            290,
            320,
            "→",
            14,
            15
        )