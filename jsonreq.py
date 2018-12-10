import requests
import json

def main():
    url = 'http://httpbin.org/json'
    result = requests.get(url)

    dataobj = result.json()
    print(json.dumps(dataobj, indent=4))

if __name__ == '__main__':
    main()
