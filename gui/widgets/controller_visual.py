from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt



class ControllerVisual(QWidget):


    def __init__(self):

        super().__init__()


        self.setMinimumSize(
            500,
            350
        )


        self.pressed_buttons = []


        self.axes = [
            0,
            0,
            0,
            0
        ]





    def set_buttons(
        self,
        buttons
    ):


        self.pressed_buttons = buttons


        self.update()





    def set_axes(
        self,
        axes
    ):


        if len(axes) >= 4:


            self.axes = [

                axes[0],

                axes[1],

                axes[2],

                axes[3]

            ]


        self.update()






    def is_pressed(
        self,
        button
    ):


        return button in self.pressed_buttons






    def draw_button(
        self,
        painter,
        x,
        y,
        radius,
        text,
        index
    ):


        if self.is_pressed(index):


            painter.setBrush(
                QColor(
                    "#8B5CF6"
                )
            )


        else:


            painter.setBrush(
                QColor(
                    "#252525"
                )
            )



        painter.setPen(
            QPen(
                QColor("#FFFFFF"),
                2
            )
        )


        painter.drawEllipse(

            x-radius,

            y-radius,

            radius*2,

            radius*2

        )



        painter.setPen(
            QColor(
                "#FFFFFF"
            )
        )


        painter.drawText(
            x-10,
            y+5,
            text
        )







    def paintEvent(
        self,
        event
    ):


        painter = QPainter(
            self
        )


        painter.setRenderHint(
            QPainter.Antialiasing
        )



        # Corpo


        painter.setBrush(
            QColor("#151515")
        )


        painter.setPen(
            QPen(
                QColor("#333333"),
                3
            )
        )


        painter.drawRoundedRect(
            80,
            50,
            340,
            220,
            80,
            80
        )





        # ======================
        # BOTÕES
        # ======================


        self.draw_button(
            painter,
            330,
            120,
            22,
            "△",
            3
        )


        self.draw_button(
            painter,
            370,
            160,
            22,
            "○",
            1
        )


        self.draw_button(
            painter,
            290,
            160,
            22,
            "□",
            2
        )


        self.draw_button(
            painter,
            330,
            200,
            22,
            "✕",
            0
        )





        # ======================
        # ANALÓGICOS
        # ======================


        # LEFT STICK


        left_x = (
            177 +
            self.axes[0] * 20
        )


        left_y = (
            177 +
            self.axes[1] * 20
        )



        painter.setBrush(
            QColor("#303030")
        )


        painter.drawEllipse(
            145,
            145,
            65,
            65
        )



        painter.setBrush(
            QColor("#8B5CF6")
        )


        painter.drawEllipse(
            left_x-15,
            left_y-15,
            30,
            30
        )




        # RIGHT STICK


        right_x = (
            277 +
            self.axes[2] * 20
        )


        right_y = (
            237 +
            self.axes[3] * 20
        )



        painter.setBrush(
            QColor("#303030")
        )


        painter.drawEllipse(
            245,
            205,
            65,
            65
        )


        painter.setBrush(
            QColor("#8B5CF6")
        )


        painter.drawEllipse(
            right_x-15,
            right_y-15,
            30,
            30
        )





        # L3 / R3


        self.draw_button(
            painter,
            177,
            177,
            12,
            "L3",
            7
        )


        self.draw_button(
            painter,
            277,
            237,
            12,
            "R3",
            8
        )





        # Ombros


        self.draw_button(
            painter,
            130,
            70,
            18,
            "L1",
            9
        )


        self.draw_button(
            painter,
            370,
            70,
            18,
            "R1",
            5
        )