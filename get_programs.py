from lxml import html
import requests

page = requests.get('http://cjsw.com/genre/electronic/')
tree = html.fromstring(page.content)


#This will create a list of links:
links = tree.xpath('//a/@href')
program_links = []

for url in links:
    if url.find("http://cjsw.com/program/") != -1:
        program_links.append(url)


print 'Program Links: ', program_links
