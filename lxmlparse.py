import requests
from lxml import etree

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)

    doc = etree.fromstring(result.content)
    # print(result.text)

    print(doc.tag)
    print(doc.attrib['title'])

    for elem in doc.findall("slide"):
        print(elem.tag)

    newSlide = etree.SubElement(doc, "slide")
    newSlide.text = "This is a new slide"

    slideCount = len(doc.findall("slide"))

if __name__ == '__main__':
    main()
