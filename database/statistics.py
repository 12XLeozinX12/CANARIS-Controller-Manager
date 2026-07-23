from database.database import Database



class GamerStatistics:


    def __init__(self):

        self.db = Database()



    # =====================================
    # CRIAR ESTATÍSTICA
    # =====================================

    def create_statistics(
            self,
            user_id
    ):


        try:


            self.db.cursor.execute(

                """
                INSERT INTO gamer_statistics
                (
                    user_id
                )

                VALUES(?)

                """,

                (
                    user_id,
                )

            )


            self.db.connection.commit()


            return True


        except Exception as erro:


            print(
                "ERRO STATISTICS CREATE:",
                erro
            )


            return False



    # =====================================
    # PEGAR ESTATÍSTICA
    # =====================================

    def get_statistics(
            self,
            user_id
    ):


        self.db.cursor.execute(

            """
            SELECT

            hours_played,
            games_started,
            wins,
            losses,
            achievements,
            last_game


            FROM gamer_statistics


            WHERE user_id=?

            """,

            (
                user_id,
            )

        )


        dados = self.db.cursor.fetchone()



        if dados:


            return {

                "hours_played": dados[0],

                "games_started": dados[1],

                "wins": dados[2],

                "losses": dados[3],

                "achievements": dados[4],

                "last_game": dados[5]

            }



        return None




    # =====================================
    # ATUALIZAR HORAS
    # =====================================


    def add_hours(
            self,
            user_id,
            horas
    ):


        self.db.cursor.execute(

            """
            UPDATE gamer_statistics

            SET hours_played =
            hours_played + ?

            WHERE user_id=?

            """,

            (
                horas,
                user_id
            )

        )


        self.db.connection.commit()




    # =====================================
    # FECHAR
    # =====================================


    def close(self):

        self.db.close()