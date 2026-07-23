import sys


from PySide6.QtWidgets import (
    QApplication,
    QMessageBox
)

from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer


from gui.main_window import MainWindow

from gui.widgets.notification import notification


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
    # QT APP
    # =========================

    app = QApplication(
        sys.argv
    )


    notification.conectar_app(
        app
    )


    app.notification = notification





    # =========================
    # ICONE
    # =========================

    try:


        app.setWindowIcon(

            QIcon(

                resource_path(

                    "assets/icons/canaris.ico"

                )

            )

        )


    except Exception as erro:


        logger.error(

            f"Erro carregando ícone: {erro}"

        )







    # =========================
    # TEMA
    # =========================

    try:


        tema_atual = settings.get(
            "tema"
        )


        theme.aplicar(

            app,

            tema_atual

        )


    except Exception as erro:


        logger.error(

            f"Erro carregando tema: {erro}"

        )







    # =========================
    # UPDATE
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

                "Nova atualização disponível!"

            )



    except Exception as erro:


        logger.error(

            f"Erro update: {erro}"

        )







    # =========================
    # JANELA PRINCIPAL
    # =========================

    try:


        logger.info(
            "Criando janela principal..."
        )


        window = MainWindow()


        logger.info(
            "Janela criada."
        )


        window.show()


        logger.info(
            "Janela exibida."
        )



    except Exception as erro:


        import traceback


        traceback.print_exc()



        logger.error(

            f"Erro abrindo janela principal: {erro}"

        )



        QMessageBox.critical(

            None,

            "CANARIS ™ CM",

            f"Erro iniciando aplicativo:\n\n{erro}"

        )


        return







    # =========================
    # NOTIFICAÇÃO
    # =========================

    QTimer.singleShot(

        800,

        lambda:

        notification.success(

            "CANARIS ™ iniciado com sucesso!"

        )

    )








    # =========================
    # LOOP QT
    # =========================

    sys.exit(

        app.exec()

    )








if __name__ == "__main__":

    main()