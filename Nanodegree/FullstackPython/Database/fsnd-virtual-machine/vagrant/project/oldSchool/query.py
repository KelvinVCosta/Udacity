import sys
import conn

def query(option):
    queries = [
        'SELECT name FROM authors;',
        'SELECT title FROM articles;',
        'SELECT title, name FROM articles, authors WHERE articles.author = authors.id;'
        ]

    entries = conn.connector(queries[option])
    for entry in entries:
        print "\n"
        data = ''.join(entry)
        print "Entry: " + data + " "


query(2)
