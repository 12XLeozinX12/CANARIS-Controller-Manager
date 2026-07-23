from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QCursor
from PySide6.QtCore import Qt


class ModernButton(QPushButton):

    def __init__(

        self,

        text="Button",

        icon=None,

        parent=None

    ):

        super().__init__(text, parent)

        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.setMinimumHeight(46)

        self.setMinimumWidth(170)

        self.setGraphicsEffect(self._shadow())

        self._build_style()

        if icon:
            self.setIcon(icon)

    # ==================================
    # SOMBRA
    # ==================================

    def _shadow(self):

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(30)

        shadow.setOffset(0, 6)

        shadow.setColor(QColor(124, 58, 237, 120))

        return shadow

    # ==================================
    # ESTILO
    # ==================================

    def _build_style(self):

        self.setStyleSheet("""

        QPushButton{

            background:qlineargradient(

                x1:0,y1:0,

                x2:1,y2:1,

                stop:0 #7C3AED,

                stop:1 #5B21B6

            );

            color:white;

            border:none;

            border-radius:12px;

            font-size:14px;

            font-weight:600;

            padding:10px 20px;

        }

        QPushButton:hover{

            background:qlineargradient(

                x1:0,y1:0,

                x2:1,y2:1,

                stop:0 #8B5CF6,

                stop:1 #6D28D9

            );

        }

        QPushButton:pressed{

            background:#4C1D95;

            padding-top:12px;

            padding-bottom:8px;

        }

        QPushButton:disabled{

            background:#3B3B46;

            color:#777777;

        }

        """)