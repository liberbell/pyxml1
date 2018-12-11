import requests
import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0

    def startDocument(self):
        print('About to start!')

    def endDocument(self):
        print('Finishing up!')

def main():
    handler = MyContentHandler()

    url = 'http://httpbin.org/xml'
    result = requests.get(url)
    print(result.text)

    print('There are {0} slide elements.'.format(handler.slideCount))
    print('There are {0} item elements.'.format(handler.itemCount))

if __name__ == '__main__':
    main()
