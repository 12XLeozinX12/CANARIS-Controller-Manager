class ButtonMapper:


    def __init__(self):

        self.mapa = {}



    def definir(
        self,
        indice,
        nome
    ):

        self.mapa[indice] = nome



    def obter(
        self,
        indice
    ):

        return self.mapa.get(

            indice,

            f"BOTÃO {indice}"

        )



    def limpar(self):

        self.mapa.clear()