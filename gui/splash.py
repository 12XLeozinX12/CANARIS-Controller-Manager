from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    QPropertyAnimation,
    QEasingCurve
)



class SplashScreen(QWidget):

    def __init__(self):

        super().__init__()


        self.setFixedSize(
            500,
            350
        )


        self.setWindowFlags(
            Qt.FramelessWindowHint
        )


        self.setStyleSheet(
            """
            QWidget{
                background:#0f0f0f;
                border-radius:20px;
            }
            """
        )


        self.init_ui()


        self.progresso = 0


        self.timer = QTimer()

        self.timer.timeout.connect(
            self.carregar
        )


        self.timer.start(
            30
        )



    def init_ui(self):


        layout = QVBoxLayout()


        layout.setAlignment(
            Qt.AlignCenter
        )


        self.logo = QLabel(
            "🐤"
        )


        self.logo.setAlignment(
            Qt.AlignCenter
        )


        self.logo.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:70px;
            """
        )



        self.titulo = QLabel(
            "CANARIS ™"
        )


        self.titulo.setAlignment(
            Qt.AlignCenter
        )


        self.titulo.setStyleSheet(
            """
            color:white;
            font-size:35px;
            font-weight:bold;
            """
        )



        self.subtitulo = QLabel(
            "Controller Manager"
        )


        self.subtitulo.setAlignment(
            Qt.AlignCenter
        )


        self.subtitulo.setStyleSheet(
            """
            color:#999;
            font-size:16px;
            """
        )



        self.status = QLabel(
            "Inicializando..."
        )


        self.status.setAlignment(
            Qt.AlignCenter
        )


        self.status.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:14px;
            """
        )



        self.bar = QProgressBar()


        self.bar.setFixedWidth(
            300
        )


        self.bar.setStyleSheet(
            """
            QProgressBar{
                background:#222;
                border-radius:10px;
                height:15px;
                text-align:center;
            }


            QProgressBar::chunk{
                background:#8B5CF6;
                border-radius:10px;
            }
            """
        )



        layout.addWidget(
            self.logo
        )


        layout.addWidget(
            self.titulo
        )


        layout.addWidget(
            self.subtitulo
        )


        layout.addSpacing(
            20
        )


        layout.addWidget(
            self.status
        )


        layout.addWidget(
            self.bar
        )


        self.setLayout(
            layout
        )



        self.animar_logo()



    def animar_logo(self):

        animacao = QPropertyAnimation(
            self.logo,
            b"windowOpacity"
        )


        animacao.setDuration(
            1500
        )


        animacao.setStartValue(
            0
        )


        animacao.setEndValue(
            1
        )


        animacao.setEasingCurve(
            QEasingCurve.OutCubic
        )


        animacao.start()


        self.animacao_logo = animacao



    def carregar(self):

        self.progresso += 1


        self.bar.setValue(
            self.progresso
        )


        mensagens = [

            "Carregando módulos...",
            "Detectando controles...",
            "Preparando interface...",
            "Finalizando..."

        ]


        indice = (
            self.progresso //
            25
        )


        if indice < len(mensagens):

            self.status.setText(
                mensagens[indice]
            )