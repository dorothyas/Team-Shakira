import sqlite3

class DB:
    def __init__ (self,db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.make_tables()

    def drop_table(self,tablename):
        self.command = "DROP TABLE "+tablename+";"
        self.values = {'tablename':tablename}
        self.cursor.execute(self.command);
        self.conn.commit()
        print tablename+' Dropped'

    def make_tables(self):
        command = """CREATE TABLE IF NOT EXISTS Users(user_id INT NOT NULL ,
                                                    email TEXT NOT NULL,
                                                    password TEXT NOT NULL,
                                                    name TEXT NOT NULL,
                                                    role TEXT NOT NULL,
                                                    PRIMARY KEY (email) ); """
        self.cursor.execute(command);
        self.conn.commit()

    def execute(self,query,operation = 'INSERT'):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            if operation == 'SELECT':
                return self.cursor.fetchall()
            print('operation passed')
            return True
        except Error as e :
            print(' operation failed {}'.format(error))
            if operation == 'SELECT':
                return []
            return False

####usage

#first create a DB instance
#db = DB('epic_db')
# then send sql query and query type to execute and wait for [] response for selct type
#print db.execute("""  SELECT * FROM Users""",'SELECT')
