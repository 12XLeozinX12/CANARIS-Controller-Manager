from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QGraphicsDropShadowEffect
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    QPropertyAnimation,
    QEasingCurve
)

from PySide6.QtGui import QFont





class NotificationWidget(QWidget):


    def __init__(
        self,
        mensagem,
        tipo="info",
        duracao=3500
    ):

        super().__init__()


        self.duracao = duracao



        self.setWindowFlags(

            Qt.FramelessWindowHint |

            Qt.Tool |

            Qt.WindowStaysOnTopHint

        )


        self.setAttribute(

            Qt.WA_TranslucentBackground

        )





        cores = {

            "success": "#22C55E",

            "info": "#8B5CF6",

            "warning": "#EAB308",

            "error": "#EF4444"

        }


        icones = {

            "success": "✔",

            "info": "🔔",

            "warning": "⚠",

            "error": "✖"

        }


        titulos = {

            "success": "Sucesso",

            "info": "CANARIS",

            "warning": "Aviso",

            "error": "Erro"

        }



        cor = cores.get(

            tipo,

            "#8B5CF6"

        )







        # =========================
        # FUNDO PRINCIPAL
        # =========================


        fundo = QWidget()


        fundo.setObjectName(

            "Card"

        )



        sombra = QGraphicsDropShadowEffect()


        sombra.setBlurRadius(

            35

        )


        sombra.setOffset(

            0,

            6

        )


        sombra.setColor(

            cor

        )


        fundo.setGraphicsEffect(

            sombra

        )





        principal = QHBoxLayout(

            self

        )


        principal.setContentsMargins(

            8,

            8,

            8,

            8

        )


        principal.addWidget(

            fundo

        )





        layout = QHBoxLayout(

            fundo

        )


        layout.setContentsMargins(

            16,

            14,

            20,

            14

        )


        layout.setSpacing(

            12

        )







        barra = QLabel()


        barra.setFixedWidth(

            5

        )


        barra.setStyleSheet(

            f"""

            background:{cor};

            border-radius:3px;

            """

        )


        layout.addWidget(

            barra

        )







        icone = QLabel(

            icones.get(

                tipo,

                "🔔"

            )

        )


        icone.setFont(

            QFont(

                "Segoe UI",

                20

            )

        )


        icone.setStyleSheet(

            """

            color:white;

            background:transparent;

            """

        )


        layout.addWidget(

            icone

        )







        textos = QVBoxLayout()





        titulo = QLabel(

            titulos.get(

                tipo,

                "CANARIS"

            )

        )


        titulo.setFont(

            QFont(

                "Segoe UI",

                11,

                QFont.Bold

            )

        )


        titulo.setStyleSheet(

            """

            color:white;

            background:transparent;

            """

        )







        texto = QLabel(

            mensagem

        )


        texto.setFont(

            QFont(

                "Segoe UI",

                10

            )

        )


        texto.setStyleSheet(

            """

            color:#B0B0B0;

            background:transparent;

            """

        )






        textos.addWidget(

            titulo

        )


        textos.addWidget(

            texto

        )



        layout.addLayout(

            textos

        )







        fundo.setStyleSheet(

            f"""

            QWidget#Card{{

                background:#0B0B0F;

                border-radius:18px;

                border:1px solid {cor};

            }}

            """

        )







    def mostrar(self):


        self.setWindowOpacity(

            0

        )


        self.show()



        self.animacao = QPropertyAnimation(

            self,

            b"windowOpacity"

        )


        self.animacao.setDuration(

            350

        )


        self.animacao.setStartValue(

            0

        )


        self.animacao.setEndValue(

            1

        )


        self.animacao.setEasingCurve(

            QEasingCurve.OutCubic

        )


        self.animacao.start()





        QTimer.singleShot(

            self.duracao,

            self.fechar

        )







    def fechar(self):


        self.animacao_saida = QPropertyAnimation(

            self,

            b"windowOpacity"

        )


        self.animacao_saida.setDuration(

            300

        )


        self.animacao_saida.setStartValue(

            1

        )


        self.animacao_saida.setEndValue(

            0

        )


        self.animacao_saida.finished.connect(

            self.close

        )


        self.animacao_saida.start()











class NotificationManager:



    def __init__(self):

        self.app = None

        self.ativas = []







    def conectar_app(

        self,

        app

    ):

        self.app = app







    def mostrar(

        self,

        mensagem,

        tipo="info"

    ):


        # =========================
        # SOM
        # =========================

        try:

            from core.sound_manager import sound

            sound.play(

                "notification"

            )

        except Exception:

            pass






        widget = NotificationWidget(

            mensagem,

            tipo

        )


        widget.adjustSize()



        self.ativas.append(

            widget

        )






        if self.app:


            area = self.app.primaryScreen().availableGeometry()



            x = (

                area.right()

                -

                widget.width()

                -

                40

            )


            y = (

                area.bottom()

                -

                widget.height()

                -

                50

            )



            widget.move(

                x,

                y

            )






        widget.mostrar()






        QTimer.singleShot(

            5000,

            lambda:

            self.remover(widget)

        )








    def remover(

        self,

        widget

    ):


        if widget in self.ativas:

            self.ativas.remove(

                widget

            )







    def success(self, mensagem):

        self.mostrar(

            mensagem,

            "success"

        )






    def info(self, mensagem):

        self.mostrar(

            mensagem,

            "info"

        )






    def warning(self, mensagem):

        self.mostrar(

            mensagem,

            "warning"

        )






    def error(self, mensagem):

        self.mostrar(

            mensagem,

            "error"

        )








notification = NotificationManager()