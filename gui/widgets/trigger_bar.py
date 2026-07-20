from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt



class TriggerBar(QWidget):


    def __init__(
        self,
        nome
    ):

        super().__init__()


        self.nome = nome

        self.valor = 0


        self.setMinimumHeight(
            45
        )





    def set_value(
        self,
        valor
    ):


        # converte -1 até 1
        # para 0 até 100


        self.valor = int(
            ((valor + 1) / 2) * 100
        )


        if self.valor < 0:

            self.valor = 0


        if self.valor > 100:

            self.valor = 100



        self.update()






    def paintEvent(
        self,
        event
    ):


        painter = QPainter(
            self
        )


        painter.setRenderHint(
            QPainter.Antialiasing
        )



        painter.setPen(
            QColor(
                "white"
            )
        )


        painter.drawText(
            10,
            25,
            self.nome
        )



        # fundo


        painter.setBrush(
            QColor(
                "#292929"
            )
        )


        painter.drawRoundedRect(
            120,
            10,
            220,
            20,
            10,
            10
        )



        # preenchimento


        largura = int(
            220 *
            self.valor /
            100
        )



        painter.setBrush(
            QColor(
                "#8B5CF6"
            )
        )


        painter.drawRoundedRect(
            120,
            10,
            largura,
            20,
            10,
            10
        )



        painter.drawText(
            360,
            25,
            f"{self.valor}%"
        )