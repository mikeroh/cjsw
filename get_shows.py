from lxml import html
import requests

root = 'http://cjsw.com'
program = '/program/fade-to-bass-2/'

page = requests.get(root+program)
tree = html.fromstring(page.content)


#This will create a list of links:
links = tree.xpath('//a/@href')
show_links = []

for url in links:
    if url.find(program + 'episode/') != -1:
        show_links.append(url)


print 'Show Links: ', show_links
