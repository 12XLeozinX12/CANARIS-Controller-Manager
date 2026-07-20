import os
import sys
import urllib.request
import subprocess
import time



DOWNLOAD_URL = (
    "https://SEU-SERVIDOR.com/CANARIS_CM_Setup.exe"
)


ARQUIVO = (
    "CANARIS_CM_Update.exe"
)



def baixar_atualizacao():


    print(
        "Baixando atualização..."
    )


    urllib.request.urlretrieve(
        DOWNLOAD_URL,
        ARQUIVO
    )



def instalar():


    print(
        "Abrindo instalador..."
    )


    subprocess.Popen(
        [
            ARQUIVO
        ]
    )



def iniciar_programa():


    caminho = (
        "CANARIS CM.exe"
    )


    if os.path.exists(
        caminho
    ):


        subprocess.Popen(
            [
                caminho
            ]
        )



if __name__ == "__main__":


    try:


        baixar_atualizacao()


        time.sleep(2)


        instalar()



    except Exception as erro:


        print(
            erro
        )