# Import
import mysql.connector


# Class
class Database:
    def __init__(self):
        # Variables
        self.db_conn: object = None

        self.db_host: str = "127.0.0.1"
        self.db_name: str = "tic_tai_toe"
        self.db_user: str = "root"
        self.db_pass: str = ""

    def connect(self):
        if self.db_conn is None:
            self.db_conn = mysql.connector.connect(
                host=self.db_host,
                user=self.db_user,
                passwd=self.db_pass,
                database=self.db_name
            )
        else:
            print("err:: db already connected")

    def get_Connection(self):
        return self.db_conn

    def get_Cursor(self):
        actual_conn = self.get_Connection()

        return actual_conn.cursor()