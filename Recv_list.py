from readjson import read_Filejson

def output_receive_list():
    listjson = read_Filejson()
    for i in range(len(listjson)):
        print(i+1, end=' ')
        if listjson[i]["status"] != 1:
            print("(chua doc)", end = ' ')
            print (listjson[i]["from"], end =", ")
            print (listjson[i]["subject"])
        else:
            print (listjson[i]["from"], end =", ")
            print (listjson[i]["subject"])
