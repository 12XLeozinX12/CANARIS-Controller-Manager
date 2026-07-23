from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
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



# ======================================
# CAMINHO DA LOGO
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent

LOGO_PATH = (
    BASE_DIR
    /
    "assets"
    /
    "images"
    /
    "canaris_logo.png"
)



# ======================================
# APP
# ======================================

app = QApplication([])



# ======================================
# JANELA
# ======================================

window = QWidget()

window.setWindowTitle(
    "CANARIS Controller Manager"
)


window.setStyleSheet(
    """
    QWidget{

        background:#0A0E27;

    }
    """
)



layout = QVBoxLayout(window)

layout.setAlignment(
    Qt.AlignCenter
)



# ======================================
# CARD PRINCIPAL
# ======================================

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



# ======================================
# LOGO
# ======================================

logo = QLabel()


pix = QPixmap(
    str(LOGO_PATH)
)


if pix.isNull():

    print(
        "ERRO: Logo não encontrada:"
    )

    print(
        LOGO_PATH
    )


else:

    print(
        "Logo carregada com sucesso!"
    )


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



# ======================================
# TITULO
# ======================================

subtitle = QLabel(
    "Controller Manager"
)


subtitle.setStyleSheet(
    """
    color:#94A3B8;

    font-size:14px;

    font-weight:500;

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



# ======================================
# CAMPOS
# ======================================

username = ModernLineEdit(
    "Username"
)


password = ModernLineEdit(
    "Password",
    True
)


cardLayout.addWidget(
    username
)


cardLayout.addWidget(
    password
)



# ======================================
# CHECKBOX
# ======================================

remember = QCheckBox(
    "Remember me"
)


remember.setStyleSheet(
    """
    QCheckBox{

        color:#F0F4F8;

        font-size:13px;

    }

    QCheckBox::indicator{

        width:18px;

        height:18px;

    }

    """
)



cardLayout.addWidget(
    remember
)



cardLayout.addSpacing(
    15
)



# ======================================
# BOTÃO
# ======================================

loginButton = ModernButton(
    "LOGIN"
)


cardLayout.addWidget(
    loginButton
)



# ======================================
# FINAL
# ======================================

layout.addWidget(
    card
)



window.resize(
    900,
    650
)


window.show()



app.exec()