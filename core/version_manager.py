import json
import os



class VersionManager:


    def __init__(self):

        self.file = "version.json"

        self.version = self.load()



    def load(self):

        if not os.path.exists(
            self.file
        ):

            return {

                "app_name":
                "CANARIS ™ CM",

                "version":
                "1.0.0"

            }



        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(
                arquivo
            )



    def get_version(self):

        return self.version.get(
            "version",
            "1.0.0"
        )



version = VersionManager()