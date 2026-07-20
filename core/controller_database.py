class ControllerDatabase:


    def __init__(self):


        self.controllers = {


            "054c":

            {

                "brand":"Sony",

                "type":"PlayStation"

            },


            "05c4":

            {

                "brand":"Sony",

                "type":"PlayStation"

            },


            "09cc":

            {

                "brand":"Sony",

                "type":"PlayStation"

            },


            "xinput":

            {

                "brand":"Microsoft",

                "type":"Xbox"

            },


            "switch":

            {

                "brand":"Nintendo",

                "type":"Nintendo"

            }

        }





    def identify(
        self,
        name,
        guid
    ):


        name = name.lower()

        guid = guid.lower()



        for key, data in self.controllers.items():


            if key in guid or key in name:


                return data



        return {


            "brand":"Generic",

            "type":"Generic"

        }





    def get_type(
        self,
        name,
        guid
    ):


        return self.identify(

            name,
            guid

        )["type"]





    def get_brand(
        self,
        name,
        guid
    ):


        return self.identify(

            name,
            guid

        )["brand"]