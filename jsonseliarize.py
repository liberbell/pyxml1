import json

def main():
    pythonData = {
        "sandwitch": "Reuben",
        "toasted": True,
        "toppings": ["Thousand Island Dressing",
                     "SauerKraut",
                     "Pickles"
                     ],
        "price" : 8.99
    }

    jsonStr = json.dumps(pythonData, indent=4)

    print('JSON Data:--------------------')
    print(jsonStr)

if __name__ == '__main__':
    main()
