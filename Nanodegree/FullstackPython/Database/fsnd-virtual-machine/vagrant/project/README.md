If you are running under vagrant no need to any special configuration
A little explanation of each file:

#controler.py
Responsible for the database connection, query execution returning the query
result

#model.py
Gets all its queries from the queries.py file and runs the select accordingly
to the option selected

#param.py
Holds the constants of the system, normally this file should be ignored by
the VCS

#queries.py
Holds all the queries used by the system

#view.py
Responsible for the output on the screen

#SQL.sql
Have all the queries used to find out the queries to be at queries.py

#README
If you got here, here's a candy for you

        .
      ,i \
    ,' 8b \
  ,;o  `8b \
 ;  Y8. d8  \
-+._ 8: d8. i:
    `:8 `8i `8
      `._Y8  8:  ___
         `'---Yjdp  "8m._
              ,"' _,o9   `m._
              | o8P"   _.8d8P`-._
              :8'   _oodP"   ,dP'`-._
               `: dd8P'   ,odP'  do8'`.
                 `-'   ,o8P'  ,o8P' ,8P`.
                   `._dP'   ddP'  ,8P' ,..
                      "`._ PP'  ,8P' _d8'L..__
                          `"-._88'  .PP,'7 ,8.`-.._
                               ``'"--"'  | d8' :8i `i.
                                         l d8  d8  dP/
                                          \`' J8' `P'
                                           \ ,8F  87
                                           `.88  ,'
                                            `.,-' mh

