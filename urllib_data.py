import urllib.request
import urllib.parse

def main():
    url = 'http://httpbin.org/get'

    args = {
        'name': 'Joe Marini',
        'is_author': True
    }

    data = urllib.parse.urlencode(args)

    result = urllib.request.urlopen(url + '?' + data)

    print('Result code: {0}'.format(result.status))

    print('Headers:----------------------')
    print(result.getheaders())


    print('Return Data:------------------')
    print(result.read().decode('UTF-8'))

if __name__ == '__main__':
    main()
