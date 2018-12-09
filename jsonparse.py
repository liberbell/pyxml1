import json

def main():
    jsonStr = '''{
        'sandwitch': 'Reuben,
        'toasted': true,
        'toppings': [
            'Thousand Island Dressing',
            'SauerKraut',
            'Pickles'
        ],
        'price': 8.99
    }'''

    data = json.loads(jsonStr)

    print('sandwitch: ' + data['sandwitch'])
    if (data['toasted']):
        print('And it`s toasted!')

    for topping in data['toppings']:
        print('Topping: ' + toppings)

if __name__ == '__main__':
    main()
