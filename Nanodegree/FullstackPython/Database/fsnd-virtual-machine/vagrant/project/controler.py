import sys
import psycopg2 as psg2
from param import CONN_STRING


class Connector:

    def __init__(self):
        print "\nConnecting to database..."
        try:
            self.conn = psg2.connect(CONN_STRING)
        except psg2.Error as ex:
            print "Something is wrong.... Unable to connect to the database...."
            print ex.pgerror
            print ex.diag.message_detail
            sys.exit(1)

    def execute(self, query):
        print "\nGetting cursor..."
        cursor = self.conn.cursor()
        cursor.execute(query)
        entries = cursor.fetchall()
        print "\nClosing cursor..."
        cursor.close()
        return entries

    def __del__(self):
        print "All done...."
        print "Disconnecting from the database.... "
        self.conn.close()
