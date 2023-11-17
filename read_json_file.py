import json
def read_json_file(filename):
    with open(filename, 'r') as f:
        try:
            listdata = json.loads(f.read())
            return listdata
        except Exception as JSONDecodeError:
            return []
