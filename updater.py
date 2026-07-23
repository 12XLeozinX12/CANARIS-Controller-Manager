import urllib.request
import os



class Updater:


    def baixar(

        self,

        url,

        destino

    ):


        try:


            urllib.request.urlretrieve(

                url,

                destino

            )


            return True



        except Exception as erro:


            print(
                erro
            )


            return False





updater = Updater()