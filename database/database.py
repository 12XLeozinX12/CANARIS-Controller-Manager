import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "canaris.db"


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

        self.create_tables()

    # ==================================
    # CRIAR TABELAS
    # ==================================

    def create_tables(self):

        # ==================================
        # USUÁRIOS
        # ==================================

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            email TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        # ==================================
        # PERFIL GAMER
        # ==================================

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gamer_profile(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER UNIQUE NOT NULL,

            nickname TEXT,

            avatar TEXT DEFAULT '',

            level INTEGER DEFAULT 1,

            xp INTEGER DEFAULT 0,

            games_played INTEGER DEFAULT 0,

            hours_played REAL DEFAULT 0,

            favorite_game TEXT DEFAULT '',

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )
        """)

        # ==================================
        # ESTATÍSTICAS GERAIS
        # ==================================

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gamer_statistics(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            hours_played INTEGER DEFAULT 0,

            games_started INTEGER DEFAULT 0,

            wins INTEGER DEFAULT 0,

            losses INTEGER DEFAULT 0,

            achievements INTEGER DEFAULT 0,

            last_game TEXT,

            FOREIGN KEY(user_id)
            REFERENCES users(id)

        )
        """)

        # ==================================
        # ESTATÍSTICAS AVANÇADAS
        # ==================================

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_stats(

            user_id INTEGER PRIMARY KEY,

            total_sessions INTEGER DEFAULT 0,

            total_hours REAL DEFAULT 0,

            buttons_pressed INTEGER DEFAULT 0,

            analog_distance REAL DEFAULT 0,

            favorite_controller TEXT DEFAULT 'Nenhum',

            FOREIGN KEY(user_id)
            REFERENCES users(id)

        )
        """)

        self.connection.commit()

    # ==================================
    # FECHAR BANCO
    # ==================================

    def close(self):

        self.connection.commit()
        self.connection.close()