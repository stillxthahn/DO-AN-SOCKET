import json
def read_Filejson():
    with open('Email_Infor.json', 'r') as filejson:
        listdata = json.load(filejson)
    return listdata
