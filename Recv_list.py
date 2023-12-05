import json
import os
from read_json_file import read_json_file

def get_files_arr(mail_folder, foldername):
    return os.listdir(os.path.join(mail_folder, foldername))[::-1]

def output_receive_list(user_folder, foldername):
    mail_folder = os.path.join(user_folder, "mailbox")
    while True:
        files_arr = get_files_arr(mail_folder, foldername)
        if not files_arr:
            print("Thư mục bạn chọn không có email nào!")
            folder = input_folder()
            if folder == '':
                return None
            foldername = ["Inbox", "Project", "Important", "Work", "Spam"][int(folder) - 1]
        else:
            break
    listjson = read_json_file(os.path.join(user_folder, 'email_infor.json'))
    for i in range(len(files_arr)):
        print(i + 1, end='. ')
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
            choice_str = input("Bạn muốn đọc Email thứ mấy (nhập 0 để xem lại toàn bộ, nhấn Enter để thoát): ")
            if choice_str == '':
                return None
            choice = int(choice_str)
            if 0 <= choice <= len(files_arr):
                return choice
            else:
                print("Vui lòng chọn lại hoặc nhập 0 để xem lại toàn bộ.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

def read_chosen_file(folder_path, choice):
    # files_arr = get_files_arr(folder_path)
    files_arr = os.listdir(folder_path)[::-1]
    file_path = os.path.join(folder_path, files_arr[choice-1])
    with open(file_path) as msgfile:
        return msgfile.read()


def update_status(user_folder, folder_path, choice):
    files_arr = os.listdir(folder_path)[::-1]
    if 1 <= int(choice) <= len(files_arr):
        selected_email_file = files_arr[int(choice) - 1]
        listjson = read_json_file(os.path.join(user_folder, 'email_infor.json'))
        for i in range(len(listjson)):
            if listjson[i]["Filename"] == selected_email_file:
                try:
                    with open(os.path.join(user_folder, 'email_infor.json'), 'r') as fileread:
                        list = json.load(fileread)
                except FileNotFoundError:
                    print ("Khong the mo file!")
                list[i]["Status"] = 1
                try:
                    with open(os.path.join(user_folder, 'email_infor.json'), 'w') as filewrite:
                        json.dump(list,filewrite,indent = 2)
                except FileNotFoundError:
                    print ("Khong the mo file!")
def input_folder():
    while True:
        folder = input("Bạn muốn xem email trong folder nào (nhấn Enter để thoát): ")
        try:
            if ('1' <= folder <= '5'):
                return folder
            elif folder == '':
                return folder
            else:
                print("Vui lòng nhập từ 1 -> 5!")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")
