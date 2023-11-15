import json
def read_Filejson():
    with open('read.json', 'r') as filejson:
        listdata = json.load(filejson)
    return listdata
