from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt



class SidebarButton(QPushButton):


    def __init__(
        self,
        texto
    ):


        super().__init__(
            texto
        )



        self.ativo = False



        self.setCursor(
            Qt.PointingHandCursor
        )



        self.setMinimumHeight(
            42
        )



        self.atualizar_estilo()







    def set_active(
        self,
        estado
    ):


        self.ativo = estado


        self.atualizar_estilo()







    def atualizar_estilo(
        self
    ):


        if self.ativo:


            self.setStyleSheet(

                """

                QPushButton{

                    background:#24183D;

                    color:#FFFFFF;

                    border:none;

                    border-left:4px solid #8B5CF6;

                    text-align:left;

                    padding:12px 16px;

                    border-radius:12px;

                    font-size:15px;

                    font-weight:bold;

                }



                QPushButton:hover{

                    background:#30204F;

                }


                """

            )



        else:


            self.setStyleSheet(

                """

                QPushButton{

                    background:transparent;

                    color:#A1A1AA;

                    border:none;

                    text-align:left;

                    padding:12px 16px;

                    border-radius:12px;

                    font-size:15px;

                }



                QPushButton:hover{

                    background:#1E1E1E;

                    color:white;

                }



                QPushButton:pressed{

                    background:#2A2A2A;

                    color:white;

                }


                """

            )