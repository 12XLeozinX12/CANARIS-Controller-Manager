from database.database import Database


class GameStats:

    def __init__(self):

        self.db = Database()

    # ===============================
    # CRIAR ESTATISTICAS
    # ===============================

    def create_stats(self, user_id):

        try:

            self.db.cursor.execute("""

            INSERT OR IGNORE INTO game_stats(

                user_id,

                total_sessions,

                total_hours,

                buttons_pressed,

                analog_distance,

                favorite_controller

            )

            VALUES(

                ?,

                0,

                0,

                0,

                0,

                'Nenhum'

            )

            """, (user_id,))

            self.db.connection.commit()

            return True

        except Exception as erro:

            print(erro)

            return False

    # ===============================
    # BUSCAR
    # ===============================

    def get_stats(self, user_id):

        self.db.cursor.execute("""

        SELECT *

        FROM game_stats

        WHERE user_id=?

        """, (user_id,))

        dados = self.db.cursor.fetchone()

        if not dados:

            return None

        return {

            "user_id": dados[0],

            "total_sessions": dados[1],

            "total_hours": dados[2],

            "buttons_pressed": dados[3],

            "analog_distance": dados[4],

            "favorite_controller": dados[5]

        }

    # ===============================
    # SOMAR SESSÃO
    # ===============================

    def add_session(self, user_id):

        self.db.cursor.execute("""

        UPDATE game_stats

        SET total_sessions = total_sessions + 1

        WHERE user_id=?

        """, (user_id,))

        self.db.connection.commit()

    # ===============================
    # SOMAR HORAS
    # ===============================

    def add_hours(self, user_id, horas):

        self.db.cursor.execute("""

        UPDATE game_stats

        SET total_hours = total_hours + ?

        WHERE user_id=?

        """, (horas, user_id))

        self.db.connection.commit()

    # ===============================
    # BOTÕES
    # ===============================

    def add_button_press(self, user_id):

        self.db.cursor.execute("""

        UPDATE game_stats

        SET buttons_pressed = buttons_pressed + 1

        WHERE user_id=?

        """, (user_id,))

        self.db.connection.commit()

    # ===============================
    # ANALÓGICOS
    # ===============================

    def add_analog_distance(self, user_id, valor):

        self.db.cursor.execute("""

        UPDATE game_stats

        SET analog_distance = analog_distance + ?

        WHERE user_id=?

        """, (valor, user_id))

        self.db.connection.commit()

    # ===============================
    # CONTROLE FAVORITO
    # ===============================

    def set_controller(self, user_id, nome):

        self.db.cursor.execute("""

        UPDATE game_stats

        SET favorite_controller=?

        WHERE user_id=?

        """, (nome, user_id))

        self.db.connection.commit()