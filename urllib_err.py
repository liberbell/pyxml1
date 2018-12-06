import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError

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
    except URLError as err:
        print('Yeah that server is bunk. {0}'.format(err.reason))

if __name__ == '__main__':
    main()
