from model import Composer


class View:

    def __init__(self):
        self.query = Composer()

    def output(self, option):
        entries = self.query.select(option)
        print "\n"
        for entry in entries:
            for data in entry:
                print " " + str(data) + " "
        print "\n"

    # def menu(self):
    #         option = raw_input('''Select an option:\n
    #         1 - The 3 most popular articles \n
    #         2 - The most popular authors of all times \n
    #         3 - Which have more than 1'%' of errors
    #         0 - Exit''')

    def __del__(self):
        print "See you soon"


opt = 0
show = View()
# Pick from 0 to 2
print "Option: " + str(opt)
show.output(opt)
