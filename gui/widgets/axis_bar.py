from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt



class AxisBar(QWidget):


    def __init__(
        self,
        titulo=""
    ):

        super().__init__()


        self.titulo = titulo

        self.valor = 0


        self.setMinimumHeight(
            45
        )




    def set_value(
        self,
        valor
    ):


        self.valor = max(
            -1,
            min(
                1,
                valor
            )
        )


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



        # texto


        painter.setPen(
            QColor(
                "#FFFFFF"
            )
        )


        painter.drawText(
            10,
            18,
            self.titulo
        )



        # barra


        x = 120

        y = 8

        largura = 230

        altura = 20



        painter.setPen(
            QPen(
                QColor(
                    "#333333"
                ),
                2
            )
        )


        painter.drawRoundedRect(
            x,
            y,
            largura,
            altura,
            10,
            10
        )



        # centro


        centro = (
            x +
            largura / 2
        )



        posicao = (
            centro +
            (
                self.valor *
                largura / 2
            )
        )



        painter.setBrush(
            QColor(
                "#8B5CF6"
            )
        )


        painter.drawEllipse(
            posicao - 8,
            y + 2,
            16,
            16
        )



        # valor


        painter.drawText(
            370,
            18,
            str(
                round(
                    self.valor,
                    2
                )
            )
        )