from lxml import html
import requests

page = requests.get('http://cjsw.com/browse')
tree = html.fromstring(page.content)


#This will create a list of links:
links = tree.xpath('//a/@href')
genre_links = []

for url in links:
    if url.find("http://cjsw.com/genre/") != -1:
        genre_links.append(url)


print 'Genre Links: ', genre_links
