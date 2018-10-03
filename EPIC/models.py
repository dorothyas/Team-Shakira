import db

def login(email, password):
    query = "SELECT * FROM users WHERE email = {} and {};".format(email, password)
    data = db.execute(query, 'SELECT')
    return data