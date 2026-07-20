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


            if callback:


                porcentagem = int(

                    bloco *
                    tamanho_bloco *
                    100 /
                    tamanho_total

                )


                callback(
                    porcentagem
                )



        urllib.request.urlretrieve(

            url,

            destino,

            progresso

        )