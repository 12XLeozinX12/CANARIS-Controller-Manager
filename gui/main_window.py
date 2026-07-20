from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QStackedWidget,
    QSizePolicy
)


from gui.pages.dashboard import Dashboard
from gui.pages.controles import Controles
from gui.pages.config import Config
from gui.pages.sobre import Sobre
from gui.pages.profiles import Profiles
from gui.pages.controller_lab import ControllerLab


from core.language_manager import language
from core.paths import resource_path


from gui.styles import DARK_THEME
from gui.widgets.sidebar_button import SidebarButton





class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()



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



        self.setStyleSheet(
            DARK_THEME
        )



        central = QWidget()

        self.setCentralWidget(
            central
        )



        layout_principal = QHBoxLayout()


        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )


        layout_principal.setSpacing(
            0
        )


        central.setLayout(
            layout_principal
        )




        # =====================
        # SIDEBAR
        # =====================


        sidebar = QVBoxLayout()


        sidebar.setSpacing(
            8
        )



        self.titulo = QLabel(
            "CANARIS ™"
        )


        self.titulo.setStyleSheet(
            """
            color:#8B5CF6;
            font-size:32px;
            font-weight:bold;
            padding:20px;
            """
        )


        sidebar.addWidget(
            self.titulo
        )



        self.btn_dashboard = SidebarButton("")
        self.btn_controles = SidebarButton("")
        self.btn_lab = SidebarButton("")
        self.btn_perfis = SidebarButton("")
        self.btn_config = SidebarButton("")
        self.btn_sobre = SidebarButton("")



        sidebar.addWidget(
            self.btn_dashboard
        )

        sidebar.addWidget(
            self.btn_controles
        )

        sidebar.addWidget(
            self.btn_lab
        )

        sidebar.addWidget(
            self.btn_perfis
        )

        sidebar.addWidget(
            self.btn_config
        )

        sidebar.addWidget(
            self.btn_sobre
        )


        sidebar.addStretch()



        versao = QLabel(
            "CANARIS ™ CM v1.0"
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





        # =====================
        # PAGINAS
        # =====================


        self.telas = QStackedWidget()


        self.telas.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )



        self.dashboard = Dashboard()

        self.controles = Controles()

        self.controller_lab = ControllerLab()

        self.perfis = Profiles()

        self.config = Config()

        self.sobre = Sobre()



        paginas = [

            self.dashboard,

            self.controles,

            self.controller_lab,

            self.perfis,

            self.config,

            self.sobre

        ]



        for pagina in paginas:

            self.telas.addWidget(
                pagina
            )



        layout_principal.addWidget(
            self.telas
        )



        # =====================
        # NAVEGAÇÃO
        # =====================


        self.btn_dashboard.clicked.connect(
            lambda:
            self.telas.setCurrentWidget(
                self.dashboard
            )
        )


        self.btn_controles.clicked.connect(
            lambda:
            self.telas.setCurrentWidget(
                self.controles
            )
        )


        self.btn_lab.clicked.connect(
            lambda:
            self.telas.setCurrentWidget(
                self.controller_lab
            )
        )


        self.btn_perfis.clicked.connect(
            lambda:
            self.telas.setCurrentWidget(
                self.perfis
            )
        )


        self.btn_config.clicked.connect(
            lambda:
            self.telas.setCurrentWidget(
                self.config
            )
        )


        self.btn_sobre.clicked.connect(
            lambda:
            self.telas.setCurrentWidget(
                self.sobre
            )
        )



        language.idioma_alterado.connect(
            self.atualizar_idioma
        )


        self.atualizar_idioma()





    def atualizar_idioma(self):


        self.btn_dashboard.setText(
            "🏠 " +
            language.texto(
                "dashboard"
            )
        )


        self.btn_controles.setText(
            "🎮 " +
            language.texto(
                "controles"
            )
        )


        self.btn_lab.setText(
            "🧪 Controller Lab"
        )


        self.btn_perfis.setText(
            "👤 " +
            language.texto(
                "perfis"
            )
        )


        self.btn_config.setText(
            "⚙ " +
            language.texto(
                "config"
            )
        )


        self.btn_sobre.setText(
            "ℹ " +
            language.texto(
                "sobre"
            )
        )