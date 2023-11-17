import json
def read_json_file(filename):
    with open(filename, 'r') as f:
        listdata = json.loads(f.read())
    return listdata
#thiecs
