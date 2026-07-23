import json
import urllib.request
import os



class UpdateManager:


    def __init__(self):

        self.url = (

            "https://raw.githubusercontent.com/"
            "12XLeozinX12/"
            "CANARIS-Controller-Manager/"
            "main/update.json"

        )




    def versao_atual(self):


        try:

            with open(
                "version.txt",
                "r",
                encoding="utf-8"
            ) as arquivo:


                return arquivo.read().strip()



        except:


            return "UNKNOWN"





    def comparar(
        self,
        atual,
        nova
    ):


        return atual != nova





    def verificar_atualizacao(self):


        try:


            resposta = urllib.request.urlopen(

                self.url,

                timeout=5

            )


            dados = json.loads(

                resposta.read()

            )


            atual = self.versao_atual()


            nova = dados.get(

                "version",

                "UNKNOWN"

            )



            if self.comparar(

                atual,

                nova

            ):


                return {


                    "update": True,


                    "version": nova,


                    "download":
                    dados.get(
                        "download"
                    ),


                    "changelog":
                    dados.get(
                        "changelog",
                        []
                    )

                }





        except Exception as erro:


            print(
                "Erro update:",
                erro
            )




        return {


            "update": False


        }





update = UpdateManager()