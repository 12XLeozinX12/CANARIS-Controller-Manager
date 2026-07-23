from database.database import Database



class UserManager:


    def __init__(self):

        self.db = Database()



    # ==================================
    # CRIAR USUARIO
    # ==================================

    def create_user(

        self,

        username,

        password,

        email=""

    ):


        try:


            self.db.cursor.execute(

                """

                INSERT INTO users

                (

                    username,

                    password,

                    email

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

                    password,

                    email

                )

            )



            self.db.connection.commit()



            return True




        except Exception as erro:

            print("==============================")

            print("ERRO DATABASE USERS")

            print(erro)

            print("==============================")

            return False





    # ==================================
    # LOGIN
    # ==================================

    def login(

        self,

        username,

        password

    ):


        self.db.cursor.execute(

            """

            SELECT *

            FROM users

            WHERE username=?

            AND password=?

            """,

            (

                username,

                password

            )

        )



        usuario = self.db.cursor.fetchone()



        if usuario:


            return {

                "id": usuario[0],

                "username": usuario[1],

                "email": usuario[3],

                "created": usuario[4]

            }



        return None





    # ==================================
    # BUSCAR USUARIO
    # ==================================

    def get_user(

        self,

        username

    ):


        self.db.cursor.execute(

            """

            SELECT *

            FROM users

            WHERE username=?

            """,

            (

                username,

            )

        )



        usuario = self.db.cursor.fetchone()



        if usuario:


            return {

                "id": usuario[0],

                "username": usuario[1],

                "email": usuario[3],

                "created": usuario[4]

            }



        return None





    # ==================================
    # ALTERAR EMAIL
    # ==================================

    def update_email(

        self,

        username,

        email

    ):


        self.db.cursor.execute(

            """

            UPDATE users

            SET email=?

            WHERE username=?

            """,

            (

                email,

                username

            )

        )


        self.db.connection.commit()



    # ==================================
    # DELETAR CONTA
    # ==================================

    def delete_user(

        self,

        username

    ):


        self.db.cursor.execute(

            """

            DELETE FROM users

            WHERE username=?

            """,

            (

                username,

            )

        )


        self.db.connection.commit()