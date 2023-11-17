from read_json_file import read_json_file
import json

def return_json():
    listjson = read_json_file('Email_Infor.json')
    return listjson
def output_receive_list(listjson):
    listjson = read_json_file()
    for i in range(len(listjson)):
        print(i+1, end=' ')
        if listjson[i]["status"] != True:
            print("(chua doc)", end = ' ')
            print (listjson[i]["from"], end =", ")
            print (listjson[i]["subject"])
        else:
            print (listjson[i]["from"], end =", ")
            print (listjson[i]["subject"])
def update_status(listjson, choice):
    if 1 <= int(choice) <= len(listjson):
        selected_email = listjson[int(choice) - 1]
        selected_email["status"] = 1
        return True
    else:
        return False

    # Lưu lại dữ liệu vào tệp JSON
def update_read(listjson):
    with open('Email_Infor.json', 'w') as file:
        json.dump(listjson, file, indent=2)
