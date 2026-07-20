from core.controller_profile import (
    XBOX_PROFILE,
    PLAYSTATION_PROFILE,
    GENERIC_PROFILE
)



def detectar_perfil(nome):


    nome = nome.lower()



    if "xbox" in nome:

        return XBOX_PROFILE



    if (
        "dualshock" in nome
        or
        "dualsense" in nome
        or
        "sony" in nome
    ):

        return PLAYSTATION_PROFILE



    return GENERIC_PROFILE