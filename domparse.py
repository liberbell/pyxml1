import xml.dom.minidom
import requests

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)

    domtree = xml.dom.minidom.parseString(result)
    rootnode = domtree.documentElement

    print('The Root element is {0}'.format(rootnode.nodeName))

if __name__ == '__main__':
    main()
