from gui.styles import DARK_THEME



LIGHT_THEME = """

QMainWindow,
QWidget {

    background:#F5F5F5;

    color:#111111;

}



QLabel {

    color:#111111;

}



QPushButton {

    background:#8B5CF6;

    color:white;

    border:none;

    border-radius:10px;

    padding:10px;

}



QPushButton:hover {

    background:#7C3AED;

}



QComboBox,
QSpinBox {

    background:white;

    color:#111111;

    border-radius:8px;

    padding:6px;

}



QCheckBox {

    color:#111111;

}



QFrame {

    background:white;

    border-radius:18px;

}

"""







class ThemeManager:



    def __init__(self):


        self.tema_atual = "Escuro"






    def aplicar(

        self,

        app,

        tema

    ):



        self.tema_atual = tema




        if tema == "Claro":


            app.setStyleSheet(

                LIGHT_THEME

            )



        else:


            app.setStyleSheet(

                DARK_THEME

            )







    def atual(self):


        return self.tema_atual








theme = ThemeManager()