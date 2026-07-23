from PySide6.QtGui import QIcon

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSizePolicy
)


from gui.widgets.animated_stack import AnimatedStack
from gui.widgets.sidebar_button import SidebarButton
from database.session import SessionManager

from gui.pages.dashboard import Dashboard
from gui.pages.controllers import Controllers
from gui.pages.controller_lab import ControllerLab
from gui.pages.profiles import Profiles
from gui.pages.calibration import Calibration
from gui.pages.settings import Settings
from gui.pages.sobre import Sobre


from core.controller_manager import ControllerManager

from core.language_manager import language
from core.paths import resource_path
from core.settings_manager import settings
from core.theme_manager import theme



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()

        # ==========================
        # USUARIO ATUAL
        # ==========================

        self.usuario_logado = None



        # ==========================
        # CONTROLLER MANAGER GLOBAL
        # ==========================

        self.controller_manager = ControllerManager()



        # ==========================
        # JANELA
        # ==========================


        self.setWindowTitle(
            "CANARIS ™ Controller Manager"
        )


        self.setMinimumSize(
            1100,
            700
        )


        self.resize(
            1100,
            700
        )



        self.setWindowIcon(

            QIcon(

                resource_path(
                    "assets/icons/canaris.ico"
                )

            )

        )



        theme.aplicar(

            QApplication.instance(),

            settings.get(
                "tema"
            )

        )



        # ==========================
        # CENTRAL
        # ==========================


        central = QWidget()

        self.setCentralWidget(
            central
        )



        layout_principal = QHBoxLayout(
            central
        )


        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )


        layout_principal.setSpacing(
            0
        )



        # ==========================
        # SIDEBAR
        # ==========================


        sidebar = QVBoxLayout()

        sidebar.setSpacing(
            8
        )

        titulo = QLabel(
            "🌙 CANARIS ™"
        )

        titulo.setAlignment(
            Qt.AlignCenter
        )

        titulo.setStyleSheet(
            """
            color:#A855F7;

            font-size:26px;

            font-weight:bold;

            padding:20px;

            """
        )


        sidebar.addWidget(
            titulo
        )



        self.btn_dashboard = SidebarButton("")
        self.btn_controllers = SidebarButton("")
        self.btn_lab = SidebarButton("")
        self.btn_profiles = SidebarButton("")
        self.btn_calibration = SidebarButton("")
        self.btn_settings = SidebarButton("")
        self.btn_sobre = SidebarButton("")



        botoes = [

            self.btn_dashboard,
            self.btn_controllers,
            self.btn_lab,
            self.btn_profiles,
            self.btn_calibration,
            self.btn_settings,
            self.btn_sobre

        ]



        for botao in botoes:

            sidebar.addWidget(
                botao
            )



        sidebar.addStretch()



        versao = QLabel(
            "CANARIS ™ CM\nVersão 1.0"
        )


        versao.setStyleSheet(
            """
            color:#777;
            padding:15px;
            """
        )


        sidebar.addWidget(
            versao
        )



        menu = QWidget()

        menu.setLayout(
            sidebar
        )


        menu.setFixedWidth(
            240
        )


        layout_principal.addWidget(
            menu
        )



        # ==========================
        # PAGINAS
        # ==========================


        self.telas = AnimatedStack()


        self.telas.setSizePolicy(

            QSizePolicy.Expanding,

            QSizePolicy.Expanding

        )

        self.dashboard = Dashboard(self)



        self.controllers = Controllers(

            self.controller_manager

        )



        self.controller_lab = ControllerLab()


        self.profiles = Profiles()


        self.calibration = Calibration()


        self.settings = Settings()


        self.sobre = Sobre()



        paginas = [

            self.dashboard,
            self.controllers,
            self.controller_lab,
            self.profiles,
            self.calibration,
            self.settings,
            self.sobre

        ]



        for pagina in paginas:

            self.telas.addWidget(
                pagina
            )



        layout_principal.addWidget(
            self.telas
        )



        # ==========================
        # NAVEGAÇÃO
        # ==========================


        self.btn_dashboard.clicked.connect(
            lambda:
            self.selecionar_menu(
                self.btn_dashboard,
                self.dashboard
            )
        )



        self.btn_controllers.clicked.connect(
            lambda:
            self.selecionar_menu(
                self.btn_controllers,
                self.controllers
            )
        )



        self.btn_lab.clicked.connect(
            lambda:
            self.selecionar_menu(
                self.btn_lab,
                self.controller_lab
            )
        )



        self.btn_profiles.clicked.connect(
            lambda:
            self.selecionar_menu(
                self.btn_profiles,
                self.profiles
            )
        )



        self.btn_calibration.clicked.connect(
            lambda:
            self.selecionar_menu(
                self.btn_calibration,
                self.calibration
            )
        )



        self.btn_settings.clicked.connect(
            lambda:
            self.selecionar_menu(
                self.btn_settings,
                self.settings
            )
        )



        self.btn_sobre.clicked.connect(
            lambda:
            self.selecionar_menu(
                self.btn_sobre,
                self.sobre
            )
        )



        language.idioma_alterado.connect(
            self.atualizar_idioma
        )



        self.atualizar_idioma()



        self.btn_dashboard.set_active(
            True
        )

    # ==========================
    # SISTEMA DE USUARIO
    # ==========================


    def set_usuario(self, usuario):

        self.usuario_logado = usuario


        print(
            "USUARIO DEFINIDO:",
            self.usuario_logado
        )



    def usuario_atual(self):

        return self.usuario_logado



    # ==========================
    # TROCAR PAGINA
    # ==========================


    def selecionar_menu(

            self,

            botao,

            pagina

    ):


        botoes = [

            self.btn_dashboard,
            self.btn_controllers,
            self.btn_lab,
            self.btn_profiles,
            self.btn_calibration,
            self.btn_settings,
            self.btn_sobre

        ]



        for b in botoes:

            b.set_active(
                False
            )



        botao.set_active(
            True
        )



        self.telas.setCurrentWidget(
            pagina
        )

    # ==========================
    # USUARIO ATUAL
    # ==========================

    def usuario_atual(self):

        return self.usuario_logado

    # ==========================
    # IDIOMA
    # ==========================

    def atualizar_idioma(self):

        self.btn_dashboard.setText(
            "🏠 " + language.texto("dashboard")
        )

        self.btn_controllers.setText(
            "🎮 " + language.texto("controles")
        )

        self.btn_lab.setText(
            "🧪 Controller Lab"
        )

        self.btn_profiles.setText(
            "👤 " + language.texto("perfis")
        )

        self.btn_calibration.setText(
            "🎯 Calibração"
            if language.idioma == "pt"
            else "🎯 Calibration"
        )

        self.btn_settings.setText(
            "⚙ " + language.texto("settings")
        )

        self.btn_sobre.setText(
            "ℹ " + language.texto("sobre")
        )