from PySide6.QtWidgets import QPushButton

from PySide6.QtCore import (
    QPropertyAnimation,
    QEasingCurve
)



class AnimatedButton(QPushButton):


    def __init__(
        self,
        texto
    ):

        super().__init__(
            texto
        )


        self.normal_style = """

        QPushButton{

            background:#171717;

            color:white;

            border:2px solid #2a2a2a;

            border-radius:35px;

            font-size:18px;

            font-weight:bold;

        }

        QPushButton:hover{

            border:2px solid #8B5CF6;

        }

        """



        self.active_style = """

        QPushButton{

            background:#8B5CF6;

            color:white;

            border:2px solid #C084FC;

            border-radius:35px;

            font-size:18px;

            font-weight:bold;

        }

        """



        self.setFixedSize(
            75,
            75
        )


        self.setStyleSheet(
            self.normal_style
        )



    def pressionar(self):


        self.setStyleSheet(
            self.active_style
        )


        animacao = QPropertyAnimation(
            self,
            b"geometry"
        )


        animacao.setDuration(
            120
        )


        animacao.setEasingCurve(
            QEasingCurve.OutBack
        )


        atual = self.geometry()


        animacao.setStartValue(
            atual
        )


        animacao.setEndValue(
            atual.adjusted(
                -4,
                -4,
                4,
                4
            )
        )


        animacao.start()


        self.animacao = animacao



    def soltar(self):


        self.setStyleSheet(
            self.normal_style
        )