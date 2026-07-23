import time





class CalibrationWizard:



    def __init__(self):

        self.reset()






    def reset(self):


        self.etapa = 0


        self.iniciado = False


        self.finalizado = False


        self.inicio_tempo = None



        self.dados = {


            "sticks": [],


            "buttons": [],


            "triggers": []

        }







    def iniciar(self):


        self.reset()


        self.iniciado = True


        self.inicio_tempo = time.time()







    def proxima_etapa(self):


        self.etapa += 1





        if self.etapa >= 5:


            self.finalizado = True







    def progresso(self):


        return int(

            (self.etapa / 5) * 100

        )








    def texto_etapa(self):


        etapas = [


            "Centralize os analógicos",


            "Mova o Left Stick em círculos",


            "Mova o Right Stick em círculos",


            "Pressione todos os botões",


            "Aperte L2 e R2"


        ]



        if self.etapa >= 5:


            return "Calibração concluída"



        return etapas[self.etapa]









    def adicionar_estado(

        self,

        estado

    ):



        if not self.iniciado:


            return





        if self.etapa <= 2:


            self.dados["sticks"].append(

                estado["axes"]

            )




        elif self.etapa == 3:


            self.dados["buttons"].append(

                estado["buttons"]

            )




        elif self.etapa == 4:


            self.dados["triggers"].append(

                estado["triggers"]

            )







    def resultado(self):


        return self.dados







wizard = CalibrationWizard()