from url_getters import get_shows
from url_getters import get_genres
from url_getters import get_programs

shows = get_shows('http://cjsw.com/program/fade-to-bass-2/')

print "0 : All"
i = 1
for url in shows:
    print str(i) + " : " + url
    i += 1


print "\nSelect the show you would like to download from the list above"
print "(Enter number 0 - " + str(len(shows)) + ") :"
