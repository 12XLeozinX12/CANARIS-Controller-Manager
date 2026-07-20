from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import (
    Qt,
    QPropertyAnimation,
    QEasingCurve
)



class AnimatedInput(QWidget):

    def __init__(self):

        super().__init__()


        self.setFixedSize(
            260,
            180
        )


        self.init_ui()



    def init_ui(self):


        layout = QVBoxLayout()


        self.titulo = QLabel(
            "INPUT"
        )


        self.titulo.setStyleSheet(
            """
            color:#8B5CF6;

            font-size:18px;

            font-weight:bold;
            """
        )



        self.botao = QLabel(
            "---"
        )


        self.botao.setStyleSheet(
            """
            color:white;

            font-size:45px;

            font-weight:bold;
            """
        )


        self.botao.setAlignment(
            Qt.AlignCenter
        )



        self.estado = QLabel(
            "Aguardando..."
        )


        self.estado.setStyleSheet(
            """
            color:#999;

            font-size:15px;
            """
        )



        layout.addWidget(
            self.titulo
        )


        layout.addWidget(
            self.botao
        )


        layout.addWidget(
            self.estado
        )



        self.setLayout(
            layout
        )


        self.setStyleSheet(
            """
            QWidget{

                background:#171717;

                border-radius:20px;

                border:2px solid #242424;

            }
            """
        )



    def atualizar(
        self,
        nome,
        pressionado
    ):


        self.botao.setText(
            nome
        )


        if pressionado:


            self.estado.setText(
                "PRESSIONADO 🟣"
            )


            self.estado.setStyleSheet(
                """
                color:#C084FC;

                font-size:15px;

                font-weight:bold;
                """
            )


            self.animar()



        else:


            self.estado.setText(
                "Solto"
            )


            self.estado.setStyleSheet(
                """
                color:#999;

                font-size:15px;
                """
            )



    def animar(self):


        animacao = QPropertyAnimation(
            self,
            b"geometry"
        )


        animacao.setDuration(
            150
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
                -5,
                -5,
                5,
                5
            )
        )


        animacao.start()


        self.animacao = animacao