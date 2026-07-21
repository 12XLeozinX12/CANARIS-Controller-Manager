from gui.styles import DARK_THEME



LIGHT_THEME = """

QMainWindow,
QWidget {

background:#f5f5f5;

color:#111;

}


QLabel {

color:#111;

}


QPushButton {

background:#8B5CF6;

color:white;

border-radius:10px;

padding:10px;

}


QPushButton:hover {

background:#7C3AED;

}

QComboBox,
QSpinBox {

background:white;

color:#111;

border-radius:8px;

padding:6px;

}


QCheckBox {

color:#111;

}

"""





class ThemeManager:


    def aplicar(
        self,
        app,
        tema
    ):


        if tema == "Claro":

            app.setStyleSheet(
                LIGHT_THEME
            )


        else:

            app.setStyleSheet(
                DARK_THEME
            )





theme = ThemeManager()