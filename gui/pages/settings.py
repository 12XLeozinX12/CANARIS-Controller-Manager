from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QCheckBox,
    QSpinBox,
    QPushButton,
    QApplication
)


from core.settings_manager import settings
from core.theme_manager import theme
from core.startup_manager import startup
from core.language_manager import language


from gui.widgets.notification import notification





class Settings(QWidget):


    def __init__(self):

        super().__init__()


        self.init_ui()


        language.idioma_alterado.connect(
            self.atualizar_textos
        )






    def init_ui(self):


        layout = QVBoxLayout(
            self
        )


        layout.setContentsMargins(
            30,
            30,
            30,
            30
        )


        layout.setSpacing(
            15
        )





        self.titulo = QLabel()


        self.titulo.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:30px;
            font-weight:bold;
            """
        )


        layout.addWidget(
            self.titulo
        )






        self.subtitulo = QLabel()


        self.subtitulo.setStyleSheet(
            """
            color:#999;
            font-size:14px;
            """
        )


        layout.addWidget(
            self.subtitulo
        )






        # TEMA


        self.tema_label = QLabel()


        layout.addWidget(
            self.tema_label
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


        self.idioma_label = QLabel()


        layout.addWidget(
            self.idioma_label
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


        self.som = QCheckBox()


        self.som.setChecked(
            settings.get(
                "som"
            )
        )


        layout.addWidget(
            self.som
        )







        # VIBRAÇÃO


        self.vibracao = QCheckBox()


        self.vibracao.setChecked(
            settings.get(
                "vibracao"
            )
        )


        layout.addWidget(
            self.vibracao
        )







        # START WINDOWS


        self.start = QCheckBox()


        self.start.setChecked(
            settings.get(
                "iniciar_windows"
            )
        )


        layout.addWidget(
            self.start
        )







        # TAXA


        self.taxa_label = QLabel()


        layout.addWidget(
            self.taxa_label
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







        # SALVAR


        self.salvar_btn = QPushButton()


        self.salvar_btn.clicked.connect(
            self.salvar
        )


        layout.addWidget(
            self.salvar_btn
        )


        layout.addStretch()



        self.atualizar_textos()







    def atualizar_textos(self):


        self.titulo.setText(

            language.texto(
                "settings_titulo"
            )

        )


        self.subtitulo.setText(
            "Personalize o CANARIS ™ Controller Manager"
        )


        self.tema_label.setText(

            language.texto(
                "tema"
            )

        )


        self.idioma_label.setText(

            language.texto(
                "idioma"
            )

        )


        self.som.setText(

            language.texto(
                "som"
            )

        )


        self.vibracao.setText(

            language.texto(
                "vibracao"
            )

        )


        self.start.setText(

            language.texto(
                "iniciar_windows"
            )

        )


        self.taxa_label.setText(

            language.texto(
                "taxa_atualizacao"
            )

        )


        self.salvar_btn.setText(

            language.texto(
                "salvar"
            )

        )









    def salvar(self):


        try:


            settings.set(
                "tema",
                self.tema.currentText()
            )



            idioma_visual = self.idioma.currentText()



            settings.set(
                "idioma",
                idioma_visual
            )



            if idioma_visual == "English":

                language.mudar_idioma(
                    "en"
                )


            else:

                language.mudar_idioma(
                    "pt"
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


                notification.info(
                    "CANARIS iniciado com o Windows."
                )


            else:


                startup.desativar()


                notification.info(
                    "Inicialização automática desativada."
                )







            theme.aplicar(

                QApplication.instance(),

                self.tema.currentText()

            )







            notification.success(
                "Configurações salvas com sucesso!"
            )






        except Exception as erro:


            notification.error(

                f"Erro ao salvar configurações: {erro}"

            )