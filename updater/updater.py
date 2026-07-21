import os
import time
import shutil
import subprocess
import sys



class CanarisUpdater:



    def __init__(self):

        self.programa_atual = (
            "CANARIS CM.exe"
        )

        self.novo_programa = (
            "CANARIS_NEW.exe"
        )

        self.backup = (
            "CANARIS_BACKUP.exe"
        )





    def fazer_backup(self):

        if os.path.exists(
            self.programa_atual
        ):


            shutil.copy2(

                self.programa_atual,

                self.backup

            )





    def substituir(self):


        if not os.path.exists(
            self.novo_programa
        ):

            return False




        self.fazer_backup()



        time.sleep(
            2
        )



        if os.path.exists(
            self.programa_atual
        ):


            os.remove(
                self.programa_atual
            )



        shutil.move(

            self.novo_programa,

            self.programa_atual

        )



        return True





    def iniciar_programa(self):


        subprocess.Popen(

            [
                self.programa_atual
            ]

        )








if __name__ == "__main__":


    updater = CanarisUpdater()



    sucesso = (
        updater.substituir()
    )



    if sucesso:


        updater.iniciar_programa()