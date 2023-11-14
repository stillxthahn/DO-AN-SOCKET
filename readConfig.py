import json
def readConfig():
  with open('config.json') as f:
    data = json.load(f)
  return data
