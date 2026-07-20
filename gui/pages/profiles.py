from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QMessageBox
)


from core.profile_manager import ProfileManager
from gui.dialogs.edit_profile import EditProfile
from core.language_manager import language





class Profiles(QWidget):


    def __init__(self):

        super().__init__()



        self.profile_manager = ProfileManager()


        self.janela_edicao = None



        self.init_ui()



        language.idioma_alterado.connect(

            self.atualizar_textos

        )





    def init_ui(self):


        self.layout = QVBoxLayout()



        self.titulo = QLabel()



        self.lista = QListWidget()



        self.editar = QPushButton()



        self.excluir = QPushButton()



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



        self.setLayout(

            self.layout

        )



        self.atualizar_textos()


        self.carregar_perfis()





    def atualizar_textos(self):


        if language.idioma == "pt":


            self.titulo.setText(

                "👤 Perfis de Controles"

            )


            self.editar.setText(

                "Editar Perfil"

            )


            self.excluir.setText(

                "Excluir Perfil"

            )


        else:


            self.titulo.setText(

                "👤 Controller Profiles"

            )


            self.editar.setText(

                "Edit Profile"

            )


            self.excluir.setText(

                "Delete Profile"

            )







    def carregar_perfis(self):


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







    def editar_perfil(self):


        indice = (

            self.lista.currentRow()

        )



        if indice < 0:


            return



        perfil = (

            self.profile_manager
            .profiles[indice]

        )



        self.janela_edicao = EditProfile(

            perfil,

            self.profile_manager

        )


        self.janela_edicao.show()







    def excluir_perfil(self):


        indice = (

            self.lista.currentRow()

        )



        if indice < 0:


            return



        resposta = QMessageBox.question(

            self,

            "CANARIS CM",

            "Excluir este perfil?"

        )



        if resposta == QMessageBox.Yes:



            self.profile_manager.delete_profile(

                indice

            )


            self.carregar_perfis()