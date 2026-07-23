from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QMessageBox,
    QHBoxLayout,
    QFrame
)

from PySide6.QtCore import Qt

from core.profile_manager import ProfileManager
from gui.dialogs.edit_profile import EditProfile
from core.language_manager import language

from gui.widgets.notification import notification





class Profiles(QWidget):


    def __init__(self):

        super().__init__()



        self.profile_manager = ProfileManager()


        self.janela_edicao = None

        self.perfil_selecionado = None

        self.init_ui()



        language.idioma_alterado.connect(

            self.atualizar_textos

        )









    def init_ui(self):


        self.layout = QVBoxLayout(
            self
        )



        self.layout.setContentsMargins(

            30,

            30,

            30,

            30

        )



        self.layout.setSpacing(

            15

        )







        self.titulo = QLabel()



        self.titulo.setStyleSheet(

            """

            color:#8B5CF6;

            font-size:28px;

            font-weight:bold;

            """

        )








        self.lista = QListWidget()

        self.lista.currentRowChanged.connect(

            self.mostrar_detalhes

        )

        self.lista.setStyleSheet(

            """

            QListWidget{

                background:#171717;

                color:white;

                border-radius:12px;

                padding:10px;

            }


            QListWidget::item{

                padding:10px;

            }


            QListWidget::item:selected{

                background:#8B5CF6;

            }

            """

        )

        # =========================
        # DETALHES DO PERFIL
        # =========================

        self.card_detalhes = QFrame()

        self.card_detalhes.setStyleSheet("""
        QFrame{

        background:#0B0B12;

        border-radius:18px;

        padding:15px;

        }

        QLabel{

        color:white;

        font-size:15px;

        }

        """)

        detalhes_layout = QVBoxLayout(
            self.card_detalhes
        )

        self.detalhes = QLabel()

        self.detalhes.setWordWrap(
            True
        )

        detalhes_layout.addWidget(
            self.detalhes
        )

        self.layout.addWidget(
            self.card_detalhes
        )


        self.editar = QPushButton()



        self.excluir = QPushButton()






        self.editar.setStyleSheet(

            self.botao_style()

        )


        self.excluir.setStyleSheet(

            self.botao_style()

        )







        self.editar.clicked.connect(

            self.editar_perfil

        )



        self.excluir.clicked.connect(

            self.excluir_perfil

        )








        self.layout.addWidget(

            self.titulo

        )



        self.layout.addWidget(

            self.lista

        )



        self.layout.addWidget(

            self.editar

        )



        self.layout.addWidget(

            self.excluir

        )





        self.atualizar_textos()



        self.carregar_perfis()










    def botao_style(self):


        return """

        QPushButton{

            background:#8B5CF6;

            color:white;

            border:none;

            padding:12px;

            border-radius:12px;

            font-size:15px;

        }


        QPushButton:hover{

            background:#A78BFA;

        }

        """









    def atualizar_textos(self):


        if language.idioma == "pt":


            self.titulo.setText(

                "👤 Perfis de Controles"

            )


            self.editar.setText(

                "✏ Editar Perfil"

            )


            self.excluir.setText(

                "🗑 Excluir Perfil"

            )


        else:


            self.titulo.setText(

                "👤 Controller Profiles"

            )


            self.editar.setText(

                "✏ Edit Profile"

            )


            self.excluir.setText(

                "🗑 Delete Profile"

            )









    def carregar_perfis(self):


        try:


            self.lista.clear()



            perfis = (

                self.profile_manager

                .get_profiles()

            )



            for perfil in perfis:



                texto = (

                    f"🎮 {perfil['name']} "

                    f"({perfil['type']})"

                )



                self.lista.addItem(

                    texto

                )



        except Exception as erro:


            notification.error(

                "Erro ao carregar perfis"

            )

    # =========================
    # MOSTRAR DETALHES
    # =========================

    def mostrar_detalhes(self, indice):

        if indice < 0:
            self.detalhes.setText(
                "Nenhum perfil selecionado"
            )

            return

        try:

            perfil = (

                self.profile_manager

                .profiles[indice]

            )

            texto = f"""

    🎮 Nome:
    {perfil.get('name', '-')}


    Tipo:
    {perfil.get('type', '-')}


    GUID:
    {perfil.get('guid', '-')}



    ⚙ Calibração:

    Left:
    {perfil.get('calibration', {}).get('deadzone_left', 0) * 100:.0f}%


    Right:
    {perfil.get('calibration', {}).get('deadzone_right', 0) * 100:.0f}%



    🎮 Controle:


    Botões:
    {len(perfil.get('buttons', {}))}


    Eixos:
    {len(perfil.get('axes', {}))}

    """

            self.detalhes.setText(
                texto
            )


        except Exception as erro:

            notification.error(
                str(erro)
            )


    def editar_perfil(self):


        indice = (

            self.lista.currentRow()

        )




        if indice < 0:



            notification.warning(

                "Selecione um perfil primeiro"

            )


            return







        try:


            perfil = (

                self.profile_manager

                .profiles[indice]

            )



            self.janela_edicao = EditProfile(

                perfil,

                self.profile_manager

            )



            self.janela_edicao.show()



            notification.info(

                "Editando perfil..."

            )



        except Exception:


            notification.error(

                "Não foi possível editar o perfil"

            )









    def excluir_perfil(self):


        indice = (

            self.lista.currentRow()

        )




        if indice < 0:



            notification.warning(

                "Selecione um perfil primeiro"

            )


            return







        resposta = QMessageBox.question(

            self,

            "CANARIS ™ CM",

            "Deseja excluir este perfil?"

        )







        if resposta == QMessageBox.Yes:



            try:



                self.profile_manager.delete_profile(

                    indice

                )



                self.carregar_perfis()



                notification.success(

                    "Perfil excluído com sucesso!"

                )



            except Exception:



                notification.error(

                    "Erro ao excluir perfil"

                )