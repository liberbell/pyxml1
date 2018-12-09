import requests

def main():
    url = 'http://httpbin.org/status/404'
    result = requests.get(url)
