from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


class ActionButton(QPushButton):

    def __init__(
        self,
        text="",
        icon="",
        color="#8B5CF6"
    ):
        super().__init__(f"{icon}  {text}")

        self.color = color

        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(48)

        self.setStyleSheet(f"""
        QPushButton{{
            background:{color};
            color:white;
            border:none;
            border-radius:14px;
            font-size:14px;
            font-weight:600;
            padding:10px 18px;
            text-align:left;
        }}

        QPushButton:hover{{
            background:#9D6CFF;
        }}

        QPushButton:pressed{{
            background:#6E3FE0;
        }}

        QPushButton:disabled{{
            background:#2A2A2A;
            color:#666666;
        }}
        """)

    def setColor(self, color):

        self.color = color

        self.setStyleSheet(f"""
        QPushButton{{
            background:{color};
            color:white;
            border:none;
            border-radius:14px;
            font-size:14px;
            font-weight:600;
            padding:10px 18px;
            text-align:left;
        }}

        QPushButton:hover{{
            background:#9D6CFF;
        }}

        QPushButton:pressed{{
            background:#6E3FE0;
        }}

        QPushButton:disabled{{
            background:#2A2A2A;
            color:#666666;
        }}
        """)