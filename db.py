import psycopg2
connection = psycopg2.connect(
    user="ehsan",
    password="180788",
    host="localhost",
    port="5432",
    database="temp"
)


def create_tables():

    commands = (
        """
        CREATE TABLE smartguard2 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            path VARCHAR(255) NOT NULL
        )
        """)
<<<<<<< HEAD
    try:
        cursor.execute(commands)
    finally:
        connection.commit()
    return 1


def insert_query(name, pathh):
    connection = set_conection()
    cursor = connection.cursor()
    abc = "INSERT INTO public.smartguard2( name, path) VALUES('" + \
        name + "','" + pathh + "');"
    cursor.execute(abc)
    connection.commit()
    print("added")
    return 1


def get_all():
    connection = set_conection()
    cursor = connection.cursor()
    cursor.execute("Select * from smartguard2")
    print(cursor.fetchall())

    connection.commit()
    return 1


def get_by_name_date(name, datee):
    connection = set_conection()
    cursor = connection.cursor()
    cursor.execute("Select path from smartguard2 where name ='" +
                   name + "' AND date = '" + datee + "'""")
    abc = cursor.fetchall()
    cursor.execute("Select id from smartguard2 where name ='" +
                   name + "' AND date = '" + datee + "'""")
    cde = cursor.fetchall()
    connection.commit()
    return abc, cde


def get_by_name(name):
    connection = set_conection()
    cursor = connection.cursor()
    path = []
    key = []
    cursor.execute(
        "Select id,path from smartguard2 where name ='" + name + "' order by id desc limit 10""")
    return cursor.fetchall()


def make_list(x):
    l1 = []
    for tup in x:
        l1.append({"uri": tup[1], "key": tup[0]})
    return l1


def drop_table():
    connection = set_conection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS smartguard2;")
    connection.commit()

=======
    return commands
>>>>>>> parent of 1fa71d0... Video saving in seprate thread


cursor = connection.cursor()
commands1 = create_tables()
cursor.execute(commands1)

#cursor.execute("DROP TABLE IF EXISTS smartguard2;")
