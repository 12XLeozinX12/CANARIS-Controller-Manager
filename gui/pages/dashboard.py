from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from gui.widgets.card import Card
from core.controller_manager import ControllerManager
from core.language_manager import language



class Dashboard(QWidget):


    def __init__(self):

        super().__init__()


        self.controller_manager = ControllerManager()


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
            color:white;
            font-size:28px;
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

        controles = (
            self.controller_manager
            .detectar_controles()
            if hasattr(
                self.controller_manager,
                "detectar_controles"
            )
            else []
        )

        total = len(
            controles
        )


        status = (
            "ONLINE"
            if total > 0
            else
            "AGUARDANDO"
        )



        cards = QHBoxLayout()



        self.card_controles = Card(
            "",
            total
        )


        self.card_status = Card(
            "",
            status
        )


        self.card_sistema = Card(
            "",
            "ONLINE",
            "#00D26A"
        )



        cards.addWidget(
            self.card_controles
        )


        cards.addWidget(
            self.card_status
        )


        cards.addWidget(
            self.card_sistema
        )



        layout.addLayout(
            cards
        )


        layout.addStretch()



        self.setLayout(
            layout
        )


        self.atualizar_textos()




    def atualizar_textos(self):


        self.titulo.setText(
            "🐤 CANARIS ™ Dashboard"
        )


        self.subtitulo.setText(
            language.texto(
                "dashboard_subtitulo"
            )
        )


        self.card_controles.set_title(
            "🎮 " +
            language.texto(
                "controles_card"
            )
        )


        self.card_status.set_title(
            "🔌 " +
            language.texto(
                "status_card"
            )
        )


        self.card_sistema.set_title(
            "⚡ " +
            language.texto(
                "sistema_card"
            )
        )