import os
import sys
import pathlib
from url_getters import *

def print_options(urls):
    print "\n\n0 : All"
    i = 1
    for url in urls:
#        print url.rsplit('/')
        print str(i) + " : " + url.rsplit('/')[-2]
        i += 1
    return

#main function

#Genres

if (len(sys.argv) == 2):
    path = pathlib.Path(sys.argv[1])
else:
    abspath = os.path.abspath(__file__)
    path = os.path.dirname(abspath)

print path

genres = get_genres()
print_options(genres)

print "\nSelect a genre from the list above."
print "(Enter number 0 - " + str(len(genres)) + ") :"
x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print "Sorry, not a number."
        exit()


#Programs
if (x > 0) and (x < len(genres)+1):
    genre = genres[x-1]
    programs = get_programs(genre)
else:
    exit()

print_options(programs)
print "\nSelect a program from the list above."
print "(Enter number 0 - " + str(len(programs)) + ") :"
x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print "Sorry, not a number."
        exit()


#Shows
if (x > 0) and (x < len(programs)+1):
    program = programs[x-1]
    shows = get_shows(program)
else:
    exit()

print_options(shows)
print "\nSelect a show date from the list above."
print "(Enter number 0 - " + str(len(shows)) + ") :"
path = str(pathlib.Path(str(path) + "/" + genre.rsplit('/')[-2] + "/" + program.rsplit("/")[-2]))
print path

x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print "Sorry, not a number."
        exit()


#Info
if (x > 0) and (x < len(shows)+1):
    info = get_info(shows[x-1], program)
    download(info[1], path, info[0], shows[x-1])
elif (x == 0):
    for show in shows:
        info = get_info(show, program)
        download(info[1], path, info[0], show)
else:
    exit()
