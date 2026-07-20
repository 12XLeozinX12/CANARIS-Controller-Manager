from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QFont


class InputButton(QLabel):


    def __init__(self, nome):

        super().__init__(nome)


        self.nome = nome

        self.pressionado = False


        self.setAlignment(
            Qt.AlignCenter
        )


        self.setFixedSize(
            55,
            55
        )


        self.animacao = QPropertyAnimation(
            self,
            b"minimumSize"
        )


        self.normal()



    def normal(self):

        self.setStyleSheet(
            """
            QLabel{

                background:#202020;

                color:white;

                border-radius:27px;

                border:2px solid #8B5CF6;

                font-size:18px;

                font-weight:bold;

            }
            """
        )



    def pressionar(self):


        self.pressionado = True


        self.setStyleSheet(
            """
            QLabel{

                background:#8B5CF6;

                color:white;

                border-radius:27px;

                font-size:18px;

                font-weight:bold;

            }
            """
        )



    def soltar(self):


        self.pressionado=False


        self.normal()