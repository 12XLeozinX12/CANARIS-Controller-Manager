import json
import urllib.request



class UpdateManager:


    def __init__(self):

        self.current_version = "1.0.0"


        # futuramente será seu servidor
        self.url = (
            "update.json"
        )

    def verificar_atualizacao(self):


        try:


            resposta = urllib.request.urlopen(
                self.update_url,
                timeout=5
            )


            dados = json.loads(
                resposta.read()
            )


            nova_versao = dados["version"]



            if nova_versao != self.current_version:


                return {

                    "update": True,

                    "version": nova_versao,

                    "download": dados["download"]

                }



            return {

                "update": False

            }



        except Exception:


            return {

                "update": False

            }





update = UpdateManager()