import json
import os


class SettingsManager:

    def __init__(self):

        self.file = "data/settings.json"

        self.settings = self.load()



    def load(self):

        if not os.path.exists(self.file):

            return {
                "theme": "dark",
                "language": "pt-BR"
            }


        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)



    def save(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                self.settings,
                arquivo,
                indent=4,
                ensure_ascii=False
            )



    def set_setting(self, key, value):

        self.settings[key] = value

        self.save()



    def get_setting(self, key):

        return self.settings.get(key)