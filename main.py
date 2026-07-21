import sys


from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon



from gui.main_window import MainWindow


from core.logger import CanarisLogger

from core.update_manager import update

from core.settings_manager import settings

from core.theme_manager import theme

from core.paths import resource_path





def main():



    # =========================
    # LOGGER
    # =========================


    logger = CanarisLogger()


    logger.info(
        "CANARIS iniciado."
    )





    # =========================
    # APP QT
    # =========================


    app = QApplication(
        sys.argv
    )






    # =========================
    # ÍCONE
    # =========================


    app.setWindowIcon(

        QIcon(

            resource_path(

                "assets/icons/canaris.ico"

            )

        )

    )







    # =========================
    # CARREGAR TEMA
    # =========================


    tema_atual = settings.get(

        "tema"

    )



    theme.aplicar(

        app,

        tema_atual

    )









    # =========================
    # ATUALIZAÇÃO
    # =========================


    try:


        resultado = update.verificar_atualizacao()



        if resultado.get(

            "update",

            False

        ):



            QMessageBox.information(

                None,

                "CANARIS ™ CM",

                f"""

Nova versão disponível:

{resultado['version']}


Versão atual:

BETA 0.1.2


Atualize para continuar usando
a versão mais recente.

"""

            )



    except Exception as erro:


        logger.error(

            f"Erro no sistema de atualização: {erro}"

        )









    # =========================
    # JANELA PRINCIPAL
    # =========================


    window = MainWindow()


    window.show()






    # =========================
    # EXECUTAR
    # =========================


    sys.exit(

        app.exec()

    )









if __name__ == "__main__":


    main()