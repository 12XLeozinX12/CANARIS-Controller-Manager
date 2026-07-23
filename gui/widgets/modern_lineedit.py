from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class ModernLineEdit(QLineEdit):

    def __init__(

        self,

        placeholder="",

        password=False,

        parent=None

    ):

        super().__init__(parent)

        self.setPlaceholderText(placeholder)

        self.setMinimumHeight(46)

        self.setFont(

            QFont(

                "Segoe UI",

                10

            )

        )

        self.setStyleSheet("""

        QLineEdit{

            background:#131B2E;

            border:2px solid #252F46;

            border-radius:12px;

            padding-left:15px;

            padding-right:15px;

            color:white;

            selection-background-color:#7C3AED;

        }

        QLineEdit:hover{

            border:2px solid #4B5563;

        }

        QLineEdit:focus{

            border:2px solid #7C3AED;

            background:#19233A;

        }

        """)

        if password:

            self.setEchoMode(

                QLineEdit.Password

            )