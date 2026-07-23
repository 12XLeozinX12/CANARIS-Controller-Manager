from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea
)

from PySide6.QtCore import Qt

from core.language_manager import language
from core.version_manager import version

from gui.widgets.notification import notification





class Sobre(QWidget):


    def __init__(self):

        super().__init__()


        self.init_ui()


        language.idioma_alterado.connect(
            self.atualizar_textos
        )


        notification.info(
            "Página Sobre carregada."
        )





    def init_ui(self):


        principal = QVBoxLayout(
            self
        )


        principal.setContentsMargins(
            0,
            0,
            0,
            0
        )



        # =========================
        # SCROLL
        # =========================


        scroll = QScrollArea()


        scroll.setWidgetResizable(
            True
        )


        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )


        scroll.setStyleSheet(
            """
            QScrollArea{
                background:#101010;
                border:none;
            }


            QScrollBar:vertical{

                background:#171717;
                width:12px;
                border-radius:6px;

            }


            QScrollBar::handle:vertical{

                background:#8B5CF6;
                border-radius:6px;

            }


            QScrollBar::handle:vertical:hover{

                background:#A855F7;

            }
            """
        )





        container = QWidget()



        layout = QVBoxLayout(
            container
        )


        layout.setContentsMargins(
            30,
            30,
            30,
            30
        )


        layout.setSpacing(
            20
        )



        scroll.setWidget(
            container
        )



        principal.addWidget(
            scroll
        )






        # =========================
        # TITULO
        # =========================


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





        # =========================
        # TEXTO
        # =========================


        self.texto = QLabel()


        self.texto.setStyleSheet(
            """
            color:white;
            font-size:16px;
            line-height:25px;
            """
        )


        self.texto.setWordWrap(
            True
        )


        self.texto.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )



        layout.addWidget(
            self.texto
        )





        # Espaço para futuras seções


        self.extra = QLabel()


        self.extra.setStyleSheet(
            """
            color:#AAAAAA;
            font-size:15px;
            """
        )


        self.extra.setWordWrap(
            True
        )


        layout.addWidget(
            self.extra
        )




        layout.addStretch()



        self.atualizar_textos()








    def atualizar_textos(self):


        try:


            versao = version.get_version()


        except Exception as erro:


            versao = "Desconhecida"


            notification.error(
                f"Erro ao carregar versão: {erro}"
            )





        if language.idioma == "pt":



            self.titulo.setText(
                "ℹ Sobre o CANARIS ™ CM"
            )



            self.texto.setText(

f"""
CANARIS ™ Controller Manager


Versão:
{versao}


Um sistema profissional para
gerenciamento, configuração e
monitoramento de controles.


Recursos:


🎮 Detecção automática de controles


🔌 Suporte USB e Bluetooth


🧪 Controller Lab para testes


👤 Sistema de perfis


🎯 Sistema avançado de calibração


🌎 Suporte multilíngue



Desenvolvido pela equipe CANARIS ™.


Todos os direitos reservados.
"""

            )



            self.extra.setText(

"""
━━━━━━━━━━━━━━━━━━


Mais informações:


O CANARIS ™ está em constante evolução.


Novos recursos, melhorias de compatibilidade
e ferramentas avançadas serão adicionadas
nas próximas versões.


Obrigado por utilizar o CANARIS ™ Controller Manager.
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
{versao}


A professional system for
controller management,
configuration and monitoring.


Features:


🎮 Automatic controller detection


🔌 USB and Bluetooth support


🧪 Controller Lab testing


👤 Profile system


🎯 Advanced calibration system


🌎 Multilingual support



Developed by the CANARIS ™ team.


All rights reserved.
"""

            )



            self.extra.setText(

"""
━━━━━━━━━━━━━━━━━━


More information:


CANARIS ™ is constantly evolving.


New features, compatibility improvements
and advanced tools will be added
in future versions.


Thank you for using CANARIS ™ Controller Manager.
"""

            )