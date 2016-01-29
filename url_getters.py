import os
from lxml import html
import requests
import pathlib
import urllib
import sys
from ID3 import *


global rem_mp3 # global variable to be used in dlProgress

def get_genres():
    page = requests.get('http://cjsw.com/browse')
    tree = html.fromstring(page.content)


    #This will create a list of links:
    links = tree.xpath('//a/@href')
    genre_links = []

    for url in links:
        if url.find("http://cjsw.com/genre/") != -1:
            genre_links.append(url)

    return list(set(genre_links))


def get_programs(genre):
    page = requests.get(genre)
    tree = html.fromstring(page.content)


    #This will create a list of links:
    links = tree.xpath('//a/@href')
    program_links = []

    for url in links:
        if url.find("http://cjsw.com/program/") != -1:
            program_links.append(url)

    return list(set(program_links))

def get_shows(program):
    root = 'http://cjsw.com'
    program = program[15:]

    page = requests.get(root+program)
    tree = html.fromstring(page.content)


    #This will create a list of links:
    links = tree.xpath('//a/@href')
    show_links = []

    for url in links:
        if url.find(program + 'episode/') != -1:
            url= url + '/'
            show_links.append(root + url)

    show_links = list(set(show_links))
    show_links.sort()
    return show_links


def get_info(url, program):
    info = []
    page = requests.get(url)
    tree = html.fromstring(page.content)
    namelist = tree.xpath('//a[@href="' + program + '"]/@title')
    if len(namelist):
        name = namelist[0]
    else:
        info.append(0)
        return info

    mp3list = tree.xpath('//button/@data-audio-src')
    if len(mp3list):
        mp3 = mp3list[0]
    else:
        info.append(0)
        return info

    info.append(1)
    info.append(name)
    info.append(mp3)
    return info

def download(url, path, album, episode_url):
    global rem_mp3
    rem_mp3 = url

    date = episode_url.rsplit('/')[-2]
    date = date[:4] + "-" + date[4:6] + "-" + date[6:]

    title = album + ' ' + date +'.mp3'
    title = str(pathlib.Path(path + "/" + title))

    #Make directory
    if not os.path.exists(os.path.dirname(title)):
        try:
            os.makedirs(os.path.dirname((title)))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #Download
    if not os.path.isfile(title):
        urllib.urlretrieve(rem_mp3, title, reporthook=dlProgress)
        print "\n"
    else:
        print "You already have that one!\n"

    #Add artist and album
    try:
        id3info = ID3(title)
        id3info.artist = "CJSW"
        id3info.album = album
    except InvalidTagError, message:
        print "Invalid ID3 tag:", message

    return


#from http://stackoverflow.com/questions/51212/how-to-write-a-download-progress-indicator-in-python
def dlProgress(count, blockSize, totalSize):
    global rem_mp3
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + rem_mp3 + "...%d%%" % percent)
    sys.stdout.flush()
    return
