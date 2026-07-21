from core.settings_manager import settings



class AppSettings:



    def tema(self):

        return settings.get(
            "tema"
        )



    def som(self):

        return settings.get(
            "som"
        )



    def vibracao(self):

        return settings.get(
            "vibracao"
        )



    def taxa(self):

        return settings.get(
            "taxa_atualizacao"
        )



    def iniciar_windows(self):

        return settings.get(
            "iniciar_windows"
        )




config = AppSettings()