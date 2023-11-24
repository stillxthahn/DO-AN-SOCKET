from read_json_file import read_json_file
import json
import os
def output_receive_list(foldername):
    listjson = read_json_file('Email_Infor.json')
    folder_path = os.path.join(os.getcwd(),"local_mailbox", foldername)
    files_arr = os.listdir(folder_path)
    files_arr.reverse()
    for i in range(len(files_arr)):
        print(i+1, end=' ')
        for j in range(len(listjson)):
            if listjson[j]["Filename"] == files_arr[i]:
                if listjson[j]["Status"] == '0':
                    print("(chua doc)", end = ' ')
                print (listjson[j]["From"], end =", ")
                print (listjson[j]["Subject"])
def read_chosen_file(foldername, choice):
    folder_path = os.path.join(os.getcwd(),"local_mailbox", foldername)
    files_arr = os.listdir(folder_path)
    files_arr.reverse()
    file_path = os.path.join(folder_path, files_arr[int (choice) -1])
    with open(file_path) as msgfile:
        readfile = msgfile.read()
        print ("Nội dung của email thứ {choice}: " , readfile)


def update_status(listjson, choice):
    if 1 <= int(choice) <= len(listjson):
        selected_email = listjson[int(choice) - 1]
        selected_email["Status"] = 1
        return True
    else:
        return False

    # Lưu lại dữ liệu vào tệp JSON
def update_read(listjson):
    with open('Email_Infor.json', 'w') as file:
        json.dump(listjson, file, indent=2)
