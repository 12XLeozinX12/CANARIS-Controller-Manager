import hashlib

from database.database import Database


class AuthManager:

    def __init__(self):

        self.db = Database()

    # ==============================
    # HASH
    # ==============================

    def hash_password(self, password: str) -> str:

        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    # ==============================
    # CADASTRAR
    # ==============================

    def create_account(

        self,

        username,

        email,

        password

    ):

        password = self.hash_password(password)

        try:

            self.db.cursor.execute(

                """
                INSERT INTO users

                (

                    username,

                    email,

                    password

                )

                VALUES

                (

                    ?,

                    ?,

                    ?

                )
                """,

                (

                    username,

                    email,

                    password

                )

            )

            user_id = self.db.cursor.lastrowid

            self.db.cursor.execute(

                """
                INSERT INTO gamer_profile

                (

                    user_id,

                    nickname,

                    platform,

                    avatar,

                    theme

                )

                VALUES

                (

                    ?,

                    ?,

                    '',

                    '',

                    'Dark'

                )
                """,

                (

                    user_id,

                    username

                )

            )

            self.db.cursor.execute(

                """
                INSERT INTO statistics

                (

                    user_id

                )

                VALUES

                (

                    ?

                )
                """,

                (

                    user_id,

                )

            )

            self.db.cursor.execute(

                """
                INSERT INTO settings

                (

                    user_id

                )

                VALUES

                (

                    ?

                )
                """,

                (

                    user_id,

                )

            )

            self.db.connection.commit()

            return True, "Conta criada com sucesso."

        except Exception as e:

            return False, str(e)

    # ==============================
    # LOGIN
    # ==============================

    def login(

        self,

        username,

        password

    ):

        password = self.hash_password(password)

        self.db.cursor.execute(

            """
            SELECT *

            FROM users

            WHERE

                username = ?

            AND

                password = ?
            """,

            (

                username,

                password

            )

        )

        user = self.db.cursor.fetchone()

        if user:

            return True, dict(user)

        return False, None

    # ==============================
    # EXISTE
    # ==============================

    def user_exists(

        self,

        username

    ):

        self.db.cursor.execute(

            """

            SELECT id

            FROM users

            WHERE username = ?

            """,

            (

                username,

            )

        )

        return self.db.cursor.fetchone() is not None