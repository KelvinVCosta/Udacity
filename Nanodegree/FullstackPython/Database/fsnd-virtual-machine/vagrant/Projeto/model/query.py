import sys
sys.path.append('../controler')
import conn

#TODO: arrumar 2a e 3a query
def query(option):
    queries = ['SELECT name FROM authors;',
        'SELECT title FROM articles;']
        # 'SELECT title, name FROM articles, authors WHERE articles\.author LIKE author\.id;',
        # 'SELECT title, name FROM articles JOIN authors ON articles\.author LIKE author\.id';
        # ]

    entries = conn.connector(queries[option])
    for entry in entries:
        print "\n"
        data = ''.join(entry)
        print "Entry: " + data + " "


query(0)
