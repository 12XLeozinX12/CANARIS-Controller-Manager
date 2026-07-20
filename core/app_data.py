import os
import json
import sys



class AppData:


    def __init__(self):

        self.folder = self.get_folder()

        self.settings_file = os.path.join(
            self.folder,
            "settings.json"
        )


        self.create_folder()


    def get_folder(self):

        if sys.platform == "win32":

            base = os.getenv(
                "APPDATA"
            )

        else:

            base = os.path.expanduser(
                "~/.config"
            )


        return os.path.join(
            base,
            "CANARIS CM"
        )



    def create_folder(self):

        if not os.path.exists(
            self.folder
        ):

            os.makedirs(
                self.folder
            )



    def load_settings(self):

        if not os.path.exists(
            self.settings_file
        ):

            return {

                "language":"pt"

            }


        try:

            with open(
                self.settings_file,
                "r",
                encoding="utf-8"
            ) as arquivo:


                return json.load(
                    arquivo
                )


        except:


            return {

                "language":"pt"

            }



    def save_settings(
        self,
        data
    ):


        with open(
            self.settings_file,
            "w",
            encoding="utf-8"
        ) as arquivo:


            json.dump(
                data,
                arquivo,
                indent=4,
                ensure_ascii=False
            )



app_data = AppData()