import sys


from PySide6.QtWidgets import (
    QApplication
)


from PySide6.QtGui import QIcon


from gui.main_window import MainWindow


from gui.update_window import UpdateWindow


from core.update_manager import update


from core.downloader import Downloader


from core.logger import CanarisLogger





def main():



    logger = CanarisLogger()


    logger.info(
        "CANARIS iniciado"
    )



    app = QApplication(
        sys.argv
    )



    app.setWindowIcon(

        QIcon(
            "assets/icons/canaris.ico"
        )

    )




    try:


        resultado = (

            update
            .verificar_atualizacao()

        )



        if resultado["update"]:


            janela = UpdateWindow(

                resultado["version"]

            )



            janela.info.setText(

f"""
Nova versão:

{resultado['version']}


Alterações:

"""
+
"\n".join(
    resultado["changelog"]
)

            )




            def baixar():


                downloader = Downloader()



                downloader.baixar(

                    resultado["download"],

                    "CANARIS_NEW.exe",

                    janela.progress.setValue

                )



                janela.info.setText(

                    "Atualização baixada!"

                )





            janela.button.clicked.connect(

                baixar

            )



            janela.exec()



    except Exception as erro:


        print(
            "Update falhou:",
            erro
        )





    window = MainWindow()


    window.show()



    sys.exit(
        app.exec()
    )





if __name__ == "__main__":

    main()