#!/usr/bin/python
#coding: utf-8
import urllib

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Danger!!!!")
    else:
        print("All good")

read_text()
