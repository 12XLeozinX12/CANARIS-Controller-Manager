from database.database import Database



class Models:


    def __init__(self):

        self.db = Database()


        self.create_models()



    # ==================================
    # CRIAR MODELOS
    # ==================================

    def create_models(self):


        self.create_users()


        self.create_gamer_profile()



    # ==================================
    # USUARIOS
    # ==================================

    def create_users(self):


        self.db.cursor.execute(

        """

        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            email TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """

        )



        self.db.connection.commit()



    # ==================================
    # PERFIL GAMER
    # ==================================

    def create_gamer_profile(self):


        self.db.cursor.execute(

        """

        CREATE TABLE IF NOT EXISTS gamer_profile(


            id INTEGER PRIMARY KEY AUTOINCREMENT,


            user_id INTEGER UNIQUE,


            nickname TEXT,


            avatar TEXT,


            level INTEGER DEFAULT 1,


            xp INTEGER DEFAULT 0,


            games_played INTEGER DEFAULT 0,


            hours_played REAL DEFAULT 0,


            favorite_game TEXT,



            FOREIGN KEY(user_id)

            REFERENCES users(id)


        )

        """

        )



        self.db.connection.commit()
        
        if __name__ == "__main__":
            Models()

            print(
                "Modelos CANARIS criados com sucesso!"
            )