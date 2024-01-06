import json
import sys

import clipboard

SAVED_DATA = "test.json"

def saveFile(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f,)
        print()

def loadItems(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadItems(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        saveFile(SAVED_DATA, data)
        print('Data Saved!!')

    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clip board')

        else:
            print('Key does not exist')

    elif command == 'list':
        print(data)

    else:
        print("Unknown Command!!")

else:
    print('Please pass exactly one command')
