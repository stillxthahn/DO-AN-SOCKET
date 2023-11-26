import json
import os
from read_json_file import read_json_file

def getFiles_arr(foldername):
    return os.listdir(os.path.join(os.getcwd(), "local_mailbox", foldername))[::-1]

def output_receive_list(foldername):
    while True:
        files_arr = getFiles_arr(foldername)
        if not files_arr:
            print("Thư mục bạn chọn không có email nào!")
            foldername = folder_choice(0)
        else:
            break
    listjson = read_json_file('Email_Infor.json')
    for i in range(len(files_arr)):
        print(i + 1, end=' ')
        for j in range(len(listjson)):
            if listjson[j]["Filename"] == files_arr[i]:
                if listjson[j]["Status"] == '0':
                    print("(chua doc)", end=' ')
                print(listjson[j]["From"], end=", ")
                print(listjson[j]["Subject"])

    return foldername

def get_valid_choice(files_arr):
    while True:
        try:
            choice = int(input("Bạn muốn đọc Email thứ mấy: "))
            if 1 <= choice <= len(files_arr):
                return choice
            else:
                print(f"Vui lòng chọn lại ")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")



def read_chosen_file(foldername, choice):
    folder_path = os.path.join(os.getcwd(), "local_mailbox", foldername)
    files_arr = getFiles_arr(foldername)
    file_path = os.path.join(folder_path, files_arr[choice-1])

    with open(file_path) as msgfile:
        return msgfile.read()


def update_status(foldername, choice):
    files_arr = getFiles_arr(foldername)
    if 1 <= int(choice) <= len(files_arr):
        selected_email_file = files_arr[int(choice) - 1]
        listjson = read_json_file('Email_Infor.json')
        for i in range(len(listjson)):
            if listjson[i]["Filename"] == selected_email_file:
                try:
                    with open("Email_Infor.json", 'r') as fileread:
                        list = json.load(fileread)
                except FileNotFoundError:
                    print ("Khong the mo file!")
                list[i]["Status"] = 1
                try:
                    with open('Email_Infor.json', 'w') as filewrite:
                        json.dump(list,filewrite,indent = 2)
                except FileNotFoundError:
                    print ("Khong the mo file!")
def folder_choice(folder):
    while not (1 <= folder <= 5):
        try:
            folder = int(input("Bạn muốn xem email trong folder nào: "))
            if not (1 <= folder <= 5):
                print("Vui lòng chọn từ 1 đến 5.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    return ["Inbox", "Project", "Important", "Work", "Spam"][folder - 1]
