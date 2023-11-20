import socket
from listreadEmail import listreadEmail
from load_email_json import load_email_json
from send_email import send_command
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
  print(state)
  state_arr = state.split()
  print(state_arr)

  listCommand = "LIST\r\n"
  list_data =  send_command(client, "LIST\r\n")

  uidl_data = send_command(client, "UIDL\r\n")
  print(uidl_data)
  list = listreadEmail(uidl_data)
  #save_email(client, list)
  #load_email_json(client, list)

  choice = input("Bạn muốn đọc Email thứ mấy: ")
  retrCommand = f"RETR {choice}\r\n"
  client.send(retrCommand.encode())
  data = client.recv(1024)
  data = data.decode()
  print(f"Nội dung email của email thứ {choice}: ", data)
  top = f"TOP {choice} 5\r\n"
  client.send(top.encode())
  topData = client.recv(1024)
  topData = topData.decode()
  print(topData)

  client.close()
