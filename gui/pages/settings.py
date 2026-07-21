from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QSpinBox,
    QMessageBox
)


from PySide6.QtWidgets import QApplication


from core.settings_manager import settings
from core.theme_manager import theme
from core.startup_manager import startup





class Settings(QWidget):


    def __init__(self):

        super().__init__()

        self.criar_interface()





    def criar_interface(self):


        layout = QVBoxLayout(
            self
        )


        titulo = QLabel(
            "⚙ Configurações CANARIS ™"
        )


        titulo.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:30px;
            font-weight:bold;
            """
        )


        layout.addWidget(
            titulo
        )





        # TEMA


        layout.addWidget(
            QLabel(
                "Tema"
            )
        )


        self.tema = QComboBox()


        self.tema.addItems(

            [

                "Escuro",

                "Claro"

            ]

        )


        self.tema.setCurrentText(

            settings.get(
                "tema"
            )

        )


        layout.addWidget(
            self.tema
        )






        # IDIOMA


        layout.addWidget(
            QLabel(
                "Idioma"
            )
        )


        self.idioma = QComboBox()


        self.idioma.addItems(

            [

                "Português",

                "English"

            ]

        )


        self.idioma.setCurrentText(

            settings.get(
                "idioma"
            )

        )


        layout.addWidget(
            self.idioma
        )






        # SOM


        self.som = QCheckBox(
            "🔊 Sons do CANARIS"
        )


        self.som.setChecked(

            settings.get(
                "som"
            )

        )


        layout.addWidget(
            self.som
        )






        # VIBRAÇÃO


        self.vibracao = QCheckBox(
            "🎮 Vibração dos controles"
        )


        self.vibracao.setChecked(

            settings.get(
                "vibracao"
            )

        )


        layout.addWidget(
            self.vibracao
        )






        # WINDOWS


        self.start = QCheckBox(
            "🚀 Iniciar com Windows"
        )


        self.start.setChecked(

            settings.get(
                "iniciar_windows"
            )

        )


        layout.addWidget(
            self.start
        )







        # TAXA


        layout.addWidget(

            QLabel(
                "Atualização do Controller Lab"
            )

        )



        self.taxa = QSpinBox()


        self.taxa.setRange(
            10,
            1000
        )


        self.taxa.setValue(

            settings.get(
                "taxa_atualizacao"
            )

        )


        self.taxa.setSuffix(
            " ms"
        )


        layout.addWidget(
            self.taxa
        )







        salvar = QPushButton(
            "💾 Salvar Configurações"
        )


        salvar.clicked.connect(
            self.salvar
        )


        layout.addWidget(
            salvar
        )


        layout.addStretch()







    def salvar(self):


        settings.set(

            "tema",

            self.tema.currentText()

        )


        settings.set(

            "idioma",

            self.idioma.currentText()

        )



        settings.set(

            "som",

            self.som.isChecked()

        )


        settings.set(

            "vibracao",

            self.vibracao.isChecked()

        )


        settings.set(

            "iniciar_windows",

            self.start.isChecked()

        )


        settings.set(

            "taxa_atualizacao",

            self.taxa.value()

        )






        if self.start.isChecked():

            startup.ativar()

        else:

            startup.desativar()






        theme.aplicar(

            QApplication.instance(),

            self.tema.currentText()

        )




        QMessageBox.information(

            self,

            "CANARIS ™",

            "Configurações salvas!"

        )