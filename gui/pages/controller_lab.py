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


        layout.setContentsMargins(
            25,
            25,
            25,
            25
        )



        titulo = QLabel(
            "🎮 CANARIS ™ Controller Lab 2.0"
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





        # ======================
        # VISUAL CONTROLE
        # ======================


        controle_card = self.create_card()


        controle_layout = QVBoxLayout(
            controle_card
        )


        self.visual = ControllerVisual()


        controle_layout.addWidget(
            self.visual
        )


        area.addWidget(
            controle_card,
            2
        )






        # ======================
        # PAINEL
        # ======================


        painel_card = self.create_card()


        painel_layout = QVBoxLayout(
            painel_card
        )



        self.info = QLabel(
            "Procurando controle..."
        )


        self.info.setStyleSheet(
            """
            color:white;
            font-size:16px;
            """
        )


        painel_layout.addWidget(
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



        painel_layout.addWidget(
            self.axis_x
        )


        painel_layout.addWidget(
            self.axis_y
        )


        painel_layout.addWidget(
            self.axis_rx
        )


        painel_layout.addWidget(
            self.axis_ry
        )





        # TRIGGERS


        self.trigger_l2 = TriggerBar(
            "L2"
        )


        self.trigger_r2 = TriggerBar(
            "R2"
        )



        painel_layout.addWidget(
            self.trigger_l2
        )


        painel_layout.addWidget(
            self.trigger_r2
        )





        # VIBRAÇÃO


        self.rumble_button = QPushButton(
            "💥 TESTAR VIBRAÇÃO"
        )


        self.rumble_button.setStyleSheet(
            """
            QPushButton{

                background:#8B5CF6;
                color:white;
                border-radius:12px;
                padding:12px;
                font-size:16px;
                font-weight:bold;

            }


            QPushButton:hover{

                background:#A855F7;

            }
            """
        )



        self.rumble_button.clicked.connect(
            self.testar_vibracao
        )



        painel_layout.addWidget(
            self.rumble_button
        )



        area.addWidget(
            painel_card,
            1
        )



        layout.addLayout(
            area
        )






    def update_controller(self):


        estado = self.manager.get_state()



        info = estado.get(
            "info",
            {}
        )



        if not info.get(
            "connected",
            False
        ):


            self.info.setText(
                "🔴 Nenhum controle conectado"
            )


            self.visual.set_buttons(
                []
            )


            return





        self.info.setText(

f"""
🟢 ONLINE


Nome:

{info.get('nome')}


Tipo:

{info.get('tipo')}


GUID:

{info.get('guid')}

"""

        )





        botoes = estado.get(
            "buttons",
            []
        )


        self.visual.set_buttons(
            botoes
        )



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






        if len(eixos) >= 6:


            self.trigger_l2.set_value(
                eixos[4]
            )


            self.trigger_r2.set_value(
                eixos[5]
            )







    def testar_vibracao(self):


        try:


            sucesso = self.manager.vibrar(
                0.8,
                600
            )



            if sucesso:


                self.info.setText(
                    "💥 Vibração ativada!"
                )


            else:


                self.info.setText(
                    "⚠️ Controle sem vibração"
                )



        except Exception as erro:


            self.info.setText(
                f"Erro vibração: {erro}"
            )