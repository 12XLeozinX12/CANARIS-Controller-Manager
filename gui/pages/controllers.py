from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QFrame,
    QInputDialog
)

from PySide6.QtCore import Qt, QTimer

from core.language_manager import language
from gui.widgets.notification import notification
from core.profile_manager import ProfileManager


class Controllers(QWidget):


    def __init__(
        self,
        controller_manager
    ):

        super().__init__()


        self.controller_manager = controller_manager

        self.profile_manager = ProfileManager()


        self.setup_ui()



        language.idioma_alterado.connect(
            self.atualizar_textos
        )



        self.lista.itemClicked.connect(
            self.selecionar_controle
        )



        self.timer = QTimer(self)


        self.timer.timeout.connect(
            self.atualizar_status
        )


        self.timer.start(
            800
        )



        self.atualizar_textos()

        self.carregar_controles()





    # =========================
    # UI
    # =========================


    def setup_ui(self):


        self.setObjectName(
            "ControllersPage"
        )



        self.setStyleSheet("""


        QWidget#ControllersPage{


            background:#050507;


        }



        QLabel{


            color:#F8FAFC;


        }




        QFrame{


            background:#0B0B12;

            border:none;

            border-radius:20px;


        }





        QPushButton{


            background:#11111A;

            color:white;

            border:none;

            border-radius:12px;

            padding:12px;


        }





        QPushButton:hover{


            background:#8B5CF6;


        }






        QListWidget{


            background:#08080D;

            color:white;

            border:none;

            border-radius:16px;

            font-size:16px;

            outline:none;


        }





        QListWidget:focus{


            border:none;

            outline:none;


        }





        QListWidget::item{


            padding:14px;

            border:none;


        }





        QListWidget::item:hover{


            background:#151522;


        }






        QListWidget::item:selected{


            background:#8B5CF6;

            border:none;


        }




        """)





        layout = QVBoxLayout(
            self
        )



        layout.setContentsMargins(
            35,
            35,
            35,
            35
        )



        layout.setSpacing(
            20
        )




        # TITULO


        self.titulo = QLabel()



        self.titulo.setStyleSheet("""


        color:#A855F7;

        font-size:34px;

        font-weight:bold;


        """)





        self.descricao = QLabel()



        self.descricao.setStyleSheet("""


        color:#64748B;

        font-size:16px;


        """)





        layout.addWidget(
            self.titulo
        )


        layout.addWidget(
            self.descricao
        )




        # CARD STATUS


        self.card = QFrame()



        card_layout = QVBoxLayout(
            self.card
        )



        card_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )




        self.status = QLabel()



        self.status.setStyleSheet("""


        font-size:20px;

        font-weight:bold;


        """)




        self.nome = QLabel()

        self.tipo = QLabel()

        self.guid = QLabel()





        card_layout.addWidget(
            self.status
        )



        card_layout.addWidget(
            self.nome
        )



        card_layout.addWidget(
            self.tipo
        )



        card_layout.addWidget(
            self.guid
        )




        layout.addWidget(
            self.card
        )


        # =========================
        # LISTA DE CONTROLES
        # =========================


        self.lista = QListWidget()


        self.lista.setFocusPolicy(
            Qt.NoFocus
        )


        layout.addWidget(
            self.lista
        )



        # =========================
        # BOTÃO ATUALIZAR
        # =========================


        self.btn_atualizar = QPushButton()


        self.btn_atualizar.clicked.connect(
            self.carregar_controles
        )



        # =========================
        # BOTÃO PERFIL
        # =========================


        self.btn_perfil = QPushButton()


        self.btn_perfil.clicked.connect(
            self.criar_perfil
        )



        layout.addWidget(
            self.btn_atualizar
        )


        layout.addWidget(
            self.btn_perfil
        )







    # =========================
    # IDIOMA
    # =========================


    def atualizar_textos(self):



        self.titulo.setText(

            "🎮 " +

            language.texto(
                "controles_titulo"
            )

        )



        self.descricao.setText(

            language.texto(
                "controles_descricao"
            )

        )



        self.btn_atualizar.setText(

            "🔄 " +

            language.texto(
                "atualizar"
            )

        )



        self.btn_perfil.setText(

            "👤 " +

            language.texto(
                "perfil"
            )

        )





    # =========================
    # CARREGAR CONTROLES
    # =========================


    def carregar_controles(self):


        self.lista.clear()



        try:


            controles = (

                self.controller_manager
                .get_devices()

            )



            if not controles:


                self.lista.addItem(

                    "❌ " +

                    language.texto(
                        "nenhum_controle"
                    )

                )

                return





            for controle in controles:



                nome = controle.get(
                    "name",
                    "Generic"
                )



                tipo = controle.get(
                    "type",
                    "Generic"
                )



                item = QListWidgetItem(


                    "🎮 "

                    +

                    nome

                    +

                    "\n"

                    +

                    tipo


                )



                item.setData(

                    Qt.UserRole,

                    controle["id"]

                )



                self.lista.addItem(
                    item
                )





        except Exception as erro:



            notification.error(
                str(erro)
            )






    # =========================
    # SELEÇÃO
    # =========================


    def selecionar_controle(
        self,
        item
    ):


        indice = item.data(
            Qt.UserRole
        )



        if indice is None:

            return





        try:



            sucesso = (

                self.controller_manager
                .selecionar_controle(
                    indice
                )

            )



            if sucesso:



                notification.success(

                    language.texto(
                        "controle_selecionado"
                    )

                )





        except Exception as erro:



            notification.error(
                str(erro)
            )
    # =========================
    # STATUS
    # =========================


    def atualizar_status(self):


        try:


            estado = (

                self.controller_manager
                .get_state()

            )



            if estado["connected"]:



                self.status.setText(

                    "🟢 " +

                    language.texto(
                        "controle_conectado"
                    )

                )



                self.status.setStyleSheet("""


                color:#22C55E;

                font-size:20px;

                font-weight:bold;


                """)





                self.nome.setText(

                    language.texto(
                        "nome"
                    )

                    +

                    ": "

                    +

                    estado["name"]

                )




                self.tipo.setText(

                    language.texto(
                        "tipo"
                    )

                    +

                    ": "

                    +

                    estado["type"]

                )





                self.guid.setText(

                    language.texto(
                        "guid"
                    )

                    +

                    ": "

                    +

                    estado["guid"]

                )





            else:




                self.status.setText(

                    "🔴 "

                    +

                    language.texto(
                        "nenhum_controle"
                    )

                )



                self.status.setStyleSheet("""


                color:#EF4444;

                font-size:20px;

                font-weight:bold;


                """)





                self.nome.setText("-")

                self.tipo.setText("-")

                self.guid.setText("-")






        except:


            pass







    # =========================
    # CRIAR PERFIL
    # =========================

    def criar_perfil(self):

        estado = (

            self.controller_manager
            .get_state()

        )

        if not estado["connected"]:
            notification.warning(

                language.texto(
                    "conecte_controle"
                )

            )

            return

        nome, ok = QInputDialog.getText(

            self,

            "CANARIS ™",

            language.texto(
                "nome_perfil"
            )

        )

        if ok and nome:

            perfil = {

                "name": nome,

                "type": estado["type"],

                "guid": estado["guid"],

                "controller": {

                    "axes":

                        estado.get(
                            "axes_count",
                            0
                        ),

                    "buttons":

                        estado.get(
                            "buttons_count",
                            0
                        )

                },

                "calibration": {

                    "deadzone_left": 0.08,

                    "deadzone_right": 0.08

                },

                "mapping": {},

                "statistics": {

                    "hours": 0

                }

            }

            try:

                self.profile_manager.create_profile(

                    perfil

                )

                notification.success(

                    language.texto(
                        "perfil_criado"
                    )

                )


            except Exception as erro:

                notification.error(

                    str(erro)

                )









    # =========================
    # SHOW EVENT
    # =========================


    def showEvent(
        self,
        event
    ):


        super().showEvent(
            event
        )



        self.carregar_controles()



        self.atualizar_status()
