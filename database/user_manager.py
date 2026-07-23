from database.database import Database


class UserManager:

    def __init__(self):

        self.db = Database()


    # ===============================
    # BUSCAR USUÁRIO
    # ===============================

    def get_user(self, user_id):

        self.db.cursor.execute(

            """
            SELECT *
            FROM users
            WHERE id = ?
            """,

            (user_id,)

        )

        user = self.db.cursor.fetchone()

        if user:

            return dict(user)

        return None


    # ===============================
    # PERFIL GAMER
    # ===============================

    def get_profile(self, user_id):

        self.db.cursor.execute(

            """
            SELECT *
            FROM gamer_profile
            WHERE user_id = ?
            """,

            (user_id,)

        )

        data = self.db.cursor.fetchone()

        if data:

            return dict(data)

        return None


    def update_profile(

        self,

        user_id,

        nickname,

        platform,

        avatar,

        theme

    ):

        self.db.cursor.execute(

            """
            UPDATE gamer_profile

            SET

                nickname=?,

                platform=?,

                avatar=?,

                theme=?

            WHERE user_id=?
            """,

            (

                nickname,

                platform,

                avatar,

                theme,

                user_id

            )

        )

        self.db.connection.commit()


    # ===============================
    # CONFIGURAÇÕES
    # ===============================

    def get_settings(self, user_id):

        self.db.cursor.execute(

            """
            SELECT *

            FROM settings

            WHERE user_id = ?
            """,

            (user_id,)

        )

        row = self.db.cursor.fetchone()

        if row:

            return dict(row)

        return None


    def update_settings(

        self,

        user_id,

        language,

        theme,

        notifications,

        startup

    ):

        self.db.cursor.execute(

            """
            UPDATE settings

            SET

                language=?,

                theme=?,

                notifications=?,

                startup=?

            WHERE user_id=?
            """,

            (

                language,

                theme,

                notifications,

                startup,

                user_id

            )

        )

        self.db.connection.commit()


    # ===============================
    # ESTATÍSTICAS
    # ===============================

    def get_statistics(self, user_id):

        self.db.cursor.execute(

            """
            SELECT *

            FROM statistics

            WHERE user_id=?
            """,

            (user_id,)

        )

        row = self.db.cursor.fetchone()

        if row:

            return dict(row)

        return None


    def add_play_time(

        self,

        user_id,

        minutes

    ):

        self.db.cursor.execute(

            """
            UPDATE statistics

            SET

                play_time = play_time + ?

            WHERE user_id = ?
            """,

            (

                minutes,

                user_id

            )

        )

        self.db.connection.commit()


    def add_controller_connection(

        self,

        user_id

    ):

        self.db.cursor.execute(

            """
            UPDATE statistics

            SET

                controllers_connected =

                controllers_connected + 1

            WHERE user_id = ?
            """,

            (

                user_id,

            )

        )

        self.db.connection.commit()


    def add_launch(self, user_id):

        self.db.cursor.execute(

            """
            UPDATE statistics

            SET launches = launches + 1

            WHERE user_id = ?
            """,

            (

                user_id,

            )

        )

        self.db.connection.commit()