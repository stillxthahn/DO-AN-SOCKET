from readjson import read_Filejson

listjson = read_Filejson()
print(listjson)
for i in range(len(listjson)):
    print(i+1, end=' ')
    if listjson[i]["status"] != 1:
        print("(chua doc)", end = ' ')
        print (listjson[i]["from"], end =", ")
        print (listjson[i]["subject"])
    else:
        print (listjson[i]["from"], end =", ")
        print (listjson[i]["subject"])

