from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QBrush, QPen
from PySide6.QtCore import Qt, QTimer





class TriggerVisualizer(QWidget):


    def __init__(self, nome="Trigger"):


        super().__init__()



        self.nome = nome



        # valor desenhado

        self.valor = 0.0


        # valor recebido do controle

        self.target = 0.0




        self.setMinimumSize(
            120,
            180
        )




        # animação suave

        self.timer = QTimer()


        self.timer.timeout.connect(
            self.animar
        )


        self.timer.start(
            16
        )









    def atualizar(self, valor):


        self.target = max(
            0,
            min(
                100,
                valor
            )
        )









    def animar(self):


        velocidade = 0.15



        diferenca = (

            self.target -

            self.valor

        )



        self.valor += (

            diferenca *

            velocidade

        )



        if abs(diferenca) < 0.1:

            self.valor = self.target



        self.update()










    def paintEvent(self,event):


        painter = QPainter(
            self
        )


        painter.setRenderHint(
            QPainter.Antialiasing
        )



        largura = self.width()


        altura = self.height()-30






        # fundo


        painter.setPen(
            Qt.NoPen
        )


        painter.setBrush(

            QBrush(
                Qt.darkGray
            )

        )


        painter.drawRoundedRect(

            30,

            10,

            largura-60,

            altura,

            10,

            10

        )







        # preenchimento


        preenchimento = int(

            altura *

            (self.valor / 100)

        )




        # cor dinâmica

        if self.valor < 40:

            cor = Qt.green


        elif self.valor < 80:

            cor = Qt.yellow


        else:

            cor = Qt.red





        painter.setBrush(

            QBrush(
                cor
            )

        )




        painter.drawRoundedRect(

            30,

            altura-preenchimento+10,

            largura-60,

            preenchimento,

            10,

            10

        )







        # texto


        painter.setPen(

            QPen(
                Qt.white
            )

        )



        painter.drawText(

            20,

            altura+25,

            f"{self.nome}: {self.valor:.0f}%"

        )