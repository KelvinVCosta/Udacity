import psycopg2 as psg2
from param import CONN_STRING


class Connector:

    def __init__(self):
        print "\nConnecting to database..."
        self.conn = psg2.connect(CONN_STRING)

    def execute(self, query):
        print "\nGetting cursor..."
        cursor = self.conn.cursor()
        cursor.execute(query)
        entries = cursor.fetchall()
        print "\nClosing cursor..."
        cursor.close()
        return entries

    def __del__(self):
        print "Disconnecting from the database.... " \
              "\n See ya!"
        self.conn.close()


# queries = ['SELECT name FROM authors;',
#            'SELECT title FROM articles;']
# conn = Connector()
# entries = conn.execute(queries[0])
# for entry in entries:
#     for data in entry:
#         res = ''.join(data)
#         print " " + res + " "
