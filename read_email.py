import socket
from listreadEmail import listreadEmail
from load_email_json import load_email_json
from send_email import send_command
from get_email import get_email
from Recv_list import output_receive_list
from Recv_list import read_chosen_file
from Recv_list import update_status
from Recv_list import folder_choice
from Recv_list import get_valid_choice
from Recv_list import getFiles_arr
#from save_email import save_email
def read_email(username, password, host, port):
  #CREATE SOCKET OBJECT AND CONNECT TO SERVER
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  try:
    client.connect(server_address)
    client.recv(1024).decode()
  except Exception as e:
     print(f"Lỗi: {e}")
     return

  send_command(client, "CAPA\r\n")
  send_command(client, f"USER {username}\r\n")
  send_command(client, f"PASS {password}\r\n")
  state = send_command(client, "STAT\r\n")

  listCommand = "LIST\r\n"
  list_data =  send_command(client, "LIST\r\n")

  uidl_data = send_command(client, "UIDL\r\n")
  list = listreadEmail(uidl_data)
  get_email(client, list)

  print("Đây là danh sách các folder trong mailbox của bạn: \r\n 1. Inbox \r\n 2. Project\r\n 3. Important \r\n 4. Work \r\n 5. Spam")
  folder = 0
  foldername = folder_choice(folder)
  print(f"Bạn chọn thư mục {foldername}")
  foldername =output_receive_list(foldername)
  files_arr = getFiles_arr(foldername)
  print("len(files_arr): ",len(files_arr))
  choice = get_valid_choice(files_arr)
  email_data = read_chosen_file(foldername, choice)
  print(f"Nội dung của email thứ {choice}: {email_data}")
  update_status(foldername, choice)

  client.close()
