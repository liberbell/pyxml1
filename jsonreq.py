import requests
import json

def main():
    url = 'http://httpbin.org/json'
    result = requests.get(url)

if __name__ == '__main__':
    main()
