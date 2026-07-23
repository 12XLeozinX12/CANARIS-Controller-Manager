# ==========================================================
# CANARIS ™ Controller Detector
# Identificação automática de controles
# ==========================================================



def detectar_tipo(

    nome,

    guid

):


    nome = str(nome).lower()

    guid = str(guid).lower()





    # ======================================================
    # XBOX / XINPUT
    # ======================================================


    xbox_keywords = [


        "xbox",

        "xinput",

        "microsoft",

        "x-box"


    ]



    for palavra in xbox_keywords:


        if palavra in nome or palavra in guid:


            return "Xbox"







    # ======================================================
    # PLAYSTATION
    # ======================================================


    playstation_keywords = [


        "dualshock",

        "dualsense",

        "playstation",

        "sony",

        "wireless controller"


    ]



    for palavra in playstation_keywords:


        if palavra in nome:


            return "PlayStation"








    # ======================================================
    # NINTENDO
    # ======================================================


    nintendo_keywords = [


        "switch",

        "joy-con",

        "nintendo",

        "pro controller"


    ]



    for palavra in nintendo_keywords:


        if palavra in nome:


            return "Nintendo"








    # ======================================================
    # LOGITECH / GENÉRICOS
    # ======================================================


    generic_keywords = [


        "logitech",

        "f310",

        "f710",

        "generic",

        "gamepad",

        "controller"


    ]



    for palavra in generic_keywords:


        if palavra in nome:


            return "Generic"







    return "Generic"