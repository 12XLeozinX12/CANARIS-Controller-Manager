import json
import os



class ControllerProfile:


    FILE = "data/controller_profiles.json"



    def __init__(self):


        self.profiles = []


        self.load()





    def load(self):


        if not os.path.exists(self.FILE):


            self.save()

            return



        try:


            with open(

                self.FILE,

                "r",

                encoding="utf-8"

            ) as file:


                self.profiles = json.load(file)



        except:


            self.profiles = []

            self.save()





    def save(self):


        os.makedirs(

            "data",

            exist_ok=True

        )


        with open(

            self.FILE,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                self.profiles,

                file,

                indent=4,

                ensure_ascii=False

            )






    def create(

        self,

        controller

    ):


        profile = {


            "id":
            controller["id"],


            "name":
            controller["nome"],


            "type":
            controller["tipo"],


            "buttons":{},

            "sensitivity":100,

            "vibration":True


        }



        self.profiles.append(

            profile

        )


        self.save()



        return profile





    def get_by_id(

        self,

        guid

    ):


        for profile in self.profiles:


            if profile["id"] == guid:


                return profile



        return None





    def update_button(

        self,

        guid,

        button,

        action

    ):


        profile = self.get_by_id(

            guid

        )


        if not profile:


            return False



        profile["buttons"][

            str(button)

        ] = action



        self.save()



        return True