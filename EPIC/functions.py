import sqlite3, datetime


def login():
    username = input('Username: ')
    password = input('Password: ')
    conn = sqlite3.connect('')
    cursor = conn.cursor()
    cursor.execute("SELECT username, role FROM users WHERE username='{}'".format(username))
    record = cursor.fetchone()
    if not record:
        print('User not registered!')
        exit()
    return record[1], str(datetime.time())


def show_scores(username):
    pass


def logout():
    pass


def select_action():
    pass


def perform_action(action):
    pass


def show_all_scores():
    pass

