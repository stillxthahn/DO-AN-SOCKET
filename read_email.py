import socket
import os
import base64
from send_email import send_command
from get_email import get_email
from recv_list import output_receive_list
from recv_list import read_chosen_file
from recv_list import update_status
from recv_list import input_folder
from recv_list import get_valid_choice
from recv_list import get_files_arr
from get_email import parse_email

def print_list_email(data):
    list = data.split('\r\n')
    list = list[1:]
    list = list[:-2]
    tmp = []
    for i in range(0, len(list)):
        list_no_Space = list[i].split(' ')
        tmp.append(list_no_Space[1])
    return tmp

def get_list_emails(client, email, password):
  send_command(client, "CAPA\r\n")
  send_command(client, f"USER {email}\r\n")
  send_command(client, f"PASS {password}\r\n")
  send_command(client, "STAT\r\n")
  send_command(client, "LIST\r\n")
  uidl_data = send_command(client, "UIDL\r\n")
  list = print_list_email(uidl_data)
  return list

def read_email(email, password, host, port):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  try:
    client.connect(server_address)
    client.recv(1024).decode()
  except Exception as e:
     print(f"Lỗi: {e}")
     return
  
  user_folder = os.path.join(os.getcwd(), "local_mailbox", email)
  mail_folder = os.path.join(os.getcwd(), "local_mailbox", email, "mailbox")
  try:
    os.makedirs(mail_folder)
    os.makedirs(os.path.join(mail_folder, "Inbox"))
    os.makedirs(os.path.join(mail_folder, "Project"))
    os.makedirs(os.path.join(mail_folder, "Work"))
    os.makedirs(os.path.join(mail_folder, "Spam"))
    os.makedirs(os.path.join(mail_folder, "Important"))
  except FileExistsError as e:
    pass
  list = get_list_emails(client, email, password)
  get_email(client, user_folder, list)

  while True:
    print("Đây là danh sách các folder trong mailbox của bạn: \r\n 1. Inbox \r\n 2. Project\r\n 3. Important \r\n 4. Work \r\n 5. Spam")
    folder = input_folder()
    if folder == '':
        return
    foldername = ["Inbox", "Project", "Important", "Work", "Spam"][int(folder) - 1]
    print(f"Bạn chọn thư mục {foldername}")
    foldername = output_receive_list(user_folder, foldername)
    files_arr = get_files_arr(mail_folder, foldername)

    while True:
        choice = get_valid_choice(files_arr)
        if choice is None:
            return
        elif choice == 0:
            break
        else:
            folder_path = os.path.join(mail_folder, foldername)
            email_data = read_chosen_file(folder_path, choice)
            data_email = parse_email(email_data, '\n')
            print(f"Nội dung của email thứ {choice}:")
            print ("Date: ", data_email['Date'])
            print ("To: ", " ".join(data_email['To']))
            if len(data_email["Cc"]) != 0:
                print ("Cc: ", " ".join(data_email['Cc']))
            print ("From: ",data_email['From'])
            print ("Subject: ", data_email['Subject'])
            print ("Content: ", data_email['Content'])
            update_status(user_folder, folder_path, choice)
            try:
                if data_email['Attachment'] != []:
                    opt = input("Trong email này có chứa " + str(len(data_email['Attachment'])) + " attached file, nhập 1 để save, nhập 0 để tiếp tục: ")
                if opt == '1':
                    print("Sau đây là các attached file:")
                    for i in range(len(data_email['Attachment'])):
                        print(str(i + 1) + ".", data_email['Attachment'][i]['name'])
                    if len(data_email['Attachment']) > 1:
                        print(str(len(data_email['Attachment']) + 1) + ". All")
                    saved_file = input("Nhập số tương ứng với file bạn muốn lưu: ")
                    saved_path = input("Cho biết đường dẫn bạn muốn lưu: ")
                    if (int(saved_file) == len(data_email['Attachment']) + 1):
                        for i in range(0, len(data_email["Attachment"])):
                            save_attachment(data_email, i, saved_path)  #i - 1: là index trong data_email['Attachment]
                    else:
                        save_attachment(data_email, int(saved_file) - 1, saved_path)
                client.close()
            except KeyError:
                pass

            #Lưu file attachment
def save_attachment(data_email, saved_file, saved_path):
    try:
        data_file = base64.b64decode(data_email['Attachment'][saved_file]['data'])
        filename = os.path.join(saved_path, data_email['Attachment'][saved_file]['name'])
        file = open(filename, 'wb')
        file.write(data_file)
        print("Lưu attached file", saved_file + 1, "thành công!")
        file.close()
    except Exception as e:
        print(str(e))
