# Quais sao os tres artigos mais populares de todos os tempos?
# Quem sao os autores de artigos mais populares de todos os tempos?
# Em quais dias mais de 1% das requisicoes resultaram em erros?*
import sys
sys.path.append('controler')
from conn import Connector


class Composer():

    def select(self, option):
        connect = Connector()
        queries = ['SELECT name FROM authors;',
            'SELECT title FROM articles;',
            'SELECT title, name FROM articles, authors WHERE (articles.author = authors.id);'
            ]

        entries = connect.execute(queries[option])
        return entries
    # for entry in entries:
    #     print "\nEntry: "
    #     for data in entry:
    #         res = ''.join(data)
    #         print " " + res + " "

    def menu(option):
        switch = {0: articles,
                  1: authors,
                  2: errors,
                  0: sys.exit(0)}
