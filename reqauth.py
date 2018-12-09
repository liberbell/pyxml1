import requests

def main():
    url ='http://httpbin.org/basic-auth/JoeMarini/MySecretWord'

    printResults(result)

def printResults(resData):
    print('Resutl code: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data: ----------------')
    print(resData.tesxt)

    print('')
