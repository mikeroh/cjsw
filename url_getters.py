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
    name = tree.xpath('//a[@href="' + program + '"]/@title')[0]
    mp3 = tree.xpath('//button/@data-audio-src')[0]

    info.append(name)
    info.append(mp3)
    return info
