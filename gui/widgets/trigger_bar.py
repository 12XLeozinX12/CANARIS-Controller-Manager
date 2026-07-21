from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar
)

from PySide6.QtCore import Qt




class TriggerBar(QWidget):


    def __init__(self, nome):

        super().__init__()


        self.nome = nome


        layout = QVBoxLayout(
            self
        )


        self.label = QLabel(
            f"{nome}: 0%"
        )


        self.label.setStyleSheet(
            """
            color:white;
            font-size:14px;
            font-weight:bold;
            """
        )



        self.bar = QProgressBar()



        self.bar.setRange(
            0,
            100
        )


        self.bar.setValue(
            0
        )



        self.bar.setTextVisible(
            True
        )



        self.bar.setStyleSheet(
            """
            QProgressBar{

                background:#222;

                border-radius:8px;

                height:20px;

                color:white;

            }


            QProgressBar::chunk{

                background:#8B5CF6;

                border-radius:8px;

            }

            """
        )



        layout.addWidget(
            self.label
        )


        layout.addWidget(
            self.bar
        )







    def set_value(self, valor):


        try:

            valor = float(valor)


        except:

            valor = 0




        # aceita 0-1 ou 0-100


        if valor <= 1:

            valor *= 100




        valor = int(
            max(
                0,
                min(
                    100,
                    valor
                )
            )
        )



        self.bar.setValue(
            valor
        )


        self.label.setText(

            f"{self.nome}: {valor}%"

        )