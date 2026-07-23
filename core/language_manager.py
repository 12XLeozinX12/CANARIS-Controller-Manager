# =====================================================
# CANARIS ™ Language Manager
# Sistema global de idiomas
# =====================================================


from PySide6.QtCore import QObject, Signal



class LanguageManager(QObject):


    idioma_alterado = Signal()



    def __init__(self):

        super().__init__()


        self.idioma = "pt"



        self.textos = {



            # =================================================
            # PORTUGUÊS
            # =================================================

            "pt": {


                # SIDEBAR

                "dashboard":
                    "Dashboard",

                "controles":
                    "Controles",

                "controller_lab":
                    "Controller Lab",

                "perfis":
                    "Perfis",

                "calibracao":
                    "Calibração",

                "settings":
                    "Configurações",

                "sobre":
                    "Sobre",



                # DASHBOARD


                "dashboard_titulo":
                    "CANARIS ™ Dashboard",


                "dashboard_descricao":
                    "Central inteligente para gerenciamento, calibração e personalização dos seus controles.",


                "dashboard_controles":
                    "Controles",


                "dashboard_perfis":
                    "Perfis",


                "dashboard_status":
                    "Sistema Online",


                "teste_notificacao":
                    "Testar Notificação",


                "notificacao_teste":
                    "Sistema de notificações funcionando!",



                # STATUS


                "sistema_online":
                    "Sistema Online",

                "sistema_offline":
                    "Sistema Offline",

                "nenhum_dispositivo":
                    "Nenhum dispositivo encontrado",

                "carregando":
                    "Carregando...",

                "conectado":
                    "Conectado",

                "desconectado":
                    "Desconectado",


                "status_controles":
                    "Status dos Controles",


                "status_calibracao":
                    "Status da Calibração",


                "status_perfis":
                    "Status dos Perfis",


                "status_sistema":
                    "Status do Sistema",


                "dashboard_status_controle":
                    "Controle conectado",


                "dashboard_status_calibracao":
                    "Calibração pronta",
                # =================================================
                # CONTROLLERS
                # =================================================

                "controles_titulo":
                    "Controles",

                "controles_descricao":
                    "Gerencie seus dispositivos conectados",

                "controles_detectados":
                    "Controles Detectados",

                "atualizar":
                    "Atualizar",

                "nenhum_controle":
                    "Nenhum controle conectado",

                "controle_conectado":
                    "Controle conectado",

                "controle_selecionado":
                    "Controle selecionado",

                "nome":
                    "Nome",

                "tipo":
                    "Tipo",

                "guid":
                    "GUID",

                # =================================================
                # CONTROLLER LAB
                # =================================================

                "controller_lab_titulo":
                    "CANARIS Controller Lab",

                "controller_lab_subtitulo":
                    "Monitoramento do Controle em Tempo Real",

                "controller_status":
                    "Status do Controle",

                "controller_botoes":
                    "Botões",

                "controller_eixos":
                    "Analógicos / Gatilhos",

                "controller_dpad":
                    "Direcional",

                "controller_sem_controle":
                    "Nenhum Controle",

                "controller_desconectado":
                    "Nenhum Controle Conectado",

                "eixo":
                    "Eixo",

                "ligado":
                    "ATIVO",

                "desligado":
                    "---",

                "nao_disponivel":
                    "N/D",

                "hat":
                    "Direcional",

                "controle_conectado_lab":
                    "Controle conectado",

                "controle_desconectado_lab":
                    "Controle desconectado",

                # =================================================
                # PERFIS
                # =================================================

                "perfil":
                    "Criar Perfil",

                "nome_perfil":
                    "Nome do perfil",

                "perfil_criado":
                    "Perfil criado com sucesso",

                # =================================================
                # CALIBRAÇÃO
                # =================================================

                "calibracao_titulo":
                    "Calibração de Controle",

                "calibracao_status":
                    "Procurando controle...",

                "procurando_controle":
                    "Procurando controle...",

                "assistente_calibracao":
                    "Assistente de Calibração",

                "aguardando_inicio":
                    "Aguardando início...",

                "iniciar_assistente":
                    "Iniciar Assistente",

                "analogicos":
                    "Analógicos",

                "left_stick":
                    "Analógico Esquerdo",

                "right_stick":
                    "Analógico Direito",

                "gatilhos":
                    "Gatilhos",

                "drift":
                    "Teste de Drift",

                "teste_drift":
                    "Teste de Drift",

                "iniciar_drift":
                    "Iniciar teste de Drift",

                "testando":
                    "Testando...",

                "deadzone":
                    "Deadzone",

                "salvar_calibracao":
                    "Salvar calibração",

                "calibracao_salva":
                    "Calibração salva com sucesso",

                "calibracao_concluida":
                    "Calibração concluída",

                "concluido":
                    "Concluído",

                # =================================================
                # NOTIFICAÇÕES
                # =================================================

                "assistente_iniciado":
                    "Assistente de calibração iniciado!",

                "drift_iniciado":
                    "Teste de drift iniciado!",

                "drift_finalizado":
                    "Teste de drift finalizado!",

                "salvo_sucesso":
                    "Calibração salva com sucesso!",

                "conecte_controle":
                    "Conecte um controle primeiro",

                "erro":
                    "Erro",

                "sucesso":
                    "Sucesso",

                "aviso":
                    "Aviso",

                "informacao":
                    "Informação"

            },

            # =================================================
            # ENGLISH
            # =================================================

            "en": {

                # SIDEBAR

                "dashboard":
                    "Dashboard",

                "controles":
                    "Controllers",

                "controller_lab":
                    "Controller Lab",

                "perfis":
                    "Profiles",

                "calibracao":
                    "Calibration",

                "settings":
                    "Settings",

                "sobre":
                    "About",

                # DASHBOARD

                "dashboard_titulo":
                    "CANARIS ™ Dashboard",

                "dashboard_descricao":
                    "Smart center for managing, calibrating and customizing your controllers.",

                "dashboard_controles":
                    "Controllers",

                "dashboard_perfis":
                    "Profiles",

                "dashboard_status":
                    "System Online",

                "teste_notificacao":
                    "Test Notification",

                "notificacao_teste":
                    "Notification system working!",

                # STATUS

                "sistema_online":
                    "System Online",

                "sistema_offline":
                    "System Offline",

                "nenhum_dispositivo":
                    "No device found",

                "carregando":
                    "Loading...",

                "conectado":
                    "Connected",

                "desconectado":
                    "Disconnected",
                "status_controles":
                    "Controller Status",

                "status_calibracao":
                    "Calibration Status",

                "status_perfis":
                    "Profile Status",

                "status_sistema":
                    "System Status",

                "dashboard_status_controle":
                    "Controller connected",

                "dashboard_status_calibracao":
                    "Calibration ready",

                # =================================================
                # CONTROLLERS
                # =================================================

                "controles_titulo":
                    "Controllers",

                "controles_descricao":
                    "Manage your connected devices",

                "controles_detectados":
                    "Detected Controllers",

                "atualizar":
                    "Refresh",

                "nenhum_controle":
                    "No controller connected",

                "controle_conectado":
                    "Controller connected",

                "controle_selecionado":
                    "Controller selected",

                "nome":
                    "Name",

                "tipo":
                    "Type",

                "guid":
                    "GUID",

                # =================================================
                # CONTROLLER LAB
                # =================================================

                "controller_lab_titulo":
                    "CANARIS Controller Lab",

                "controller_lab_subtitulo":
                    "Real Time Controller Monitor",

                "controller_status":
                    "Controller Status",

                "controller_botoes":
                    "Buttons",

                "controller_eixos":
                    "Analog / Triggers",

                "controller_dpad":
                    "D-Pad",

                "controller_sem_controle":
                    "No Controller",

                "controller_desconectado":
                    "No Controller Connected",

                "eixo":
                    "Axis",

                "ligado":
                    "ON",

                "desligado":
                    "---",

                "nao_disponivel":
                    "N/A",

                "hat":
                    "HAT",

                "controle_conectado_lab":
                    "Controller connected",

                "controle_desconectado_lab":
                    "Controller disconnected",

                # =================================================
                # PERFIS
                # =================================================

                "perfil":
                    "Create Profile",

                "nome_perfil":
                    "Profile name",

                "perfil_criado":
                    "Profile created successfully",

                # =================================================
                # CALIBRATION
                # =================================================

                "calibracao_titulo":
                    "Controller Calibration",

                "calibracao_status":
                    "Searching controller...",

                "procurando_controle":
                    "Searching controller...",

                "assistente_calibracao":
                    "Calibration Wizard",

                "aguardando_inicio":
                    "Waiting start...",

                "iniciar_assistente":
                    "Start Wizard",

                "analogicos":
                    "Analog Sticks",

                "left_stick":
                    "Left Stick",

                "right_stick":
                    "Right Stick",

                "gatilhos":
                    "Triggers",

                "drift":
                    "Drift Test",

                "teste_drift":
                    "Drift Test",

                "iniciar_drift":
                    "Start Drift Test",

                "testando":
                    "Testing...",

                "deadzone":
                    "Deadzone",

                "salvar_calibracao":
                    "Save Calibration",

                "calibracao_salva":
                    "Calibration saved successfully",

                "calibracao_concluida":
                    "Calibration completed",

                "concluido":
                    "Completed",

                # =================================================
                # NOTIFICATIONS
                # =================================================

                "assistente_iniciado":
                    "Calibration wizard started!",

                "drift_iniciado":
                    "Drift test started!",

                "drift_finalizado":
                    "Drift test finished!",

                "salvo_sucesso":
                    "Calibration saved successfully!",

                "conecte_controle":
                    "Connect a controller first",

                "erro":
                    "Error",

                "sucesso":
                    "Success",

                "aviso":
                    "Warning",

                "informacao":
                    "Information"

            }

        }

        # =====================================================
        # PEGAR TEXTO
        # =====================================================
    def texto(self, chave):
            return self.textos.get(
                self.idioma,
                {}
            ).get(
                chave,
                chave
            )

        # =====================================================
        # TROCAR IDIOMA
        # =====================================================

    def mudar_idioma(self, idioma):
            if idioma in self.textos:
                self.idioma = idioma

                self.idioma_alterado.emit()

    # =====================================================
    # INSTÂNCIA GLOBAL
    # =====================================================

language = LanguageManager()