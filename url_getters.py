from lxml import html
import requests

def get_genres():
    page = requests.get('http://cjsw.com/browse')
    tree = html.fromstring(page.content)


    #This will create a list of links:
    links = tree.xpath('//a/@href')
    genre_links = []

    for url in links:
        if url.find("http://cjsw.com/genre/") != -1:
            genre_links.append(url)

    genre_links = set(genre_links)
    for url in genre_links:
        print url

    return

def get_programs(genre):
    page = requests.get(genre)
    tree = html.fromstring(page.content)


    #This will create a list of links:
    links = tree.xpath('//a/@href')
    program_links = []

    for url in links:
        if url.find("http://cjsw.com/program/") != -1:
            program_links.append(url)

    program_links = set(program_links)
    for url in program_links:
        print url

    return

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
            show_links.append(root + url)

    show_links = set(show_links)
    for url in show_links:
        print url

    return
