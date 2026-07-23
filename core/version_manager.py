import json
import os


class VersionManager:


    def __init__(self):

        self.file = "version.json"



    def get_version(self):

        try:

            if not os.path.exists(
                self.file
            ):
                return "UNKNOWN"



            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as arquivo:


                dados = json.load(
                    arquivo
                )


            return dados.get(
                "version",
                "UNKNOWN"
            )


        except Exception:


            return "UNKNOWN"



    def get_info(self):


        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as arquivo:


                return json.load(
                    arquivo
                )


        except:


            return {}




version = VersionManager()