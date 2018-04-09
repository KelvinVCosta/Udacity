import sys
sys.path.append('model')
import composer


class View():

    def __init__(self):
        self.query = composer

    def output(self, option):
        entries = self.query.select(option)
        for entry in entries:
            print "\nEntry: "
            for data in entry:
                res = ''.join(data)
                print " " + res + " "

    def menu(self):
            option = raw_input('''Select an option:\n
            1 - The 3 most popular articles \n
            2 - The most popular authors of all times \n
            3 - Which have more than 1'%' of errors
            0 - Exit''')

    def __del__(self):
        print "See you soon"

# show = View()
# show.output(2)
