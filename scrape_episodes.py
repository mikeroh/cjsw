import os
import sys
import pathlib
from url_getters import *
from sys import stdin

path = pathlib.Path(sys.argv[1])

program = sys.argv[2]
shows = get_shows(program)
path = str(pathlib.Path(str(path) + "/" + program.rsplit("/")[-2]))

print "\n\n0 : All"
print_options(shows)
print "\nSelect a show date from the list above."
print "(Enter number 0 - " + str(len(shows)) + ") :"

try:
    x = int(stdin.readline())
except ValueError:
    print "Sorry, not a number."
    exit()

#Info
if (x > 0) and (x < len(shows)+1):
    info = get_info(shows[x-1], program)
    if(info[0]):
        download(info[2], path, info[1], shows[x-1])
elif (x == 0):
    for show in shows:
        info = get_info(show, program)
        if(info[0]):
            download(info[2], path, info[1], show)
else:
    exit()
