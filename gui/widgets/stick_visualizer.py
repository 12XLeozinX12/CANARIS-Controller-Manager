from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QBrush
from PySide6.QtCore import Qt, QTimer





class StickVisualizer(QWidget):


    def __init__(self):

        super().__init__()


        # posição atual desenhada

        self.x = 0.0
        self.y = 0.0



        # posição desejada

        self.target_x = 0.0
        self.target_y = 0.0



        self.deadzone = 0.08



        self.setMinimumSize(
            220,
            220
        )



        # animação

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.animar
        )

        self.timer.start(
            16
        )







    def atualizar(

        self,

        x,

        y,

        deadzone=None

    ):


        self.target_x = x

        self.target_y = y



        if deadzone is not None:

            self.deadzone = deadzone







    def animar(self):


        velocidade = 0.18



        self.x += (

            self.target_x - self.x

        ) * velocidade



        self.y += (

            self.target_y - self.y

        ) * velocidade



        self.update()







    def paintEvent(self,event):


        painter = QPainter(
            self
        )


        painter.setRenderHint(
            QPainter.Antialiasing
        )



        centro_x = self.width() // 2

        centro_y = self.height() // 2



        raio = min(
            self.width(),
            self.height()
        ) // 2 - 20







        painter.setPen(

            QPen(
                Qt.gray,
                2
            )

        )


        painter.setBrush(

            QBrush(
                Qt.transparent
            )

        )


        painter.drawEllipse(

            centro_x-raio,

            centro_y-raio,

            raio*2,

            raio*2

        )







        # DEADZONE


        dz = int(
            raio*self.deadzone
        )



        painter.setPen(

            QPen(
                Qt.darkGreen,
                2
            )

        )



        painter.drawEllipse(

            centro_x-dz,

            centro_y-dz,

            dz*2,

            dz*2

        )







        # linhas


        painter.setPen(

            QPen(
                Qt.gray,
                1
            )

        )


        painter.drawLine(

            centro_x-raio,
            centro_y,

            centro_x+raio,
            centro_y

        )


        painter.drawLine(

            centro_x,
            centro_y-raio,

            centro_x,
            centro_y+raio

        )








        pos_x = centro_x + int(

            self.x * raio

        )


        pos_y = centro_y + int(

            self.y * raio

        )





        cor = Qt.green



        if (

            abs(self.x) > self.deadzone

            or

            abs(self.y) > self.deadzone

        ):

            cor = Qt.red






        painter.setPen(
            Qt.NoPen
        )


        painter.setBrush(

            QBrush(
                cor
            )

        )


        painter.drawEllipse(

            pos_x-10,

            pos_y-10,

            20,

            20

        )