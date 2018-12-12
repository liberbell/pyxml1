import requests
import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    def startElement(self, tagName, attrs):
        if tagName == 'slideshow':
            print('slideshow title: ' + attrs['title'])
        elif tagName == 'slide':
            self.slideCount += 1
        elif tagName == 'item':
            self.itemCount += 1

    def startDocument(self):
        print('About to start!')

    def endDocument(self):
        print('Finishing up!')

def main():
    handler = MyContentHandler()

    url = 'http://httpbin.org/xml'
    result = requests.get(url)
    # print(result.text)

    xml.sax.parseString(result.text, handler)


    print('There are {0} slide elements.'.format(handler.slideCount))
    print('There are {0} item elements.'.format(handler.itemCount))

if __name__ == '__main__':
    main()
