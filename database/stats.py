from database.database import Database


class StatsManager:

    def __init__(self):
        self.db = Database()

    # ==========================================
    # CRIA REGISTRO CASO NÃO EXISTA
    # ==========================================

    def create_stats(self, user_id):

        self.db.cursor.execute("""

        INSERT OR IGNORE INTO game_stats(

            user_id

        )

        VALUES(?)

        """, (user_id,))

        self.db.connection.commit()

    # ==========================================
    # NOVA SESSÃO
    # ==========================================

    def add_session(self, user_id):

        self.create_stats(user_id)

        self.db.cursor.execute("""

        UPDATE game_stats

        SET total_sessions = total_sessions + 1

        WHERE user_id = ?

        """, (user_id,))

        self.db.connection.commit()

    # ==========================================
    # BOTÃO PRESSIONADO
    # ==========================================

    def add_button_press(self, user_id):

        self.create_stats(user_id)

        self.db.cursor.execute("""

        UPDATE game_stats

        SET buttons_pressed = buttons_pressed + 1

        WHERE user_id = ?

        """, (user_id,))

        self.db.connection.commit()

    # ==========================================
    # DISTÂNCIA DOS ANALÓGICOS
    # ==========================================

    def add_analog_distance(self, user_id, distance):

        self.create_stats(user_id)

        self.db.cursor.execute("""

        UPDATE game_stats

        SET analog_distance = analog_distance + ?

        WHERE user_id = ?

        """, (distance, user_id))

        self.db.connection.commit()

    # ==========================================
    # CONTROLE FAVORITO
    # ==========================================

    def set_favorite_controller(self, user_id, controller_name):

        self.create_stats(user_id)

        self.db.cursor.execute("""

        UPDATE game_stats

        SET favorite_controller = ?

        WHERE user_id = ?

        """, (controller_name, user_id))

        self.db.connection.commit()

    # ==========================================
    # PEGAR ESTATÍSTICAS
    # ==========================================

    def get_stats(self, user_id):

        self.create_stats(user_id)

        self.db.cursor.execute("""

        SELECT *

        FROM game_stats

        WHERE user_id = ?

        """, (user_id,))

        row = self.db.cursor.fetchone()

        if not row:
            return None

        return {

            "user_id": row[0],

            "total_sessions": row[1],

            "total_hours": row[2],

            "buttons_pressed": row[3],

            "analog_distance": row[4],

            "favorite_controller": row[5]

        }