import pickle
import mysql.connector

USER_NAME   =   "neltarim"
HOST_ADRESS =   "localhost"
PWD         =   "usertest"
DB_NAME     =   "purbeurredb"
COUNTRY     =   "France"

CONN = mysql.connector.connect(host=HOST_ADRESS, user=USER_NAME, password=PWD, database=DB_NAME)

class rel_test():

    def __init__(self):
        self.cursor = CONN.cursor()

    def rel_to_cat()