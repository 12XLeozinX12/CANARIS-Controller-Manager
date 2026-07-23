from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QProgressBar,
    QGroupBox,
    QSlider,
    QScrollArea
)


from PySide6.QtCore import (
    Qt,
    QTimer
)


import time


from core.profile_manager import ProfileManager

from core.controller_manager import ControllerManager

from core.calibration_manager import calibration

from core.drift_detector import drift

from core.calibration_wizard import wizard


from core.language_manager import language



from gui.widgets.stick_visualizer import StickVisualizer

from gui.widgets.trigger_visualizer import TriggerVisualizer

from gui.widgets.notification import notification





class Calibration(QWidget):


    def __init__(self):

        super().__init__()



        # =========================
        # CONTROLLER
        # =========================


        self.controller_manager = ControllerManager()

        self.profile_manager = ProfileManager()

        self.guid = None


        self.testando_drift = False


        self.calibracao_assistente = False




        # =========================
        # INTERFACE
        # =========================


        self.setup_ui()



        # =========================
        # IDIOMA
        # =========================


        language.idioma_alterado.connect(

            self.atualizar_textos

        )





        # =========================
        # TIMER
        # =========================


        self.timer = QTimer(
            self
        )


        self.timer.timeout.connect(

            self.atualizar

        )


        self.timer.start(
            100
        )




        self.atualizar_textos()







    # =========================
    # INTERFACE
    # =========================


    def setup_ui(self):


        self.setObjectName(
            "CalibrationPage"
        )



        self.setStyleSheet("""


        QWidget#CalibrationPage{


            background:#050507;


        }



        QLabel{


            color:#F8FAFC;


        }




        QGroupBox{


            color:#A855F7;

            font-size:17px;

            font-weight:bold;

            background:#0B0B12;

            border:none;

            border-radius:18px;

            margin-top:10px;


        }





        QGroupBox::title{


            subcontrol-origin:margin;

            left:15px;

            padding:0 5px;


        }





        QPushButton{


            background:#11111A;

            color:white;

            border:none;

            border-radius:12px;

            padding:12px;


        }




        QPushButton:hover{


            background:#8B5CF6;


        }





        QProgressBar{


            background:#11111A;

            border:none;

            border-radius:8px;

            height:15px;


        }





        QProgressBar::chunk{


            background:#8B5CF6;

            border-radius:8px;


        }





        QSlider::groove:horizontal{


            background:#222;

            height:5px;


        }





        QSlider::handle:horizontal{


            background:#8B5CF6;

            width:14px;

            margin:-5px;

            border-radius:7px;


        }



        """)





        principal = QVBoxLayout(
            self
        )



        principal.setContentsMargins(
            0,
            0,
            0,
            0
        )




        scroll = QScrollArea()



        scroll.setWidgetResizable(
            True
        )



        scroll.setHorizontalScrollBarPolicy(

            Qt.ScrollBarAlwaysOff

        )




        container = QWidget()



        self.layout = QVBoxLayout(
            container
        )



        self.layout.setContentsMargins(
            30,
            30,
            30,
            30
        )



        self.layout.setSpacing(
            20
        )



        scroll.setWidget(
            container
        )



        principal.addWidget(
            scroll
        )





        # continua na parte 2/4
        # =========================
        # TITULO
        # =========================


        self.titulo = QLabel()



        self.titulo.setStyleSheet("""


        color:#A855F7;

        font-size:32px;

        font-weight:bold;


        """)



        self.status = QLabel()



        self.layout.addWidget(
            self.titulo
        )



        self.layout.addWidget(
            self.status
        )







        # =========================
        # ASSISTENTE
        # =========================


        self.grupo_assistente = QGroupBox()



        assist_layout = QVBoxLayout(

            self.grupo_assistente

        )




        self.etapa_texto = QLabel()



        self.barra_calibracao = QProgressBar()



        self.barra_calibracao.setRange(

            0,

            100

        )




        self.btn_assistente = QPushButton()



        self.btn_assistente.clicked.connect(

            self.iniciar_assistente

        )





        assist_layout.addWidget(

            self.etapa_texto

        )



        assist_layout.addWidget(

            self.barra_calibracao

        )



        assist_layout.addWidget(

            self.btn_assistente

        )




        self.layout.addWidget(

            self.grupo_assistente

        )









        # =========================
        # STICKS
        # =========================


        self.grupo_sticks = QGroupBox()



        sticks_layout = QHBoxLayout(

            self.grupo_sticks

        )



        sticks_layout.setSpacing(

            30

        )





        left_box = QVBoxLayout()



        self.left_label = QLabel()



        left_box.addWidget(

            self.left_label

        )




        self.left_visual = StickVisualizer()



        left_box.addWidget(

            self.left_visual

        )






        right_box = QVBoxLayout()



        self.right_label = QLabel()



        right_box.addWidget(

            self.right_label

        )




        self.right_visual = StickVisualizer()



        right_box.addWidget(

            self.right_visual

        )






        sticks_layout.addLayout(

            left_box

        )



        sticks_layout.addLayout(

            right_box

        )





        self.layout.addWidget(

            self.grupo_sticks

        )







        # =========================
        # TRIGGERS
        # =========================


        self.grupo_trigger = QGroupBox()



        trigger_layout = QHBoxLayout(

            self.grupo_trigger

        )





        self.l2_visual = TriggerVisualizer(

            "L2"

        )



        self.r2_visual = TriggerVisualizer(

            "R2"

        )





        trigger_layout.addWidget(

            self.l2_visual

        )



        trigger_layout.addWidget(

            self.r2_visual

        )




        self.layout.addWidget(

            self.grupo_trigger

        )





        # continua na parte 3/4
        # =========================
        # DRIFT
        # =========================

        self.grupo_drift = QGroupBox()

        drift_layout = QVBoxLayout(

            self.grupo_drift

        )

        self.drift_left = QLabel()

        self.drift_right = QLabel()

        self.barra_drift = QProgressBar()

        self.barra_drift.setRange(

            0,

            100

        )

        self.btn_drift = QPushButton()

        self.btn_drift.clicked.connect(

            self.iniciar_drift

        )

        drift_layout.addWidget(

            self.drift_left

        )

        drift_layout.addWidget(

            self.drift_right

        )

        drift_layout.addWidget(

            self.barra_drift

        )

        drift_layout.addWidget(

            self.btn_drift

        )

        self.layout.addWidget(

            self.grupo_drift

        )

        # =========================
        # DEADZONE
        # =========================

        self.grupo_deadzone = QGroupBox()

        dead_layout = QVBoxLayout(

            self.grupo_deadzone

        )

        self.txt_dead_left = QLabel()

        self.dead_left = QSlider(

            Qt.Horizontal

        )

        self.dead_left.setRange(

            0,

            50

        )

        self.dead_left.setValue(

            8

        )

        self.txt_dead_right = QLabel()

        self.dead_right = QSlider(

            Qt.Horizontal

        )

        self.dead_right.setRange(

            0,

            50

        )

        self.dead_right.setValue(

            8

        )

        dead_layout.addWidget(

            self.txt_dead_left

        )

        dead_layout.addWidget(

            self.dead_left

        )

        dead_layout.addWidget(

            self.txt_dead_right

        )

        dead_layout.addWidget(

            self.dead_right

        )

        self.layout.addWidget(

            self.grupo_deadzone

        )

        # =========================
        # SALVAR
        # =========================

        self.salvar = QPushButton()

        self.salvar.clicked.connect(

            self.salvar_calibracao

        )

        self.layout.addWidget(

            self.salvar

        )

        self.layout.addStretch()

    # =========================
    # TRADUÇÃO
    # =========================

    def atualizar_textos(self):
        self.titulo.setText(

            "🎯 "

            +

            language.texto(

                "calibracao_titulo"

            )

        )

        self.status.setText(

            language.texto(

                "calibracao_status"

            )

        )

        self.grupo_assistente.setTitle(

            "🚀 "

            +

            language.texto(

                "assistente_calibracao"

            )

        )

        self.etapa_texto.setText(

            language.texto(

                "aguardando_inicio"

            )

        )

        self.btn_assistente.setText(

            "🚀 "

            +

            language.texto(

                "iniciar_assistente"

            )

        )

        self.grupo_sticks.setTitle(

            "🎮 "

            +

            language.texto(

                "analogicos"

            )

        )

        self.left_label.setText(

            language.texto(

                "left_stick"

            )

        )

        self.right_label.setText(

            language.texto(

                "right_stick"

            )

        )

        self.grupo_trigger.setTitle(

            "🔘 "

            +

            language.texto(

                "gatilhos"

            )

        )

        self.grupo_drift.setTitle(

            "🔍 "

            +

            language.texto(

                "teste_drift"

            )

        )

        self.btn_drift.setText(

            "🔄 "

            +

            language.texto(

                "iniciar_drift"

            )

        )

        self.grupo_deadzone.setTitle(

            "⚙ "

            +

            language.texto(

                "deadzone"

            )

        )

        self.txt_dead_left.setText(

            language.texto(

                "left_stick"

            )

        )

        self.txt_dead_right.setText(

            language.texto(

                "right_stick"

            )

        )

        self.salvar.setText(

            "💾 "

            +

            language.texto(

                "salvar_calibracao"

            )

        )


    # =========================
    # ASSISTENTE
    # =========================


    def iniciar_assistente(self):


        wizard.iniciar()



        self.calibracao_assistente = True



        self.btn_assistente.setEnabled(

            False

        )




        self.etapa_texto.setText(

            wizard.texto_etapa()

        )




        notification.info(

            language.texto(

                "assistente_iniciado"

            )

        )







    # =========================
    # DRIFT
    # =========================


    def iniciar_drift(self):


        drift.reset()



        self.testando_drift = True




        self.btn_drift.setEnabled(

            False

        )




        self.btn_drift.setText(

            "⏳ "

            +

            language.texto(

                "testando"

            )

        )




        notification.info(

            language.texto(

                "drift_iniciado"

            )

        )









    # =========================
    # ATUALIZAÇÃO
    # =========================


    def atualizar(self):


        try:


            controles = (

                self.controller_manager

                .detectar_controles()

            )




            if not controles:


                self.status.setText(

                    "❌ "

                    +

                    language.texto(

                        "nenhum_controle"

                    )

                )


                return

            controle = controles[0]

            novo_guid = controle["guid"]

            # mudou o controle conectado
            if novo_guid != self.guid:
                self.guid = novo_guid

                self.carregar_calibracao()




            self.status.setText(

                "✅ "

                +

                controle["nome"]

            )







            estado = (

                self.controller_manager

                .get_state()

            )




            eixos = estado["axes"]






            if len(eixos) >= 4:



                self.left_visual.atualizar(

                    eixos[0],

                    eixos[1],

                    self.dead_left.value() / 100

                )




                self.right_visual.atualizar(

                    eixos[2],

                    eixos[3],

                    self.dead_right.value() / 100

                )







            self.l2_visual.atualizar(

                estado["triggers"]["L2"]

            )




            self.r2_visual.atualizar(

                estado["triggers"]["R2"]

            )









            # =========================
            # ASSISTENTE
            # =========================


            if self.calibracao_assistente:



                wizard.adicionar_estado(

                    estado

                )




                self.barra_calibracao.setValue(

                    wizard.progresso()

                )




                self.etapa_texto.setText(

                    wizard.texto_etapa()

                )






                if wizard.finalizado:



                    self.calibracao_assistente = False




                    self.btn_assistente.setEnabled(

                        True

                    )




                    self.btn_assistente.setText(

                        "✅ "

                        +

                        language.texto(

                            "concluido"

                        )

                    )





                    notification.success(

                        language.texto(

                            "calibracao_concluida"

                        )

                    )









            # =========================
            # DRIFT
            # =========================


            if self.testando_drift:



                drift.adicionar_leitura(

                    eixos

                )




                self.barra_drift.setValue(

                    drift.progresso()

                )






                if drift.finalizado():



                    self.testando_drift = False




                    self.btn_drift.setEnabled(

                        True

                    )




                    self.btn_drift.setText(

                        "🔄 "

                        +

                        language.texto(

                            "iniciar_drift"

                        )

                    )




                    resultado = drift.analisar()





                    self.drift_left.setText(

                        f"Left: {resultado['left']['valor']}"

                    )




                    self.drift_right.setText(

                        f"Right: {resultado['right']['valor']}"

                    )





                    notification.success(

                        language.texto(

                            "drift_finalizado"

                        )

                    )




        except Exception:

            pass

    # =========================
    # CARREGAR CALIBRAÇÃO
    # =========================

    def carregar_calibracao(self):

        if not self.guid:
            return

        dados = calibration.carregar(

            self.guid

        )

        self.dead_left.setValue(

            int(
                dados.get(
                    "deadzone_left",
                    0.08
                )
                *
                100
            )

        )

        self.dead_right.setValue(

            int(
                dados.get(
                    "deadzone_right",
                    0.08
                )
                *
                100
            )

        )

        print(
            "CALIBRAÇÃO CARREGADA:",
            dados
        )

        notification.info(

            "🎮 Calibração carregada"

        )








    # =========================
    # SALVAR CALIBRAÇÃO
    # =========================

    def salvar_calibracao(self):

        if not self.guid:
            notification.warning(

                language.texto(

                    "conecte_controle"

                )

            )

            return

        dados = {

            "deadzone_left":

                self.dead_left.value() / 100,

            "deadzone_right":

                self.dead_right.value() / 100,

            "trigger_deadzone":

                0.05

        }

        try:

            # Salva calibração individual

            calibration.salvar(

                self.guid,

                dados

            )

            # Atualiza perfil do controle

            self.profile_manager.update_controller_data(

                self.guid,

                "calibration",

                dados

            )

            self.status.setText(

                "✅ "

                +

                language.texto(

                    "calibracao_salva"

                )

            )

            notification.success(

                language.texto(

                    "calibracao_salva"

                )

            )





        except Exception as erro:

            print(

                "ERRO AO SALVAR CALIBRAÇÃO:",

                erro

            )

            notification.error(

                str(erro)

            )









    # =========================
    # SHOW EVENT
    # =========================


    def showEvent(self,event):


        super().showEvent(

            event

        )


        self.atualizar()