import urllib.request



class Downloader:



    def baixar(

        self,

        url,

        destino,

        callback=None

    ):



        def progresso(

            bloco,

            tamanho_bloco,

            tamanho_total

        ):



            if callback and tamanho_total > 0:


                porcentagem = int(

                    bloco *
                    tamanho_bloco *
                    100 /
                    tamanho_total

                )


                if porcentagem > 100:

                    porcentagem = 100



                callback(
                    porcentagem
                )





        urllib.request.urlretrieve(

            url,

            destino,

            progresso

        )