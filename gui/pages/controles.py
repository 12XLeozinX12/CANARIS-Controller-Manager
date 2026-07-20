from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QFrame
)

from core.controller_manager import ControllerManager
from core.language_manager import language



class Controles(QWidget):


    def __init__(self):

        super().__init__()


        self.controller_manager = ControllerManager()


        self.init_ui()


        language.idioma_alterado.connect(
            self.atualizar_textos
        )


        self.atualizar_controles()



    def init_ui(self):


        layout = QVBoxLayout()


        layout.setContentsMargins(
            25,
            25,
            25,
            25
        )


        self.titulo = QLabel()


        self.titulo.setStyleSheet(
            """
            color:white;
            font-size:28px;
            font-weight:bold;
            """
        )


        layout.addWidget(
            self.titulo
        )



        self.subtitulo = QLabel()


        self.subtitulo.setStyleSheet(
            """
            color:#999;
            font-size:14px;
            """
        )


        layout.addWidget(
            self.subtitulo
        )



        area = QHBoxLayout()



        lista_frame = QFrame()


        lista_frame.setStyleSheet(
            """
            QFrame{
                background:#171717;
                border-radius:15px;
            }
            """
        )


        lista_layout = QVBoxLayout(
            lista_frame
        )



        self.titulo_lista = QLabel()


        self.titulo_lista.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:18px;
            font-weight:bold;
            """
        )


        lista_layout.addWidget(
            self.titulo_lista
        )



        self.lista = QListWidget()


        lista_layout.addWidget(
            self.lista
        )



        area.addWidget(
            lista_frame,
            1
        )



        info_frame = QFrame()


        info_frame.setStyleSheet(
            """
            QFrame{
                background:#171717;
                border-radius:15px;
            }
            """
        )


        info_layout = QVBoxLayout(
            info_frame
        )



        self.titulo_info = QLabel()


        self.titulo_info.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:18px;
            font-weight:bold;
            """
        )


        info_layout.addWidget(
            self.titulo_info
        )



        self.info = QLabel()


        self.info.setStyleSheet(
            """
            color:white;
            font-size:15px;
            """
        )


        info_layout.addWidget(
            self.info
        )



        self.status = QLabel()


        self.status.setStyleSheet(
            """
            color:#ff4444;
            font-size:18px;
            font-weight:bold;
            """
        )


        info_layout.addWidget(
            self.status
        )



        self.atualizar = QPushButton()


        self.atualizar.clicked.connect(
            self.atualizar_controles
        )


        info_layout.addWidget(
            self.atualizar
        )


        info_layout.addStretch()



        area.addWidget(
            info_frame,
            2
        )



        layout.addLayout(
            area
        )


        self.setLayout(
            layout
        )


        self.atualizar_textos()




    def atualizar_textos(self):


        self.titulo.setText(
            "🎮 " +
            language.texto(
                "controles_titulo"
            )
        )


        self.subtitulo.setText(
            language.texto(
                "controles_descricao"
            )
        )


        self.titulo_lista.setText(
            language.texto(
                "controles_detectados"
            )
        )


        self.titulo_info.setText(
            language.texto(
                "informacoes"
            )
        )


        self.atualizar.setText(
            language.texto(
                "atualizar"
            )
        )



    def atualizar_controles(self):


        self.lista.clear()


        controles = (
            self.controller_manager
            .detectar_controles()
        )


        if not controles:


            self.lista.addItem(
                language.texto(
                    "nenhum_controle"
                )
            )


            self.info.setText(
                language.texto(
                    "nenhum_controle"
                )
            )


            self.status.setText(
                "● OFFLINE"
            )


            return



        for controle in controles:


            item = QListWidgetItem(

                "🎮 " +
                controle["nome"]

            )


            self.lista.addItem(
                item
            )



        primeiro = controles[0]


        self.info.setText(

            f"""
Controller:

{primeiro['nome']}


ID:

{primeiro['id']}


Buttons:

{primeiro['botoes']}


Axes:

{primeiro['eixos']}
"""

        )


        self.status.setText(
            "● ONLINE"
        )


        self.status.setStyleSheet(
            """
            color:#00D26A;
            font-size:18px;
            font-weight:bold;
            """
        )