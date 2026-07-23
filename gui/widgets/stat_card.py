from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class StatCard(QFrame):

    def __init__(
        self,
        title="",
        value="0",
        icon="📊",
        color="#8B5CF6"
    ):

        super().__init__()

        self.color = color


        self.setMinimumHeight(
            145
        )


        self.setStyleSheet("""
        QFrame{
            background:#171717;
            border:1px solid #252525;
            border-radius:18px;
        }
        """)



        layout = QVBoxLayout(
            self
        )


        layout.setContentsMargins(
            22,
            20,
            22,
            20
        )


        layout.setSpacing(
            8
        )



        self.icon = QLabel(
            icon
        )


        self.icon.setAlignment(
            Qt.AlignCenter
        )


        self.icon.setStyleSheet("""
        font-size:26px;
        """)



        self.title = QLabel(
            title
        )


        self.title.setAlignment(
            Qt.AlignCenter
        )


        self.title.setStyleSheet("""
        color:#999999;
        font-size:14px;
        font-weight:600;
        """)



        self.value = QLabel(
            str(value)
        )


        self.value.setAlignment(
            Qt.AlignCenter
        )


        self.value.setStyleSheet(f"""
        color:{color};
        font-size:34px;
        font-weight:700;
        """)



        layout.addWidget(
            self.icon
        )

        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.value
        )



    def setTitle(
        self,
        text
    ):

        self.title.setText(
            text
        )



    def setValue(
        self,
        value
    ):

        self.value.setText(
            str(value)
        )



    def setIcon(
        self,
        icon
    ):

        self.icon.setText(
            icon
        )