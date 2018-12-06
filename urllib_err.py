import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError

def main():
    url='http://non-such-server.org'
    # url='http://httpbin.org/status/404'
    # url='http://httpbin.org/html'

    try:
        result = urllib.request.urlopen(url)
        print('Result code: {}'.format(result.status))
        if (result.getcode() == HTTPStatus.OK):
            print(result.read().decode('UTF-8'))
    except HTTPError as err:
        print('Error: {0}'.format(err.code))

if __name__ == '__main__':
    main()
