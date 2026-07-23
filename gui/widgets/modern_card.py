from PySide6.QtWidgets import QFrame
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class ModernCard(QFrame):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setObjectName("ModernCard")

        self.setStyleSheet("""

        QFrame#ModernCard{

            background:#131B2E;

            border:1px solid #252F46;

            border-radius:20px;

        }

        """)

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(40)

        shadow.setOffset(0,10)

        shadow.setColor(QColor(0,0,0,180))

        self.setGraphicsEffect(shadow)