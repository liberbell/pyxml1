import requests
from requests.auth import HTTPBasicAuth

def main():
    url ='http://httpbin.org/basic-auth/JoeMarini/MySecretWord'
    myCreds = HTTPBasicAuth('JoeMarini', 'MySecretWord')

    printResults(result)

def printResults(resData):
    print('Resutl code: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data: ----------------')
    print(resData.tesxt)

    print('')
