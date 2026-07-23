# ==========================================================
# CANARIS ™ Controller Manager
# Database Manager
# Sistema de Banco de Dados
# ==========================================================


import sqlite3
import os
from pathlib import Path


# ==========================================================
# CAMINHO DO BANCO
# ==========================================================


def get_database_path():
    # Windows

    if os.name == "nt":

        base = os.getenv(
            "APPDATA"
        )


    # Linux

    else:

        base = os.path.expanduser(
            "~/.config"
        )

    folder = os.path.join(

        base,

        "CANARIS CM"

    )

    os.makedirs(

        folder,

        exist_ok=True

    )

    return Path(folder) / "canaris.db"


DB_PATH = get_database_path()


# ==========================================================
# DATABASE
# ==========================================================


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(

            DB_PATH

        )

        self.cursor = self.connection.cursor()

        # Ativa relações entre tabelas

        self.cursor.execute(

            "PRAGMA foreign_keys = ON"

        )

        self.create_tables()

    # ======================================================
    # CRIAR TABELAS
    # ======================================================

    def create_tables(self):

        # ==================================
        # USUÁRIOS
        # ==================================

        self.cursor.execute("""

                            CREATE TABLE IF NOT EXISTS users
                            (

                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,

                                username
                                TEXT
                                UNIQUE
                                NOT
                                NULL,

                                password
                                TEXT
                                NOT
                                NULL,

                                email
                                TEXT,

                                created_at
                                TIMESTAMP
                                DEFAULT
                                CURRENT_TIMESTAMP

                            )

                            """)

        # ==================================
        # PERFIL GAMER
        # ==================================

        self.cursor.execute("""

                            CREATE TABLE IF NOT EXISTS gamer_profile
                            (

                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,

                                user_id
                                INTEGER
                                UNIQUE
                                NOT
                                NULL,

                                nickname
                                TEXT,

                                avatar
                                TEXT
                                DEFAULT
                                '',

                                level
                                INTEGER
                                DEFAULT
                                1,

                                xp
                                INTEGER
                                DEFAULT
                                0,

                                games_played
                                INTEGER
                                DEFAULT
                                0,

                                hours_played
                                REAL
                                DEFAULT
                                0,

                                favorite_game
                                TEXT
                                DEFAULT
                                '',


                                FOREIGN
                                KEY
                            (
                                user_id
                            )
                                REFERENCES users
                            (
                                id
                            )
                                ON DELETE CASCADE

                                )

                            """)

        # ==================================
        # ESTATÍSTICAS GERAIS
        # ==================================

        self.cursor.execute("""

                            CREATE TABLE IF NOT EXISTS gamer_statistics
                            (

                                id
                                INTEGER
                                PRIMARY
                                KEY
                                AUTOINCREMENT,

                                user_id
                                INTEGER
                                NOT
                                NULL,

                                hours_played
                                INTEGER
                                DEFAULT
                                0,

                                games_started
                                INTEGER
                                DEFAULT
                                0,

                                wins
                                INTEGER
                                DEFAULT
                                0,

                                losses
                                INTEGER
                                DEFAULT
                                0,

                                achievements
                                INTEGER
                                DEFAULT
                                0,

                                last_game
                                TEXT,


                                FOREIGN
                                KEY
                            (
                                user_id
                            )
                                REFERENCES users
                            (
                                id
                            )
                                ON DELETE CASCADE

                                )

                            """)

        # ==================================
        # ESTATÍSTICAS AVANÇADAS
        # ==================================

        self.cursor.execute("""

                            CREATE TABLE IF NOT EXISTS game_stats
                            (

                                user_id
                                INTEGER
                                PRIMARY
                                KEY,

                                total_sessions
                                INTEGER
                                DEFAULT
                                0,

                                total_hours
                                REAL
                                DEFAULT
                                0,

                                buttons_pressed
                                INTEGER
                                DEFAULT
                                0,

                                analog_distance
                                REAL
                                DEFAULT
                                0,

                                favorite_controller
                                TEXT
                                DEFAULT
                                'Nenhum',


                                FOREIGN
                                KEY
                            (
                                user_id
                            )
                                REFERENCES users
                            (
                                id
                            )
                                ON DELETE CASCADE

                                )

                            """)

        self.connection.commit()

    # ======================================================
    # COMMIT
    # ======================================================

    def commit(self):

        self.connection.commit()

    # ======================================================
    # FECHAR BANCO
    # ======================================================

    def close(self):

        try:

            self.connection.commit()

            self.connection.close()



        except:

            pass