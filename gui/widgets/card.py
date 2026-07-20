from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt



class Card(QFrame):


    def __init__(
        self,
        titulo,
        valor,
        cor="#8B5CF6"
    ):

        super().__init__()


        self.cor = cor


        self.setStyleSheet(
            f"""
            QFrame
            {{
                background:#171717;
                border-radius:18px;
            }}
            """
        )


        layout = QVBoxLayout(
            self
        )


        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        self.titulo = QLabel(
            titulo
        )


        self.titulo.setStyleSheet(
            """
            color:#999;
            font-size:14px;
            font-weight:bold;
            """
        )


        self.titulo.setAlignment(
            Qt.AlignCenter
        )



        self.valor = QLabel(
            str(valor)
        )


        self.valor.setStyleSheet(
            f"""
            color:{cor};
            font-size:32px;
            font-weight:bold;
            """
        )


        self.valor.setAlignment(
            Qt.AlignCenter
        )



        layout.addWidget(
            self.titulo
        )


        layout.addWidget(
            self.valor
        )



    def set_title(
        self,
        texto
    ):

        self.titulo.setText(
            texto
        )



    def set_value(
        self,
        valor
    ):

        self.valor.setText(
            str(valor)
        )