import json
from json import JSONDecodeError

def main():
    jsonStr = '''{
        "sandwitch": "Reuben",
        "toasted": true,
        "toppings": [
            "Thousand Island Dressing",
            "SauerKraut",
            "Pickles"
        ],
        "price": 8.99
    }'''

    try:
        data = json.loads(jsonStr)
    except JSONDecodeError as err:
        print('Wooops, JSON decoded error')
        print(err.msg)
        print(err.lineno, err.colno)

    print('sandwitch: ' + data['sandwitch'])
    if (data['toasted']):
        print('And it`s toasted!')

    for topping in data['toppings']:
        print('Topping: ' + topping)

if __name__ == '__main__':
    main()
