import json
def read_json_file():
    with open('Email_Infor.json', 'r') as filejson:
        listdata = json.loads(filejson.read())
    return listdata
#thiecs
