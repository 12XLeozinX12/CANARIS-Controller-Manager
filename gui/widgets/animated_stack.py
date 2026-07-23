from PySide6.QtWidgets import QStackedWidget
from PySide6.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
    QPoint
)



class AnimatedStack(QStackedWidget):


    def __init__(self):

        super().__init__()

        self.animacao = None



    def setCurrentWidget(
        self,
        widget
    ):


        atual = self.currentWidget()



        if atual == widget:

            return



        if atual is None:

            super().setCurrentWidget(
                widget
            )

            return




        largura = self.width()



        widget.setGeometry(
            self.rect()
        )


        widget.move(
            largura,
            0
        )



        super().setCurrentWidget(
            widget
        )



        self.animacao = QPropertyAnimation(

            widget,

            b"pos"

        )



        self.animacao.setDuration(
            250
        )



        self.animacao.setStartValue(

            QPoint(
                largura,
                0
            )

        )



        self.animacao.setEndValue(

            QPoint(
                0,
                0
            )

        )



        self.animacao.setEasingCurve(

            QEasingCurve.OutCubic

        )



        self.animacao.start()