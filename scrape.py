from url_getters import get_shows
from url_getters import get_genres
from url_getters import get_programs
from url_getters import get_info
import urllib
import sys

global rem_mp3 # global variable to be used in dlProgress

#from http://stackoverflow.com/questions/51212/how-to-write-a-download-progress-indicator-in-python
def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + rem_mp3 + "...%d%%" % percent)
    sys.stdout.flush()
    return

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
    programs = get_programs(genres[x-1])
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
else:
    exit()

date = shows[x-1].rsplit('/')[-1]
date = date[:4] + "-" + date[4:6] + "-" + date[6:]

title = info[0] + ' ' + date +'.mp3'
rem_mp3 = info[1]
print title

#Download
urllib.urlretrieve(rem_mp3, title, reporthook=dlProgress)
