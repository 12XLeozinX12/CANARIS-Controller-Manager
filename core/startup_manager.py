import os
import sys
import winreg



class StartupManager:


    def __init__(self):

        self.nome = "CANARIS CM"



    def caminho_executavel(self):


        if getattr(
            sys,
            'frozen',
            False
        ):

            return sys.executable


        else:

            return os.path.abspath(
                sys.argv[0]
            )






    def ativar(self):


        caminho = self.caminho_executavel()



        chave = winreg.OpenKey(

            winreg.HKEY_CURRENT_USER,

            r"Software\Microsoft\Windows\CurrentVersion\Run",

            0,

            winreg.KEY_SET_VALUE

        )



        winreg.SetValueEx(

            chave,

            self.nome,

            0,

            winreg.REG_SZ,

            caminho

        )



        winreg.CloseKey(
            chave
        )







    def desativar(self):


        try:


            chave = winreg.OpenKey(

                winreg.HKEY_CURRENT_USER,

                r"Software\Microsoft\Windows\CurrentVersion\Run",

                0,

                winreg.KEY_SET_VALUE

            )


            winreg.DeleteValue(

                chave,

                self.nome

            )


            winreg.CloseKey(
                chave
            )


        except:


            pass






    def ativo(self):


        try:


            chave = winreg.OpenKey(

                winreg.HKEY_CURRENT_USER,

                r"Software\Microsoft\Windows\CurrentVersion\Run"

            )


            winreg.QueryValueEx(

                chave,

                self.nome

            )


            winreg.CloseKey(
                chave
            )


            return True



        except:


            return False






startup = StartupManager()