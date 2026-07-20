from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QPen,
    QBrush,
    QColor
)

from PySide6.QtCore import Qt



class AnalogStick(QWidget):

    def __init__(self, nome):

        super().__init__()

        self.nome = nome

        self.x = 0

        self.y = 0


        self.setMinimumSize(
            180,
            180
        )



    def atualizar(
        self,
        x,
        y
    ):

        self.x = x

        self.y = y

        self.update()



    def paintEvent(self, event):

        painter = QPainter(self)


        painter.setRenderHint(
            QPainter.Antialiasing
        )


        centro_x = self.width() // 2

        centro_y = self.height() // 2



        pen = QPen(
            QColor("#8B5CF6")
        )

        pen.setWidth(3)


        painter.setPen(
            pen
        )


        painter.setBrush(
            QBrush(
                QColor("#222222")
            )
        )


        painter.drawEllipse(
            centro_x-60,
            centro_y-60,
            120,
            120
        )



        pos_x = centro_x + int(
            self.x * 45
        )


        pos_y = centro_y + int(
            self.y * 45
        )


        painter.setBrush(
            QBrush(
                QColor("#8B5CF6")
            )
        )


        painter.drawEllipse(
            pos_x-20,
            pos_y-20,
            40,
            40
        )



        painter.setPen(
            QColor("white")
        )


        painter.drawText(
            45,
            20,
            self.nome
        )


        painter.drawText(
            40,
            155,
            f"X: {self.x}"
        )


        painter.drawText(
            40,
            175,
            f"Y: {self.y}"
        )