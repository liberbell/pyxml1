import requests

def main():


def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers----------------------')
    print(resData.headers)
    print('\n')

    print('Return data:-----------------')
    print(resData.content)



if __name__ == '__main__':
    main()
