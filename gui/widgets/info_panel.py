from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import Qt


class InfoPanel(QFrame):

    def __init__(self, title="Information"):

        super().__init__()

        self.setStyleSheet("""
        QFrame{
            background:#171717;
            border:1px solid #252525;
            border-radius:18px;
        }

        QLabel{
            border:none;
        }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            22,
            22,
            22,
            22
        )

        layout.setSpacing(15)

        self.title = QLabel(title)

        self.title.setStyleSheet("""
        color:white;
        font-size:22px;
        font-weight:700;
        """)

        layout.addWidget(self.title)

        self.container = QVBoxLayout()

        self.container.setSpacing(10)

        layout.addLayout(self.container)

        layout.addStretch()

        self.items = {}

    def setTitle(self, title):

        self.title.setText(title)

    def clear(self):

        while self.container.count():

            item = self.container.takeAt(0)

            if item.widget():

                item.widget().deleteLater()

        self.items = {}

    def setInfo(self, data: dict):

        self.clear()

        for key, value in data.items():

            row = QFrame()

            row.setStyleSheet("""
            QFrame{
                background:#1D1D1D;
                border-radius:10px;
            }
            """)

            h = QHBoxLayout(row)

            h.setContentsMargins(
                12,
                10,
                12,
                10
            )

            lbl_key = QLabel(str(key))

            lbl_key.setStyleSheet("""
            color:#9B9B9B;
            font-size:13px;
            font-weight:600;
            """)

            lbl_value = QLabel(str(value))

            lbl_value.setAlignment(Qt.AlignRight)

            lbl_value.setStyleSheet("""
            color:white;
            font-size:13px;
            font-weight:700;
            """)

            h.addWidget(lbl_key)

            h.addStretch()

            h.addWidget(lbl_value)

            self.container.addWidget(row)