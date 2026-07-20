import os
import time
import shutil
import subprocess
import sys



class CanarisUpdater:



    def __init__(self):


        self.atual = (
            "CANARIS CM.exe"
        )


        self.novo = (
            "update/CANARIS_NEW.exe"
        )


        self.backup = (
            "backup/CANARIS_OLD.exe"
        )





    def criar_backup(self):


        if not os.path.exists(
            "backup"
        ):

            os.makedirs(
                "backup"
            )



        if os.path.exists(
            self.atual
        ):


            shutil.copy(

                self.atual,

                self.backup

            )







    def instalar(self):


        if not os.path.exists(
            self.novo
        ):


            return False




        self.criar_backup()



        time.sleep(
            2
        )



        shutil.move(

            self.novo,

            self.atual

        )



        return True







    def iniciar(self):


        if os.path.exists(
            self.atual
        ):


            subprocess.Popen(
                [
                    self.atual
                ]
            )






if __name__ == "__main__":


    updater = CanarisUpdater()



    if updater.instalar():


        updater.iniciar()