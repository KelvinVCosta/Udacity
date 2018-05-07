import psycopg2 as pg2

from param import conn_string

class Connector():
    """docstring for ."""
    def __init__(self):
        print "\nConnecting to the database..."
        self.conn = pg2.connect(conn_string)

    def execute(self, query):
        print "\nGetting cursor..."
        cursor = self.conn.cursor()
        cursor.execute(query)
        entries = cursor.fetchall()
        print "\nClosing cursor..."
        cursor.close()
        return entries

    def __del__(self):
        print "\nClosing connector..."
        self.conn.close()

# queries = ['SELECT name FROM authors;',
#     'SELECT title FROM articles;']
# conn = Connector()
# conn.execute(queries[0])

# def connector(query):
#     conn_string = "dbname='news' user='vagrant' password='vagrant'"
#     print "Connecting to the database..."
#     connector = pg2.connect(conn_string)
#     print "Getting cursor..."
#     cursor = connector.cursor()
#     print "Connected..."
#
#     # for query in queries:
#     cursor.execute(query)
#     entries = cursor.fetchall()
#
#     print "Closing cursor..."
#     cursor.close()
#
#     print "Closing connector..."
#     connector.close()
#
#     print "Closed..."
#     return entries
