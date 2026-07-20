from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QProgressBar
)

from PySide6.QtCore import Qt



class UpdateWindow(QDialog):


    def __init__(
        self,
        version
    ):

        super().__init__()


        self.setWindowTitle(
            "CANARIS ™ Update"
        )


        self.setFixedSize(
            400,
            220
        )



        layout = QVBoxLayout(
            self
        )



        titulo = QLabel(
            "🚀 Nova atualização encontrada"
        )


        titulo.setAlignment(
            Qt.AlignCenter
        )


        titulo.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:20px;
            font-weight:bold;
            """
        )



        layout.addWidget(
            titulo
        )



        self.info = QLabel(

f"""
Versão disponível:

{version}

"""

        )


        self.info.setAlignment(
            Qt.AlignCenter
        )



        layout.addWidget(
            self.info
        )



        self.progress = QProgressBar()


        self.progress.setValue(
            0
        )


        layout.addWidget(
            self.progress
        )



        self.button = QPushButton(
            "⬇ Atualizar agora"
        )


        layout.addWidget(
            self.button
        )