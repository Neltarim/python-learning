import mysql.connector
from getpass import getpass
from os import system as sc

user_name   =   "neltarim"
host_adress =   "localhost"
pwd         =   "usertest"#getpass("database password :")
db          =   "test"


###################################################################################
def basic():
    conn = mysql.connector.connect(host=host_adress, user=user_name, password=pwd, database=db)
    cursor = conn.cursor()

    ### here you can do your shit to the db

    conn.close()
###################################################################################


def connectdb():
    print("Connection ...")
    conn = mysql.connector.connect(host=host_adress, user=user_name, password=pwd, database=db)
    return conn

def tablecreate():
    
    conn = connectdb()
    cursor = conn.cursor()
    print("Creating table \"visiteurs\" in " + db)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS visiteurs (
        id int(5) NOT NULL AUTO_INCREMENT,
        name varchar(50) DEFAULT NULL,
        age INTEGER DEFAULT NULL,
        PRIMARY KEY(id)
    );
    """)

    conn.close()
    print("table \"visiteurs\" created.")

def insertdata():
    print("Data insertion ...")
    visiteurs = [
        {"name": "brigitte", "age": "98"},
        {"name": "francois", "age": "56"},
        {"name": "kevin", "age": "12"},
        {"name": "alex", "age": "22"},
        {"name": "karin", "age": "27"}
    ]

    conn = connectdb()
    cursor = conn.cursor()

    for visiteur in visiteurs:
        print("Trying to insert ", visiteur)
        cursor.execute("INSERT INTO visiteurs (name, age) VALUES (%(name)s, %(age)s)", visiteur)

    conn.commit()
    conn.close()

    print("Data added.")

def getdata():
    conn = connectdb()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age FROM visiteurs")
    rows = cursor.fetchall()
    data = []
    print("data :")
    
    for row in rows:
        data.append(row)
        print(row)

    conn.close()

    data_formmatted = []
    for row in data:
        el = {"id": row[0], "name": row[1], "age": row[2]}
        data_formmatted.append(el)

    return data_formmatted

def dumpdb():
    sc("mysqldump -u {} -p --opt {} > {}-backup.sql".format(user_name, db, db))

def dumptable(table):
    sc("mysqldump -u {} -p --opt {} > {}_{}-backup.sql".format(user_name, table, table, db))

def emptytable(table):
    conn = connectdb()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM {};".format(table))
    conn.commit()
    conn.close()
    print(table + " deleted.")

def update():
    conn = connectdb()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE visiteurs
    SET name='kevin', age='17'
    WHERE id=16;
    """)
    conn.commit()
    conn.close()

def istable(table):
    conn = connectdb()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES LIKE \'" + table + "\'")
    row = cursor.fetchall()

    print(row)
    return True

def isempty(table):
    conn = connectdb()
    cursor = conn.cursor()

    cursor.execute("SELECT EXISTS (SELECT 1 FROM {})".format(table))
    row = cursor.fetchall()
    print(row[0][0])

emptytable("visiteurs")
isempty("visiteurs")