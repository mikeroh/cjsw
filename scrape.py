from url_getters import get_shows
from url_getters import get_genres
from url_getters import get_programs
from url_getters import get_info

genres = get_genres()

print "0 : All"
i = 1
for url in genres:
    print str(i) + " : " + url[22:-1]
    i += 1

print "\nSelect a genre from the list above."
print "(Enter number 0 - " + str(len(genres)) + ") :"
x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print "Sorry, not a number."
        exit()

if (x > 0) and (x < len(genres)):
    programs = get_programs(genres[x-1])
else:
    exit()

print "\n\n0 : All"
i = 1
for url in programs:
    print str(i) + " : " + url[24:-1]
    i += 1

print "\nSelect a program from the list above."
print "(Enter number 0 - " + str(len(programs)) + ") :"
x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print "Sorry, not a number."
        exit()

if (x > 0) and (x < len(programs)):
    program = programs[x-1]
    shows = get_shows(program)
else:
    exit()

print "\n\n0 : All"
i = 1
for url in shows:
    print str(i) + " : " + url[-8:-4] + "-" + url[-4:-2] + "-" + url[-2:]
    i += 1

print "\nSelect a show date from the list above."
print "(Enter number 0 - " + str(len(shows)) + ") :"
x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print "Sorry, not a number."
        exit()

if (x > 0) and (x < len(shows)):
    info = []
    info = get_info(shows[x-1], program)
else:
    exit()
