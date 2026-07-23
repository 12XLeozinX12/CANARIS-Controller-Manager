# ==========================================================
# CANARIS ™ Controller Layouts
# Sistema de mapeamento de controles
# ==========================================================


# ==========================================================
# XBOX / XINPUT
# ==========================================================

XBOX_LAYOUT = {


    # Face buttons

    "A": 0,

    "B": 1,

    "X": 2,

    "Y": 3,



    # Shoulder

    "LB": 4,

    "RB": 5,



    # Menu

    "SELECT": 6,

    "START": 7,



    # Stick buttons

    "LS": 8,

    "RS": 9,



    # D-PAD

    "DPAD_UP": 10,

    "DPAD_DOWN": 11,

    "DPAD_LEFT": 12,

    "DPAD_RIGHT": 13

}






# ==========================================================
# PLAYSTATION
# DualShock / DualSense
# ==========================================================

PLAYSTATION_LAYOUT = {


    # Face buttons

    "X": 0,

    "CIRCLE": 1,

    "SQUARE": 2,

    "TRIANGLE": 3,



    # Shoulder

    "L1":4,

    "R1":5,



    # Menu

    "SHARE":6,

    "OPTIONS":7,



    # Stick press

    "L3":8,

    "R3":9,



    # Extra

    "PS":10,

    "TOUCHPAD":11

}







# ==========================================================
# NINTENDO SWITCH PRO
# ==========================================================

SWITCH_LAYOUT = {


    "B":0,

    "A":1,

    "Y":2,

    "X":3,


    "L":4,

    "R":5,


    "MINUS":6,

    "PLUS":7,


    "L3":8,

    "R3":9,


    "HOME":10,

    "CAPTURE":11

}







# ==========================================================
# CONTROLE GENERICO
# ==========================================================

GENERIC_LAYOUT = {


    "BUTTON_1":0,

    "BUTTON_2":1,

    "BUTTON_3":2,

    "BUTTON_4":3,


    "BUTTON_5":4,

    "BUTTON_6":5,


    "SELECT":6,

    "START":7,


    "L3":8,

    "R3":9

}








# ==========================================================
# PEGAR LAYOUT PELO TIPO
# ==========================================================


def get_layout(tipo):


    if not tipo:

        return GENERIC_LAYOUT



    tipo = tipo.lower()





    if "xbox" in tipo:


        return XBOX_LAYOUT





    if "playstation" in tipo:


        return PLAYSTATION_LAYOUT






    if "sony" in tipo:


        return PLAYSTATION_LAYOUT






    if "switch" in tipo:


        return SWITCH_LAYOUT





    return GENERIC_LAYOUT