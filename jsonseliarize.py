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

    jsonStr = json.dumps(pythonData)

    print('JSON Data:--------------------')
    print(jsonStr)
