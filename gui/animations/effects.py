from PySide6.QtCore import (
    QPropertyAnimation,
    QEasingCurve
)

from PySide6.QtWidgets import (
    QGraphicsOpacityEffect
)



def fade_in(widget, duration=400):

    efeito = QGraphicsOpacityEffect()

    widget.setGraphicsEffect(
        efeito
    )


    animacao = QPropertyAnimation(
        efeito,
        b"opacity"
    )


    animacao.setDuration(
        duration
    )


    animacao.setStartValue(
        0
    )


    animacao.setEndValue(
        1
    )


    animacao.setEasingCurve(
        QEasingCurve.OutCubic
    )


    animacao.start()


    widget._fade_effect = efeito

    widget._fade_animation = animacao




def fade_out(widget, duration=300):

    efeito = QGraphicsOpacityEffect()

    widget.setGraphicsEffect(
        efeito
    )


    animacao = QPropertyAnimation(
        efeito,
        b"opacity"
    )


    animacao.setDuration(
        duration
    )


    animacao.setStartValue(
        1
    )


    animacao.setEndValue(
        0
    )


    animacao.setEasingCurve(
        QEasingCurve.InCubic
    )


    animacao.start()


    widget._fade_effect = efeito

    widget._fade_animation = animacao