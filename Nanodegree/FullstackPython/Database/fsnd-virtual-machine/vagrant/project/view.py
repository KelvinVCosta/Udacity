from model import Composer


class View:

    def __init__(self):
        self.query = Composer()
        self.menu()

    def output(self, option):
        entries = self.query.select(option)
        print "\n"
        for row in entries:
            for data in row:
                print data
        print "\n"

    def menu(self):
            option = raw_input('''Select an option:
            0 - The 3 most popular articles
            1 - The most popular authors of all times
            2 - Which logs have more than 1% of errors
            Option: ''')
            self.output(int(option))

    def __del__(self):
        print "See you soon"

