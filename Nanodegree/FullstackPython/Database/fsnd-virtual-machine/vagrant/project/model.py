from controler import Connector
import queries


class Composer:

    def select(self, option):
        print "Selected option: " + str(option)
        connect = Connector()
        query_opt = [queries.SQL_MOST_VIEWS,
                     queries.SQL_AUTHORS_MOST_VIEWS,
                     queries.SQL_ERR_LOG_1_PERC_MORE]
        entries = connect.execute(query_opt[option])
        return entries
