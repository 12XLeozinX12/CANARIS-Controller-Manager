from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from core.language_manager import language
from core.version_manager import version



class Sobre(QWidget):


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


        self.titulo.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:30px;
            font-weight:bold;
            """
        )



        self.texto = QLabel()


        self.texto.setStyleSheet(
            """
            color:white;
            font-size:16px;
            """
        )


        self.texto.setWordWrap(
            True
        )


        layout.addWidget(
            self.titulo
        )


        layout.addWidget(
            self.texto
        )


        layout.addStretch()



        self.setLayout(
            layout
        )


        self.atualizar_textos()



    def atualizar_textos(self):


        if language.idioma == "pt":


            self.titulo.setText(
                "ℹ Sobre o CANARIS ™ CM"
            )


            self.texto.setText(

f"""
CANARIS ™ Controller Manager


Versão:
{version.get_version()}


Um sistema profissional para
gerenciamento, configuração e
monitoramento de controles.


Recursos:

🎮 Detecção automática de controles

🔌 Suporte USB e Bluetooth

🧪 Controller Lab para testes

👤 Sistema de perfis

🌎 Suporte multilíngue


Desenvolvido pela equipe CANARIS.


Todos os direitos reservados.
"""

            )



        else:


            self.titulo.setText(
                "ℹ About CANARIS ™ CM"
            )


            self.texto.setText(

f"""
CANARIS ™ Controller Manager


Version:
{version.get_version()}


A professional system for
controller management,
configuration and monitoring.


Features:

🎮 Automatic controller detection

🔌 USB and Bluetooth support

🧪 Controller Lab testing

👤 Profile system

🌎 Multilingual support


Developed by the CANARIS team.


All rights reserved.
"""

            )