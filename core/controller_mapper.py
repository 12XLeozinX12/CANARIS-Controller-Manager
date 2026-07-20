class ControllerMapper:


    def __init__(self):

        self.maps = {


            # =================================
            # PLAYSTATION
            # =================================

            "PlayStation": {


                0: "✕ X",

                1: "⭕ O",

                2: "◻ Quadrado",

                3: "🔺 Triângulo",


                4: "SHARE",

                6: "OPTIONS",


                7: "L3",

                8: "R3",


                9: "L1",

                10: "L2",


                11: "D-PAD UP",

                12: "D-PAD DOWN",

                13: "D-PAD LEFT",

                14: "D-PAD RIGHT",


                15: "TOUCH PAD CLICK"

            },




            # =================================
            # XBOX
            # =================================

            "Xbox": {


                0: "A",

                1: "B",

                2: "X",

                3: "Y",


                4: "VIEW",

                5: "MENU",


                6: "LB",

                7: "RB",


                8: "LS",

                9: "RS",


                10: "LT",

                11: "RT",


                12: "D-PAD UP",

                13: "D-PAD DOWN",

                14: "D-PAD LEFT",

                15: "D-PAD RIGHT"

            }



        }





    def get_button_name(
        self,
        tipo,
        botao
    ):


        controle = self.maps.get(
            tipo,
            {}
        )



        return controle.get(

            botao,

            f"BOTÃO {botao}"

        )