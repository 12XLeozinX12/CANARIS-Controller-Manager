from core.settings_manager import settings



class ConfigManager:


    def tema(self):

        return settings.get(
            "tema"
        )



    def idioma(self):

        return settings.get(
            "idioma"
        )



    def som_ativo(self):

        return settings.get(
            "som"
        )



    def vibracao_ativa(self):

        return settings.get(
            "vibracao"
        )



    def taxa_controller(self):

        return settings.get(
            "taxa_atualizacao"
        )



    def iniciar_windows(self):

        return settings.get(
            "iniciar_windows"
        )





config = ConfigManager()