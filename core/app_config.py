from core.settings_manager import settings


class AppConfig:


    @property
    def tema(self):

        return settings.get(
            "tema"
        )


    @property
    def idioma(self):

        return settings.get(
            "idioma"
        )


    @property
    def vibracao(self):

        return settings.get(
            "vibracao"
        )


    @property
    def som(self):

        return settings.get(
            "som"
        )


    @property
    def taxa(self):

        return settings.get(
            "taxa_atualizacao"
        )


    @property
    def iniciar_windows(self):

        return settings.get(
            "iniciar_windows"
        )



config = AppConfig()