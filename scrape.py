import os
import sys
import pathlib
from url_getters import *
from sys import stdin

global genre
global program

def show_selection(shows, get_latest):
    global genre
    global program

    print path
    print genre
    print program
    show_path = str(pathlib.Path(str(path) + "/" + genre.rsplit('/')[-2] + "/" + program.rsplit("/")[-2]))

    if (not get_latest):
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
        #Get the most recent show.
        x = len(shows)
        if (x == 0):
            exit()

    #Get a single show
    if (x > 0) and (x < len(shows)+1):
        info = get_info(shows[x-1], program)
        if(info[0]):
            download(info[2], show_path, info[1], shows[x-1])

    elif (x == 0):
        #Get all of the shows, if zero was selected.
        for show in shows:
            info = get_info(show, program)
            if(info[0]):
                download(info[2], show_path, info[1], show)
    else:
        exit()

def program_selection(programs, get_latest):
    global genre
    global program

    if (not get_latest):
        print "\n\n0 : Update " + genre.rsplit('/')[-2] + " for the week"
        print_options(programs)
        print "\nSelect a program from the list above."
        print "(Enter number 1 - " + str(len(programs)) + ") :"

        try:
            x = int(stdin.readline())
        except ValueError:
            print "Sorry, not a number."
            exit()
    else:
        x=0

    #Retrieve and list the shows
    if (x > 0) and (x < len(programs)+1):
        program = programs[x-1]
        shows = get_shows(program)
        show_selection(shows, False)
    elif (x == 0):
        #Get the most recent episode of every program.
        for program in programs:
            shows = get_shows(program)
            show_selection(shows, True)
    else:
        exit()

def genre_selection(user_genre):
    global genre
    #Retrieve and list the genres
    genres = get_genres()
    genre = -1
    print_options(genres)

    if(user_genre == ""):
        print "\nSelect a genre from the list above."
        print "(Enter number 1 - " + str(len(genres)) + ") :"
        try:
            x = int(stdin.readline())
        except ValueError:
            print "Sorry, not a number."
            exit()

        if (x > 0) and (x < len(genres)+1):
            genre = genres[x-1]
            programs = get_programs(genre)
            program_selection(programs, False)
            return
        else:
            exit()

    else:
        #Search the list for the one the user asked for.
        for item in genres:
            if(item.find(user_genre) != -1):
                genre = item
                break

    if(genre == -1):
        print "Sorry, " + user_genre + " was not found in the list."
        exit()
    else:
        print genre
        programs = get_programs(genre)
        program_selection(programs, True)


#main function

#Determine the destination path
if (len(sys.argv) >= 2):
    path = pathlib.Path(sys.argv[1])
else:
    abspath = os.path.abspath(__file__)
    path = os.path.dirname(abspath)

#Download the latest of a genre for the week if the user has selected one.
if (len(sys.argv) >= 3):
    user_genre = sys.argv[2]
else:
    user_genre = ""

genre_selection(user_genre)
