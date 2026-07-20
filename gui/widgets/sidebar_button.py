from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


class SidebarButton(QPushButton):


    def __init__(self, texto):

        super().__init__(texto)


        self.setCheckable(False)


        self.setCursor(
            Qt.PointingHandCursor
        )


        self.setStyleSheet(
            """
            QPushButton{

                background:#171717;

                color:white;

                border:none;

                text-align:left;

                padding:14px;

                border-radius:12px;

                font-size:15px;

            }



            QPushButton:hover{

                background:#252525;

            }



            QPushButton:pressed{

                background:#8B5CF6;

                color:white;

            }

            """
        )