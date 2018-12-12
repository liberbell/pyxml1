import xml.dom.minidom
import requests

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)

    domtree = xml.dom.minidom.parseString(result)
    rootnode = domtree.documentElement

    print('Root element ')
