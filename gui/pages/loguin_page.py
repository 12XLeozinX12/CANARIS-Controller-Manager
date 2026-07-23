from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QCheckBox
)

from PySide6.QtCore import Qt

from PySide6.QtGui import QPixmap

from gui.widgets.modern_card import ModernCard
from gui.widgets.modern_button import ModernButton
from gui.widgets.modern_lineedit import ModernLineEdit



class LoginPage(QWidget):


    def __init__(self, parent=None):

        super().__init__(parent)


        self._build_ui()



    # ==================================
    # INTERFACE
    # ==================================

    def _build_ui(self):


        self.setStyleSheet(
            """
            QWidget{

                background:#0A0E27;

            }
            """
        )


        layout = QVBoxLayout(self)


        layout.setAlignment(
            Qt.AlignCenter
        )



        # CARD

        card = ModernCard()


        card.setFixedSize(
            420,
            520
        )


        cardLayout = QVBoxLayout(card)


        cardLayout.setContentsMargins(
            35,
            35,
            35,
            35
        )


        cardLayout.setSpacing(
            18
        )



        # LOGO

        logo = QLabel()


        base = Path(__file__).resolve().parent.parent.parent


        logo_path = (

            base
            /
            "assets"
            /
            "images"
            /
            "canaris_logo.png"

        )



        pix = QPixmap(
            str(logo_path)
        )



        if not pix.isNull():


            pix = pix.scaled(

                180,
                180,

                Qt.KeepAspectRatio,

                Qt.SmoothTransformation

            )


            logo.setPixmap(
                pix
            )



        logo.setAlignment(
            Qt.AlignCenter
        )



        cardLayout.addWidget(
            logo
        )



        # TITULO


        title = QLabel(
            "CANARIS"
        )


        title.setStyleSheet(
            """
            color:white;

            font-size:26px;

            font-weight:700;

            """
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        cardLayout.addWidget(
            title
        )



        subtitle = QLabel(
            "Controller Manager"
        )


        subtitle.setStyleSheet(
            """
            color:#94A3B8;

            font-size:13px;

            """
        )


        subtitle.setAlignment(
            Qt.AlignCenter
        )


        cardLayout.addWidget(
            subtitle
        )



        cardLayout.addSpacing(
            15
        )



        # CAMPOS


        self.username = ModernLineEdit(
            "Username"
        )


        self.password = ModernLineEdit(
            "Password",
            True
        )


        cardLayout.addWidget(
            self.username
        )


        cardLayout.addWidget(
            self.password
        )



        # REMEMBER


        self.remember = QCheckBox(
            "Remember me"
        )


        self.remember.setStyleSheet(
            """
            QCheckBox{

                color:#F0F4F8;

            }

            """
        )


        cardLayout.addWidget(
            self.remember
        )



        cardLayout.addSpacing(
            10
        )



        # BOTÃO


        self.login_button = ModernButton(
            "LOGIN"
        )


        cardLayout.addWidget(
            self.login_button
        )



        layout.addWidget(
            card
        )