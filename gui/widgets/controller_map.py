# CANARIS ™ Controller Manager
# Controller Map Widget BETA


from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QFont
from PySide6.QtCore import Qt


class ControllerMap(QWidget):

    def __init__(self):
        super().__init__()

        self.tipo = "Nenhum Controle"
        self.connected = False

        self.buttons = {}

        self.axes = {
            "LX":0.0,
            "LY":0.0,
            "RX":0.0,
            "RY":0.0
        }

        self.setMinimumSize(600,350)



    def update_controller(
            self,
            tipo="Controle",
            buttons=None,
            axes=None,
            triggers=None
    ):

        self.tipo = tipo or "Controle"

        self.connected = True

        self.buttons = buttons or {}


        if isinstance(axes, list):

            valores = axes + [0,0,0,0]

            self.axes["LX"] = float(valores[0])
            self.axes["LY"] = float(valores[1])
            self.axes["RX"] = float(valores[2])
            self.axes["RY"] = float(valores[3])


        self.update()



    def pressed(self, name):

        return self.buttons.get(name, False)



    def paintEvent(self,event):

        p = QPainter(self)

        p.setRenderHint(
            QPainter.Antialiasing
        )


        w = self.width()
        h = self.height()


        # fundo CANARIS

        p.fillRect(
            self.rect(),
            QColor("#080812")
        )


        # titulo

        p.setPen(
            QColor("#FFFFFF")
        )

        p.setFont(
            QFont(
                "Segoe UI",
                18,
                QFont.Bold
            )
        )


        p.drawText(
            25,
            35,
            "CANARIS ™ Controller Map"
        )


        p.setFont(
            QFont(
                "Segoe UI",
                11
            )
        )


        p.setPen(
            QColor("#AAAAAA")
        )


        status = (
            "ONLINE"
            if self.connected
            else "OFFLINE"
        )


        p.drawText(
            25,
            60,
            f"{self.tipo}  |  {status}"
        )


        # painel

        p.setBrush(
            QColor("#151520")
        )

        p.setPen(
            QPen(
                QColor("#8B5CF6"),
                2
            )
        )


        p.drawRoundedRect(
            20,
            85,
            w-40,
            190,
            18,
            18
        )


        # sticks

        self.draw_stick(
            p,
            130,
            180,
            "LX",
            "LY"
        )


        self.draw_stick(
            p,
            w-130,
            180,
            "RX",
            "RY"
        )


        # botoes

        self.draw_button(
            p,
            w-230,
            140,
            "Y"
        )

        self.draw_button(
            p,
            w-280,
            180,
            "X"
        )

        self.draw_button(
            p,
            w-180,
            180,
            "B"
        )

        self.draw_button(
            p,
            w-230,
            220,
            "A"
        )


        # dados

        p.setPen(
            QColor("#AAAAAA")
        )

        p.drawText(
            30,
            h-30,
            f"LX:{self.axes['LX']:.2f}  LY:{self.axes['LY']:.2f}"
        )

        p.drawText(
            250,
            h-30,
            f"RX:{self.axes['RX']:.2f}  RY:{self.axes['RY']:.2f}"
        )




    def draw_button(
            self,
            p,
            x,
            y,
            name
    ):

        ativo = self.pressed(name)


        p.setBrush(
            QColor("#8B5CF6")
            if ativo
            else QColor("#333344")
        )


        p.setPen(
            QPen(
                QColor("#777777"),
                2
            )
        )


        p.drawEllipse(
            x-18,
            y-18,
            36,
            36
        )


        p.setPen(Qt.white)


        p.drawText(
            x-5,
            y+5,
            name
        )




    def draw_stick(
            self,
            p,
            x,
            y,
            ax,
            ay
    ):


        p.setBrush(
            QColor("#222233")
        )


        p.setPen(
            QColor("#22D3EE")
        )


        p.drawEllipse(
            x-40,
            y-40,
            80,
            80
        )


        px = x + self.axes[ax] * 30
        py = y + self.axes[ay] * 30


        p.setBrush(
            QColor("#8B5CF6")
        )


        p.drawEllipse(
            px-12,
            py-12,
            24,
            24
        )