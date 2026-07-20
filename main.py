import sys

from PySide6.QtWidgets import (
    QApplication,
    QMessageBox
)

from PySide6.QtGui import QIcon

from gui.main_window import MainWindow
from gui.update_window import UpdateWindow

from core.logger import CanarisLogger
from core.update_manager import update
from core.downloader import Downloader




def main():


    logger = CanarisLogger()

    logger.info(
        "CANARIS iniciado."
    )



    app = QApplication(
        sys.argv
    )



    app.setWindowIcon(
        QIcon(
            "assets/icons/canaris.ico"
        )
    )





    # ==========================
    # ATUALIZAÇÃO
    # ==========================


    try:


        resultado = (
            update
            .verificar_atualizacao()
        )



        if resultado.get(
            "update",
            False
        ):


            janela = UpdateWindow(

                resultado["version"]

            )


            janela.show()



            def iniciar_download():


                downloader = Downloader()



                downloader.baixar(

                    resultado["download"],

                    "CANARIS_UPDATE.exe",

                    janela.progress.setValue

                )



                janela.info.setText(

                    """
Atualização concluída!

Reinicie o CANARIS.
"""

                )



            janela.button.clicked.connect(
                iniciar_download
            )



            janela.exec()





    except Exception as erro:


        logger.error(
            f"Erro atualização: {erro}"
        )







    # ==========================
    # ABRIR APP
    # ==========================


    window = MainWindow()


    window.show()



    sys.exit(
        app.exec()
    )






if __name__ == "__main__":

    main()