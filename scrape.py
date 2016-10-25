import os
import sys
import pathlib
from url_getters import *
from sys import stdin

global genre
global program

def episode_selection(episodes, get_latest):
    global genre
    global program

    episode_path = str(pathlib.Path(str(path) + "/" + genre.rsplit('/')[-2] + "/" + program.rsplit("/")[-2]))

    if (not get_latest):
        print "\n\n0 : All"
        print_options(episodes)
        print "\nSelect a episode date from the list above."
        print "(Enter number 0 - " + str(len(episodes)) + ") :"

        try:
            x = int(stdin.readline())
        except ValueError:
            print "Sorry, not a number."
            exit()
    else:
        #Get the most recent episode.
        x = len(episodes)
        if (x == 0):
            exit()

    #Get a single episode
    if (x > 0) and (x < len(episodes)+1):
        info = get_info(episodes[x-1], program)
        if(info[0]):
            download(info[2], episode_path, info[1], episodes[x-1])

    elif (x == 0):
        #Get all of the episodes, if zero was selected.
        for episode in episodes:
            info = get_info(episode, program)
            if(info[0]):
                download(info[2], episode_path, info[1], episode)
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

    #Retrieve and list the episodes
    if (x > 0) and (x < len(programs)+1):
        program = programs[x-1]
        episodes = get_episodes(program)
        episode_selection(episodes, False)
    elif (x == 0):
        #Get the most recent episode of every program.
        for program in programs:
            episodes = get_episodes(program)
            episode_selection(episodes, True)
    else:
        exit()

def genre_selection(user_genre):
    global genre
    #Retrieve and list the genres
    genres = get_genres()
    genre = -1

    if(user_genre == ""):
        print_options(genres)
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
