from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox
)

from core.language_manager import language



class Config(QWidget):


    def __init__(self):

        super().__init__()


        self.init_ui()


        language.idioma_alterado.connect(
            self.atualizar_textos
        )



    def init_ui(self):


        layout = QVBoxLayout()


        layout.setContentsMargins(
            25,
            25,
            25,
            25
        )


        self.titulo = QLabel()


        self.idioma_label = QLabel()


        self.combo = QComboBox()


        self.combo.addItem(
            "Português",
            "pt"
        )


        self.combo.addItem(
            "English",
            "en"
        )


        self.combo.currentIndexChanged.connect(
            self.mudar_idioma
        )


        layout.addWidget(
            self.titulo
        )


        layout.addWidget(
            self.idioma_label
        )


        layout.addWidget(
            self.combo
        )


        layout.addStretch()


        self.setLayout(
            layout
        )


        self.atualizar_textos()



    def atualizar_textos(self):


        self.titulo.setText(
            language.texto(
                "config_titulo"
            )
        )


        self.idioma_label.setText(

            "Idioma / Language"

        )



        if language.idioma == "pt":

            self.combo.setCurrentIndex(
                0
            )

        else:

            self.combo.setCurrentIndex(
                1
            )




    def mudar_idioma(self):


        idioma = (
            self.combo.currentData()
        )


        language.mudar_idioma(
            idioma
        )