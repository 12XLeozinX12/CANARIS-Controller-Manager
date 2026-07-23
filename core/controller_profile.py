# CANARIS ™ Controller Manager
# Sistema de perfis de controles


class ControllerProfiles:


    @staticmethod
    def xbox():

        return {

            "tipo": "Xbox",

            "buttons": {

                "A": 0,
                "B": 1,
                "X": 2,
                "Y": 3,

                "LB": 4,
                "RB": 5,

                "BACK": 6,
                "START": 7,

                "LS": 8,
                "RS": 9,

                "HOME": 10
            },


            "axes": {

                "LX":0,
                "LY":1,

                "RX":2,
                "RY":3,

                "LT":4,
                "RT":5

            },


            "dpad": {

                "axis": False

            }

        }




    @staticmethod
    def playstation():


        return {


            "tipo":"PlayStation",


            "buttons":{


                "X":0,
                "CIRCLE":1,
                "SQUARE":2,
                "TRIANGLE":3,


                "L1":4,
                "R1":5,


                "SHARE":6,
                "OPTIONS":7,


                "L3":8,
                "R3":9,


                "PS":10

            },



            "axes":{


                "LX":0,
                "LY":1,


                "RX":2,
                "RY":5,


                "L2":3,
                "R2":4

            },



            "dpad":{

                "axis":False

            }

        }




    @staticmethod
    def nintendo():


        return {


            "tipo":"Nintendo",


            "buttons":{


                "B":0,
                "A":1,
                "Y":2,
                "X":3,


                "L":4,
                "R":5,


                "MINUS":6,
                "PLUS":7,


                "LS":8,
                "RS":9,


                "HOME":10

            },



            "axes":{


                "LX":0,
                "LY":1,

                "RX":2,
                "RY":3,


                "ZL":4,
                "ZR":5

            },


            "dpad":{

                "axis":False

            }

        }




    @staticmethod
    def generic():


        return {


            "tipo":"Generic",


            "buttons":{


                "A":0,
                "B":1,
                "X":2,
                "Y":3

            },


            "axes":{


                "LX":0,
                "LY":1,

                "RX":2,
                "RY":3

            },


            "dpad":{

                "axis":False

            }

        }





    @staticmethod
    def detectar(nome,guid):


        nome = nome.lower()
        guid = guid.lower()



        if any(x in nome for x in [

            "xbox",
            "xinput",
            "microsoft"

        ]):

            return ControllerProfiles.xbox()



        if any(x in nome for x in [

            "dualshock",
            "dualsense",
            "playstation",
            "sony"

        ]):

            return ControllerProfiles.playstation()



        if any(x in nome for x in [

            "nintendo",
            "switch",
            "joy"

        ]):

            return ControllerProfiles.nintendo()



        return ControllerProfiles.generic()