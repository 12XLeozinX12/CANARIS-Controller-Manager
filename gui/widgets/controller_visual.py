from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QColor,
    QBrush,
    QPen,
    QFont
)
from PySide6.QtCore import Qt





class ControllerVisual(QWidget):


    def __init__(self):

        super().__init__()


        self.state = {

            "buttons": {},
            "axes": {},
            "triggers": {},
            "type": "Generic"

        }


        self.setMinimumSize(
            700,
            420
        )



        self.setStyleSheet(
            """
            QWidget{

                background:#0A0A0F;

                border-radius:25px;

            }

            """
        )






    # ============================
    # RECEBE ESTADO
    # ============================


    def update_state(self,state):


        if state:


            self.state = state


            self.update()







    def button_pressed(self,index):


        return self.state.get(

            "buttons",

            {}

        ).get(

            index,

            False

        )







    # ============================
    # DESENHO PRINCIPAL
    # ============================


    def paintEvent(self,event):


        painter = QPainter(self)


        painter.setRenderHint(

            QPainter.Antialiasing

        )



        w=self.width()



        # corpo


        painter.setBrush(

            QColor("#161622")

        )


        painter.setPen(

            QPen(

                QColor("#8B5CF6"),

                3

            )

        )



        painter.drawRoundedRect(

            120,

            90,

            w-240,

            230,

            70,

            70

        )





        # alças


        painter.setBrush(

            QColor("#161622")

        )



        painter.drawEllipse(

            70,

            210,

            130,

            120

        )



        painter.drawEllipse(

            w-200,

            210,

            130,

            120

        )






        self.draw_stick(

            painter,

            230,

            220,

            "LX",

            "LY"

        )



        self.draw_stick(

            painter,

            w-230,

            220,

            "RX",

            "RY"

        )





        if self.state.get("type")=="PlayStation":


            self.playstation(

                painter

            )


        else:


            self.xbox(

                painter

            )





        self.draw_trigger(

            painter,

            160,

            120,

            "L2"

        )


        self.draw_trigger(

            painter,

            w-160,

            120,

            "R2"

        )







    # ============================
    # BOTÕES XBOX
    # ============================


    def xbox(self,p):


        w=self.width()



        self.draw_button(

            p,

            "Y",

            w-170,

            155,

            3

        )


        self.draw_button(

            p,

            "X",

            w-210,

            200,

            2

        )


        self.draw_button(

            p,

            "B",

            w-130,

            200,

            1

        )


        self.draw_button(

            p,

            "A",

            w-170,

            245,

            0

        )








    # ============================
    # PLAYSTATION
    # ============================


    def playstation(self,p):


        w=self.width()



        self.draw_button(

            p,

            "△",

            w-170,

            155,

            3

        )


        self.draw_button(

            p,

            "□",

            w-210,

            200,

            2

        )


        self.draw_button(

            p,

            "○",

            w-130,

            200,

            1

        )


        self.draw_button(

            p,

            "✕",

            w-170,

            245,

            0

        )








    # ============================
    # BOTÃO
    # ============================


    def draw_button(

            self,

            p,

            texto,

            x,

            y,

            index

    ):


        ativo=self.button_pressed(

            index

        )



        cor = (

            "#8B5CF6"

            if ativo

            else

            "#252533"

        )



        p.setBrush(

            QColor(cor)

        )


        p.setPen(

            QPen(

                QColor("#AAAAAA"),

                1

            )

        )


        p.drawEllipse(

            x-24,

            y-24,

            48,

            48

        )



        p.setPen(

            QColor("white")

        )


        p.setFont(

            QFont(

                "Segoe UI",

                15,

                QFont.Bold

            )

        )


        p.drawText(

            x-8,

            y+6,

            texto

        )







    # ============================
    # ANALÓGICO
    # ============================


    def draw_stick(

            self,

            p,

            x,

            y,

            ax,

            ay

    ):



        axes=self.state.get(

            "axes",

            {}

        )


        dx=axes.get(

            ax,

            0

        )*30



        dy=axes.get(

            ay,

            0

        )*30






        p.setBrush(

            QColor("#20202B")

        )


        p.setPen(

            QPen(

                QColor("#8B5CF6"),

                2

            )

        )



        p.drawEllipse(

            x-45,

            y-45,

            90,

            90

        )



        p.setBrush(

            QColor("#8B5CF6")

        )


        p.drawEllipse(

            x-15+dx,

            y-15+dy,

            30,

            30

        )







    # ============================
    # GATILHO
    # ============================


    def draw_trigger(

            self,

            p,

            x,

            y,

            nome

    ):


        valor=self.state.get(

            "triggers",

            {}

        ).get(

            nome,

            0

        )



        p.setBrush(

            QColor("#22222E")

        )


        p.setPen(Qt.NoPen)


        p.drawRoundedRect(

            x-40,

            y,

            80,

            15,

            8,

            8

        )



        p.setBrush(

            QColor("#8B5CF6")

        )


        p.drawRoundedRect(

            x-40,

            y,

            int(80*valor/100),

            15,

            8,

            8

        )