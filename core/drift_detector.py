import time





class DriftDetector:



    def __init__(self):

        self.reset()






    def reset(self):


        self.left_samples = []

        self.right_samples = []

        self.iniciado = time.time()





    def adicionar_leitura(

        self,

        axes

    ):


        if len(axes) < 4:

            return



        self.left_samples.append(

            {

                "x": axes[0],

                "y": axes[1]

            }

        )



        self.right_samples.append(

            {

                "x": axes[2],

                "y": axes[3]

            }

        )







    def tempo_decorrido(self):


        return time.time() - self.iniciado








    def finalizado(self):


        return self.tempo_decorrido() >= 10







    def progresso(self):


        valor = int(

            (self.tempo_decorrido()/10)*100

        )


        if valor > 100:

            valor = 100


        return valor








    def analisar(self):


        resultado = {



            "left":{


                "drift":False,

                "valor":0


            },



            "right":{


                "drift":False,

                "valor":0


            }



        }




        if len(self.left_samples) == 0:


            return resultado






        left = self.calcular(

            self.left_samples

        )



        right = self.calcular(

            self.right_samples

        )





        resultado["left"]["valor"] = left


        resultado["right"]["valor"] = right





        if left > 0.10:


            resultado["left"]["drift"] = True




        if right > 0.10:


            resultado["right"]["drift"] = True






        return resultado







    def calcular(

        self,

        dados

    ):



        total = 0



        for valor in dados:


            x = abs(

                valor["x"]

            )


            y = abs(

                valor["y"]

            )


            total += (

                x+y

            ) / 2





        return round(

            total / len(dados),

            3

        )







drift = DriftDetector()