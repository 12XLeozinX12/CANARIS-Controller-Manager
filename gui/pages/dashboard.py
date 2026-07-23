from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton
)

from PySide6.QtCore import Qt

from core.language_manager import language
from gui.widgets.notification import notification
from database.profile import GamerProfile


class Dashboard(QWidget):


    def __init__(self, main_window=None):

        super().__init__()


        self.main_window = main_window


        self.profile_manager = GamerProfile()


        self.usuario = None

        self.setup_ui()

        language.idioma_alterado.connect(
            self.atualizar_textos
        )

        self.atualizar_textos()

        self.carregar_usuario()

    # =====================================================
    # INTERFACE
    # =====================================================

    def setup_ui(self):

        self.setObjectName(
            "DashboardPage"
        )

        self.setStyleSheet("""


        QWidget#DashboardPage{

            background:#050507;

        }



        QLabel{

            color:white;

        }



        QFrame{

            background:#0B0B12;

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


        """)

        main = QVBoxLayout(
            self
        )

        main.setContentsMargins(
            35,
            35,
            35,
            35
        )

        main.setSpacing(
            20
        )

        # =====================================
        # HEADER
        # =====================================

        self.titulo = QLabel()

        self.titulo.setStyleSheet("""

        color:#A855F7;

        font-size:34px;

        font-weight:bold;

        """)

        self.subtitulo = QLabel()

        self.subtitulo.setStyleSheet("""

        color:#9CA3AF;

        font-size:15px;

        """)

        main.addWidget(
            self.titulo
        )

        main.addWidget(
            self.subtitulo
        )

        # =====================================
        # PERFIL LOGADO
        # =====================================

        self.user_box = QFrame()

        user_layout = QVBoxLayout(
            self.user_box
        )

        self.user_name = QLabel()

        self.user_name.setStyleSheet("""
        color:#A855F7;
        font-size:22px;
        font-weight:bold;
        """)

        self.user_info = QLabel()

        self.user_info.setStyleSheet("""
        color:#D4D4D8;
        font-size:14px;
        """)

        user_layout.addWidget(
            self.user_name
        )

        user_layout.addWidget(
            self.user_info
        )

        main.addWidget(
            self.user_box
        )

        # =====================================
        # STATUS CARDS
        # =====================================

        cards = QHBoxLayout()

        cards.setSpacing(
            20
        )

        self.card_controle = self.card(
            "🎮"
        )

        self.card_perfil = self.card(
            "📁"
        )

        self.card_calibracao = self.card(
            "🎯"
        )

        self.card_sistema = self.card(
            "🟢"
        )

        cards.addWidget(
            self.card_controle
        )

        cards.addWidget(
            self.card_perfil
        )

        cards.addWidget(
            self.card_calibracao
        )

        cards.addWidget(
            self.card_sistema
        )

        main.addLayout(
            cards
        )

        # =====================================
        # PAINEL DE STATUS
        # =====================================

        self.status_box = QFrame()

        status_layout = QVBoxLayout(
            self.status_box
        )

        self.status_title = QLabel()

        self.status_title.setStyleSheet("""

        color:#A855F7;

        font-size:18px;

        font-weight:bold;

        """)

        self.status_controle = QLabel()

        self.status_perfil = QLabel()

        self.status_idioma = QLabel()

        self.status_calibracao = QLabel()

        self.status_update = QLabel()

        for item in [

            self.status_controle,

            self.status_perfil,

            self.status_idioma,

            self.status_calibracao,

            self.status_update

        ]:
            item.setStyleSheet("""

            color:#D4D4D8;

            font-size:14px;

            """)

            status_layout.addWidget(
                item
            )

        status_layout.insertWidget(
            0,
            self.status_title
        )

        main.addWidget(
            self.status_box
        )

        # =====================================
        # TESTE
        # =====================================

        self.btn_notify = QPushButton()

        self.btn_notify.clicked.connect(
            self.testar_notificacao
        )

        main.addWidget(
            self.btn_notify
        )

        main.addStretch()

    # =====================================================
    # CARD
    # =====================================================

    def card(self, emoji):

        frame = QFrame()

        frame.setMinimumHeight(
            150
        )

        layout = QVBoxLayout(
            frame
        )

        layout.setAlignment(
            Qt.AlignCenter
        )

        icon = QLabel(
            emoji
        )

        icon.setAlignment(
            Qt.AlignCenter
        )

        icon.setStyleSheet("""

        font-size:42px;

        """)

        texto = QLabel()

        texto.setAlignment(
            Qt.AlignCenter
        )

        texto.setStyleSheet("""

        font-size:17px;

        font-weight:bold;

        """)

        layout.addWidget(
            icon
        )

        layout.addWidget(
            texto
        )

        frame.texto = texto

        return frame

    # =====================================================
    # TRADUÇÃO
    # =====================================================

    def atualizar_textos(self):

        self.titulo.setText(
            "🌙 " +
            language.texto(
                "dashboard_titulo"
            )
        )

        self.subtitulo.setText(
            language.texto(
                "dashboard_descricao"
            )
        )

        self.card_controle.texto.setText(
            language.texto(
                "dashboard_controles"
            )
        )

        self.card_perfil.texto.setText(
            language.texto(
                "dashboard_perfis"
            )
        )

        self.card_calibracao.texto.setText(
            language.texto(
                "calibracao"
            )
        )

        self.card_sistema.texto.setText(
            language.texto(
                "dashboard_status"
            )
        )

        self.status_title.setText(
            "📊 CANARIS ™ Status"
        )

        self.status_controle.setText(
            "🎮 " +
            language.texto(
                "controle_conectado"
            )
        )

        self.status_perfil.setText(
            "📁 " +
            language.texto(
                "perfil"
            )
        )

        self.status_idioma.setText(
            "🌐 " +
            self.idioma_texto()
        )

        self.status_calibracao.setText(
            "🎯 " +
            language.texto(
                "calibracao_status"
            )
        )

        self.status_update.setText(
            "🔄 CANARIS ™ Ready"
        )

        self.btn_notify.setText(
            "🔔 " +
            language.texto(
                "teste_notificacao"
            )
        )

    def idioma_texto(self):

        if language.idioma == "pt":
            return "Português"

        return "English"

       # =====================================================
        # PERFIL GAMER
        # =====================================================

    def carregar_usuario(self):

            try:

                if not self.main_window:
                    return

                if not hasattr(
                        self.main_window,
                        "usuario_atual"
                ):
                    return

                self.usuario = (
                    self.main_window.usuario_atual()
                )

                print(
                    "USUARIO DASHBOARD:",
                    self.usuario
                )

                if self.usuario:

                    self.user_name.setText(

                        "🎮 Bem vindo, "

                        +

                        self.usuario["username"]

                    )

                    perfil = (

                        self.profile_manager.get_profile(

                            self.usuario["id"]

                        )

                    )

                    if perfil:

                        self.user_info.setText(

                            f"""
    ⭐ Level: {perfil['level']}
    ⚡ XP: {perfil['xp']}
    🎯 Partidas: {perfil['games_played']}
    ⏱ Horas: {perfil['hours_played']}h
    """

                        )


                    else:

                        self.user_info.setText(

                            """
    ⭐ Level: 999999
    ⚡ XP: 0
    🎯 Partidas: 0
    ⏱ Horas: 4 Dias e 12 horas.
    """

                        )


                else:

                    self.user_name.setText(

                        "🎮 SISTEMA DE USUARIO AINDA EM PRODUÇÃO ⚠️"

                    )


            except Exception as erro:

                print(

                    "Erro carregando usuário:",

                    erro

                )


    # =====================================================
    # NOTIFICAÇÃO
    # =====================================================

    def testar_notificacao(self):

        notification.success(

            language.texto(
                "notificacao_teste"
            )

        )