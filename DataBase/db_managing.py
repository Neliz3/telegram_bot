import psycopg2
from dependences import host, user_db, user_pass, db_name
import functools
import operator


# Connecting to a DataBase
def db_connect():
    connection = psycopg2.connect(
        host=host,
        user=user_db,
        password=user_pass,
        database=db_name
    )
    connection.autocommit = True
    return connection


# Create a new table
#def new_table():
#    connection = db_connect()
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """CREATE TABLE users(
#            id serial PRIMARY KEY,
#            first_name varchar (40),
#            source_ln varchar (2),
#            target_ln varchar (2),
#            word varchar,
#            user_id integer);"""
#        )
#    print("[INFO] Table created successfully")


# Checking if user is in a database
def exist_user(user_id):
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT user_id from users WHERE user_id = '{user_id}';"""
        )
        result = cursor.fetchall()
        if not result:
            return False
        else:
            return True


# Inserting new user to a table
def add_user(user_name, user_id):
    connection = db_connect()

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, source_ln, target_ln, word, user_id)
            VALUES (%s, %s, %s, %s, %s);""",
            (f'{user_name}', 'ns', 'nt', None, f'{user_id}')
        )
        print("[INFO] Data was successfully inserted")


# Updating source_ln in a table
def update_source(user_id, source_ln):
    connection = db_connect()

    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE users SET source_ln = '{source_ln}'
            WHERE user_id = '{user_id}';"""
        )
        print("[INFO] Source language updated successfully")


# Updating target_ln in a table
def update_target(user_id, target_ln):
    connection = db_connect()

    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE users SET target_ln = '{target_ln}'
            WHERE user_id = '{user_id}';"""
        )
        print("[INFO] Target language updated successfully")


# Updating word in a table
def update_word(user_id, data):
    connection = db_connect()

    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE users SET word = '{data}'
            WHERE user_id = '{user_id}';"""
        )


# Getting data from a table
def get_inf():
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT id, first_name, source_ln, target_ln, word from users;"""
        )
        print(cursor.fetchall())


# Getting count of users
def count_users():
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT count(*) from users;"""
        )
        result = functools.reduce(operator.add, (cursor.fetchall()))
        return result


# Getting names of users
def name_users():
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT first_name from users;"""
        )
        result = functools.reduce(operator.add, (cursor.fetchall()))
        return result


# Getting source_ln from a table
def get_source(user_id):
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT source_ln from users WHERE user_id = '{user_id}';"""
        )
        a = ''.join(cursor.fetchone())
        return a


# Getting target_ln from a table
def get_target(user_id):
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT target_ln from users WHERE user_id = '{user_id}';"""
        )
        a = ''.join(cursor.fetchone())
        return a


# Getting word from a table
def get_word(user_id):
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT word from users WHERE user_id = '{user_id}';"""
        )
        a = ''.join(cursor.fetchone())
        return a


# Deleting a user
def delete_user(user_id):
    connection = db_connect()
    with connection.cursor() as cursor:
        cursor.execute(
                f"""DELETE from users WHERE user_id = '{user_id}';"""
        )
        print("[INFO] User was deleted successfully")
