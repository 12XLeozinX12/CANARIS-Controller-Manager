from PySide6.QtCore import QObject, Signal

from core.app_data import app_data



class LanguageManager(QObject):


    idioma_alterado = Signal()



    def __init__(self):

        super().__init__()


        settings = app_data.load_settings()


        self.idioma = settings.get(
            "language",
            "pt"
        )



        self.textos = {


            "pt": {


                # MENU

                "dashboard":
                "Dashboard",


                "controles":
                "Controles",


                "perfis":
                "Perfis",


                "config":
                "Configurações",


                "sobre":
                "Sobre",



                # DASHBOARD

                "dashboard_subtitulo":
                "Visão geral do sistema",


                "controles_card":
                "Controles",


                "status_card":
                "Status",


                "sistema_card":
                "Sistema",



                # CONTROLES

                "controles_titulo":
                "Controles",


                "controles_descricao":
                "Gerencie todos os controles conectados ao CANARIS ™ CM",


                "controles_detectados":
                "Controles detectados",


                "informacoes":
                "Informações",


                "nenhum_controle":
                "Nenhum controle conectado.",


                "atualizar":
                "🔄 Atualizar dispositivos",



                # PERFIS

                "perfil_titulo":
                "👤 Perfis de Controles",


                "editar_perfil":
                "Editar Perfil",



                # CONFIG

                "config_titulo":
                "⚙ Configurações",



                # SOBRE

                "sobre_titulo":
                "ℹ Sobre o CANARIS ™ CM",



                # CONTROLLER LAB

                "lab_titulo":
                "🎮 CANARIS ™ Controller Lab",


                "procurando":
                "Procurando controle...",



            },



            "en": {


                # MENU

                "dashboard":
                "Dashboard",


                "controles":
                "Controllers",


                "perfis":
                "Profiles",


                "config":
                "Settings",


                "sobre":
                "About",



                # DASHBOARD

                "dashboard_subtitulo":
                "System overview",


                "controles_card":
                "Controllers",


                "status_card":
                "Status",


                "sistema_card":
                "System",



                # CONTROLES

                "controles_titulo":
                "Controllers",


                "controles_descricao":
                "Manage all controllers connected to CANARIS ™ CM",


                "controles_detectados":
                "Detected controllers",


                "informacoes":
                "Information",


                "nenhum_controle":
                "No controller connected.",


                "atualizar":
                "🔄 Update devices",



                # PERFIS

                "perfil_titulo":
                "👤 Controller Profiles",


                "editar_perfil":
                "Edit Profile",



                # CONFIG

                "config_titulo":
                "⚙ Settings",



                # SOBRE

                "sobre_titulo":
                "ℹ About CANARIS ™ CM",



                # CONTROLLER LAB

                "lab_titulo":
                "🎮 CANARIS ™ Controller Lab",


                "procurando":
                "Searching controller...",


            }


        }



    def texto(
        self,
        chave
    ):


        return self.textos.get(
            self.idioma,
            self.textos["pt"]
        ).get(
            chave,
            chave
        )




    def mudar_idioma(
        self,
        novo_idioma
    ):


        if novo_idioma not in [
            "pt",
            "en"
        ]:

            return



        self.idioma = novo_idioma



        app_data.save_settings(

            {

                "language":
                self.idioma

            }

        )



        self.idioma_alterado.emit()



# Instância global

language = LanguageManager()