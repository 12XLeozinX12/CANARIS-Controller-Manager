# ==========================================================
# CANARIS Controller Manager 21.0
# Controller Lab Interface
# ==========================================================


from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame
)

from PySide6.QtCore import (
    QTimer
)

from PySide6.QtGui import (
    QFont
)


from core.controller_engine import ControllerEngine



# Tradução CANARIS

try:

    from core.language_manager import language


except:


    language = None



# Notificações CANARIS

try:

    from gui.widgets.notification import NotificationManager

except:

    NotificationManager = None





# ==========================================================
# CARD
# ==========================================================

class CanarisCard(QFrame):


    def __init__(
        self,
        title
    ):


        super().__init__()


        self.setObjectName(
            "CanarisCard"
        )


        self.layout = QVBoxLayout()


        self.title = QLabel(
            title
        )


        self.title.setFont(
            QFont(
                "Segoe UI",
                12,
                QFont.Bold
            )
        )


        self.layout.addWidget(
            self.title
        )


        self.setLayout(
            self.layout
        )





# ==========================================================
# CONTROLLER LAB
# ==========================================================

class ControllerLab(QWidget):


    def __init__(self):


        super().__init__()



        # ENGINE

        self.engine = ControllerEngine()



        self.last_connection = False

        self.create_ui()

        language.idioma_alterado.connect(

            self.update_texts

        )



        self.timer = QTimer(
            self
        )


        self.timer.timeout.connect(
            self.update_interface
        )


        self.timer.start(
            50
        )



        self.apply_style()





    # ======================================================
    # UI
    # ======================================================


    def create_ui(self):


        main = QVBoxLayout(
            self
        )

        self.header = QLabel()

        self.header.setFont(
            QFont(
                "Segoe UI",
                24,
                QFont.Bold
            )
        )

        self.subtitle = QLabel()

        main.addWidget(
            self.header
        )

        main.addWidget(
            self.subtitle
        )


        # STATUS


        self.status_card = CanarisCard(
            "Controller Status"
        )


        self.status_label = QLabel(
            "🔴 No Controller"
        )


        self.status_card.layout.addWidget(
            self.status_label
        )



        main.addWidget(
            self.status_card
        )




        # BODY


        body = QHBoxLayout()



        # BUTTONS


        self.buttons_card = CanarisCard(
            "Buttons"
        )


        self.buttons_grid = QGridLayout()



        self.button_labels = []



        for i in range(16):


            label = QLabel(
                f"B{i}: ---"
            )


            self.button_labels.append(
                label
            )


            self.buttons_grid.addWidget(
                label,
                i // 4,
                i % 4
            )



        self.buttons_card.layout.addLayout(
            self.buttons_grid
        )



        # AXIS


        self.axis_card = CanarisCard(
            "Analog / Triggers"
        )


        self.axis_labels = []



        for i in range(8):


            label = QLabel(
                f"Axis {i}: 0.00"
            )


            self.axis_labels.append(
                label
            )


            self.axis_card.layout.addWidget(
                label
            )



        body.addWidget(
            self.buttons_card
        )


        body.addWidget(
            self.axis_card
        )



        main.addLayout(
            body
        )



        # D-PAD


        self.hat_card = CanarisCard(
            "D-Pad"
        )


        self.hat_label = QLabel(
            "HAT: (0,0)"
        )


        self.hat_card.layout.addWidget(
            self.hat_label
        )

        main.addWidget(
            self.hat_card
        )

        # Aplicar tradução inicial
        self.update_texts()
        
    # ======================================================
    # TRADUÇÃO
    # ======================================================

    def update_texts(self):

        self.header.setText(

            "🎮 " +

            language.texto(

                "controller_lab_titulo"

            )

        )

        self.subtitle.setText(

            language.texto(

                "controller_lab_subtitulo"

            )

        )

        self.status_card.title.setText(

            language.texto(

                "controller_status"

            )

        )

        self.buttons_card.title.setText(

            language.texto(

                "controller_botoes"

            )

        )

        self.axis_card.title.setText(

            language.texto(

                "controller_eixos"

            )

        )

        self.hat_card.title.setText(

            language.texto(

                "controller_dpad"

            )

        )


    # ======================================================
    # UPDATE
    # ======================================================


    def update_interface(self):


        self.engine.update()



        state = self.engine.get_state()



        connected = state["connected"]



        # CONNECTION EVENT


        if connected != self.last_connection:


            if connected:


                self.notify(
                    "CANARIS",
                    "Controller conectado"
                )


            else:


                self.notify(
                    "CANARIS",
                    "Controller desconectado"
                )



            self.last_connection = connected




        # STATUS


        if connected:


            self.status_label.setText(

                f"🟢 {state['name']}"

            )


        else:


            self.status_label.setText(

                "🔴 No Controller Connected"

            )



        # BUTTONS


        buttons = state["buttons"]



        for i in range(16):


            if i < len(buttons):


                self.button_labels[i].setText(

                    f"B{i}: {'🟢 ON' if buttons[i] else '---'}"

                )

            else:


                self.button_labels[i].setText(

                    f"B{i}: N/A"

                )




        # AXIS


        axes = state["axes"]



        for i in range(8):


            if i < len(axes):


                self.axis_labels[i].setText(

                    f"Axis {i}: {axes[i]}"

                )


            else:


                self.axis_labels[i].setText(

                    f"Axis {i}: N/A"

                )




        # TRIGGERS


        triggers = state["triggers"]



        if len(axes):


            self.axis_labels[6].setText(

                f"L2: {triggers['L2']}"

            )


            self.axis_labels[7].setText(

                f"R2: {triggers['R2']}"

            )




        # HAT


        self.hat_label.setText(

            f"HAT: {state['hat']}"

        )






    # ======================================================
    # NOTIFICATION
    # ======================================================


    def notify(
        self,
        title,
        message
    ):


        if NotificationManager:


            try:


                NotificationManager.send(
                    title,
                    message
                )


            except:

                pass





    # ======================================================
    # STYLE
    # ======================================================


    def apply_style(self):


        self.setStyleSheet(

        """

        QWidget
        {
            background:#0d1117;
            color:#eeeeee;
            font-family:"Segoe UI";
        }


        QFrame#CanarisCard
        {
            background:#161b22;
            border-radius:14px;
            border:1px solid #30363d;
            padding:10px;
        }


        QLabel
        {
            color:#e6edf3;
        }


        """

        )