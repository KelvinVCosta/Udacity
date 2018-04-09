#!/usr/bin/python
#coding: utf-8
'''
Objetivo:
    1) Se passaram duas horas desde o ultimo break?
    2) Se sim, reproduza o video
Autor: Kelvin
'''
import time
import webbrowser

total_breaks = 3
break_count = 0

print("Sistema iniciou")
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=tTMi3LyUBws")
    break_count = break_count + 1
print("E agora parou...")
