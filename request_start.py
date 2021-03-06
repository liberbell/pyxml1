import requests

def main():
    # url = 'http://httpbin.org/xml'
    # result = requests.get(url)
    # printResults(result)

    url2 = 'http://httpbin.org/post'
    datavalues = {
        'key1': 'value1',
        'key2': 'value2'
    }
    result = requests.post(url2, data=datavalues)
    # printResults(result)

    url3 = 'http://httpbin.org/get'
    headervalues = {
        'User-Agent': 'Joe Marini App / 1.0.0',
    }
    result = requests.get(url3, headers=headervalues)
    printResults(result)


def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers----------------------')
    print(resData.headers)
    print('\n')

    print('Return data:-----------------')
    print(resData.text)



if __name__ == '__main__':
    main()
