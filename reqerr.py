import requests

def main():
    url = 'http://httpbin.org/status/404'
    result = requests.get(url)
    printResults(result)


def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Returned Data:--------------------')
    print(resData.text)
