from model import Composer


class View:

    def __init__(self):
        self.query = Composer()
        self.menu()

    def output(self, option):
        entries = self.query.select(option)
        print "\n"
        for row in entries:
            if option == 0:
                print "Title: " + row[0]
                print str(row[1]) + " views\n"
            elif option == 1:
                print "Author: " + row[0]
                print str(row[1]) + " views\n"
            elif option ==2:
                print "Date: " + str(row[0])
                print "Percentage: " + str(row[1])
                print "Error logs: " + str(row[2])
                print "Logs: " + str(row[3])
                print "\n"
        print "\n"

    def menu(self):

        try:
            option = int(raw_input('''Select an option:
            0 - The 3 most popular articles of all times
            1 - The most popular authors
            2 - Which days have more than 1% of errors logs
            3 - Exit
            Option: '''))

            if option in range(0, 3):
                self.output(option)
                self.menu()
            elif option == 3:
                exit(0)
            else:
                print "Invalid input\n"
                self.menu()
        except ValueError:
            print "Just numbers, please...\n"
            self.menu()

    def __del__(self):
        print "See you soon"

