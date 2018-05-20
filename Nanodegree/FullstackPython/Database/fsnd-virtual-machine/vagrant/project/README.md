#System explanation
This system's goal is create a report to the requested questions:
* Which are the top 3 articles with most views?
* Who are the authors of these articles?
* Which days have 1% or more of error logs?


#Preparing the terrain
First, download all the files that we will use:
Get the [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip)

Or clone this [repo](https://github.com/udacity/fullstack-nanodegree-vm)

Download and unzip the [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

#Setting up to run
At the command line interface, type:

1) vagrant up
2) vagrant ssh 

These commands will install and start the linux virtual machine 
If all goes fine, you should at a terminal under vagrant@vagrant signture

Copy the newsdata.sql file to the shared directory vagrant 

3) Back to the vm terminal, cd /vagrant

4) psql -d news -f newsdata.sql


With these, you got the virtual machine and the database prepared to run this system


#Starting the system
To start this system, run the main.py file


#Files explanation

####controler.py
Responsible for the database connection, query execution returning the query
result

####model.py
Gets all its queries from the queries.py file and runs the select accordingly
to the option selected

####param.py
Holds the constants of the system, normally this file should be ignored by
the VCS

####queries.py
Holds all the queries used by the system

####view.py
Responsible for the output on the screen

####SQL.sql
Have all the queries used to find out the queries to be at queries.py