import os
import sys
import pathlib
from url_getters import *
from sys import stdin

def show_selection(shows, get_latest):
    show_path = str(pathlib.Path(str(path) + "/" + genre.rsplit('/')[-2] + "/" + program.rsplit("/")[-2]))

    if (!get_latest):
        print "\n\n0 : All"
        print_options(shows)
        print "\nSelect a show date from the list above."
        print "(Enter number 0 - " + str(len(shows)) + ") :"
    try:
        x = int(stdin.readline())
    except ValueError:
        print "Sorry, not a number."
        exit()
    else:
        x = len(shows)

    #Get the single show, or all shows, if zero was selected.
    if (x > 0) and (x < len(shows)+1):
        info = get_info(shows[x-1], program)
        if(info[0]):
            download(info[2], show_path, info[1], shows[x-1])
    elif (x == 0):
        for show in shows:
            info = get_info(show, program)
            if(info[0]):
                download(info[2], show_path, info[1], show)
    else:
        exit()

#main function

#Retrieve and list the genres

if (len(sys.argv) == 2):
    path = pathlib.Path(sys.argv[1])
else:
    abspath = os.path.abspath(__file__)
    path = os.path.dirname(abspath)

genres = get_genres()
print_options(genres)

print "\nSelect a genre from the list above."
print "(Enter number 1 - " + str(len(genres)) + ") :"

try:
    x = int(stdin.readline())
except ValueError:
    print "Sorry, not a number."
    exit()


#Retrieve and list the programs
if (x > 0) and (x < len(genres)+1):
    genre = genres[x-1]
    programs = get_programs(genre)
else:
    exit()

print "\n\n0 : Update " + genre + " for the week"
print_options(programs)
print "\nSelect a program from the list above."
print "(Enter number 1 - " + str(len(programs)) + ") :"

try:
    x = int(stdin.readline())
except ValueError:
    print "Sorry, not a number."
    exit()


#Retrieve and list the shows
if (x > 0) and (x < len(programs)+1):
    program = programs[x-1]
    shows = get_shows(program)
    show_selection(shows, False)
elif (x == 0):
    for program in programs:
        shows = get_shows(program)
        show_selection(shows, True)
else:
    exit()
