from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton
)

from PySide6.QtCore import QTimer

from core.controller_manager import ControllerManager

from gui.widgets.controller_visual import ControllerVisual
from gui.widgets.axis_bar import AxisBar
from gui.widgets.trigger_bar import TriggerBar



class ControllerLab(QWidget):


    def __init__(self):
        from core.controller_debug import ControllerDebug
        self.debug = ControllerDebug()


        super().__init__()


        self.manager = ControllerManager()


        self.init_ui()



        self.timer = QTimer()


        self.timer.timeout.connect(
            self.update_controller
        )


        self.timer.start(50)







    def create_card(self):

        frame = QFrame()


        frame.setStyleSheet(
            """
            QFrame{
                background:#171717;
                border-radius:20px;
            }
            """
        )


        return frame







    def init_ui(self):


        layout = QVBoxLayout(
            self
        )


        titulo = QLabel(
            "🎮 CANARIS ™ Controller Lab"
        )


        titulo.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:30px;
            font-weight:bold;
            """
        )


        layout.addWidget(
            titulo
        )



        area = QHBoxLayout()





        card_visual = self.create_card()


        visual_layout = QVBoxLayout(
            card_visual
        )


        self.visual = ControllerVisual()


        visual_layout.addWidget(
            self.visual
        )


        area.addWidget(
            card_visual,
            2
        )







        card_info = self.create_card()


        info_layout = QVBoxLayout(
            card_info
        )



        self.info = QLabel(
            "Procurando controle..."
        )


        self.info.setStyleSheet(
            "color:white;font-size:16px;"
        )


        info_layout.addWidget(
            self.info
        )




        self.axis_x = AxisBar(
            "Left Stick X"
        )


        self.axis_y = AxisBar(
            "Left Stick Y"
        )


        self.axis_rx = AxisBar(
            "Right Stick X"
        )


        self.axis_ry = AxisBar(
            "Right Stick Y"
        )



        info_layout.addWidget(
            self.axis_x
        )

        info_layout.addWidget(
            self.axis_y
        )

        info_layout.addWidget(
            self.axis_rx
        )

        info_layout.addWidget(
            self.axis_ry
        )




        self.trigger_l2 = TriggerBar(
            "L2"
        )


        self.trigger_r2 = TriggerBar(
            "R2"
        )


        info_layout.addWidget(
            self.trigger_l2
        )


        info_layout.addWidget(
            self.trigger_r2
        )





        self.rumble = QPushButton(
            "💥 TESTAR VIBRAÇÃO"
        )


        self.rumble.clicked.connect(
            self.testar_vibracao
        )


        info_layout.addWidget(
            self.rumble
        )




        area.addWidget(
            card_info,
            1
        )



        layout.addLayout(
            area
        )









    def update_controller(self):


        estado = self.manager.get_state()



        if not estado["info"].get(
            "connected",
            False
        ):


            self.info.setText(
                "🔴 Nenhum controle conectado"
            )


            self.visual.set_buttons(
                {}
            )


            return






        self.info.setText(

            f"""
🟢 ONLINE


Nome:
{estado['info']['nome']}


Tipo:
{estado['info']['tipo']}


GUID:
{estado['info']['guid']}
"""

        )




        # =====================
        # BOTÕES
        # =====================


        self.visual.set_buttons(

            estado.get(
                "buttons",
                {}
            )

        )




        # =====================
        # EIXOS
        # =====================


        eixos = estado.get(
            "axes",
            []
        )


        self.visual.set_axes(
            eixos
        )




        if len(eixos) >= 4:


            self.axis_x.set_value(
                eixos[0]
            )


            self.axis_y.set_value(
                eixos[1]
            )


            self.axis_rx.set_value(
                eixos[2]
            )


            self.axis_ry.set_value(
                eixos[3]
            )





        triggers = estado.get(
            "triggers",
            {}
        )


        self.trigger_l2.set_value(
            triggers.get(
                "L2",
                0
            )
        )


        self.trigger_r2.set_value(
            triggers.get(
                "R2",
                0
            )
        )








    def testar_vibracao(self):


        self.manager.vibrar(
            0.8,
            600
        )