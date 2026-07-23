import time

from database.stats import StatsManager


class StatisticsManager:

    def __init__(self):

        self.stats = StatsManager()

        self.user_id = None

        self.session_start = None

    # =====================================
    # INICIAR SESSÃO
    # =====================================

    def start_session(self, user_id, controller_name):

        self.user_id = user_id

        self.session_start = time.time()

        self.stats.add_session(user_id)

        self.stats.set_favorite_controller(

            user_id,

            controller_name

        )

        print(
            "[STATS] Sessão iniciada."
        )

    # =====================================
    # BOTÃO
    # =====================================

    def button_pressed(self):

        if self.user_id is None:
            return

        self.stats.add_button_press(

            self.user_id

        )

    # =====================================
    # ANALÓGICOS
    # =====================================

    def analog_moved(self, distance):

        if self.user_id is None:
            return

        self.stats.add_analog_distance(

            self.user_id,

            distance

        )

    # =====================================
    # FINALIZAR
    # =====================================

    def finish_session(self):

        if self.user_id is None:
            return

        tempo = (

            time.time()

            - self.session_start

        ) / 3600

        self.stats.db.cursor.execute(

            """
            UPDATE game_stats

            SET total_hours =
            total_hours + ?

            WHERE user_id = ?
            """,

            (
                tempo,

                self.user_id

            )

        )

        self.stats.db.connection.commit()

        print(

            "[STATS] Sessão encerrada:",

            round(

                tempo,

                4

            ),

            "horas"

        )