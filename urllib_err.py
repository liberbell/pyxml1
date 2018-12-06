import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError

def main():
    # url='http://'non-such-server.org'
    url='http://httpbin.org/status/404'
    # url='http://httpbin.org/html'

    result = urllib.request.urlopen(url)
    print('Result code: {}'.format(result.status))
    if (result.getcode() == HTTPStatus.OK):
        print(result.read().decode('UTF-8'))

if __name__ == '__main__':
    main()
