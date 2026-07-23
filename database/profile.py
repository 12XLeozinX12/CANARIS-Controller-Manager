from database.database import Database




class GamerProfile:



    def __init__(self):

        self.db = Database()



    # ==================================
    # CRIAR PERFIL
    # ==================================

    def create_profile(

        self,

        user_id,

        nickname

    ):


        try:


            self.db.cursor.execute(

            """

            INSERT INTO gamer_profile

            (

                user_id,

                nickname

            )

            VALUES

            (

                ?,

                ?

            )

            """,

            (

                user_id,

                nickname

            )

            )


            self.db.connection.commit()



            return True



        except Exception as erro:


            print(
                erro
            )


            return False



    # ==================================
    # BUSCAR PERFIL
    # ==================================

    def get_profile(

        self,

        user_id

    ):


        self.db.cursor.execute(

        """

        SELECT *

        FROM gamer_profile

        WHERE user_id=?

        """,

        (

            user_id,

        )

        )


        perfil = self.db.cursor.fetchone()



        if perfil:


            return {


                "id":perfil[0],

                "user_id":perfil[1],

                "nickname":perfil[2],

                "avatar":perfil[3],

                "level":perfil[4],

                "xp":perfil[5],

                "games":perfil[6],

                "hours":perfil[7],

                "favorite":perfil[8]

            }



        return None