import socket
import uuid
import time
def sendEmail(username, emailFrom, host, port):
  #CREATE SOCKET OBJECT AND CONNECT TO SERVER
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  client.connect(server_address)

  #SERVER RESPONSE AFTER CONNECTION
  recv = client.recv(1024)
  recv = recv.decode()

  #EHLO COMMAND
  heloCommand = 'EHLO [' + host + ']\r\n'
  client.send(heloCommand.encode())
  recv1 = client.recv(1024)
  recv1 = recv1.decode()

  #MAIL FROM
  mailFrom = f"MAIL FROM:<{emailFrom}>\r\n"
  client.send(mailFrom.encode())
  recv2 = client.recv(1024)
  recv2 = recv2.decode()

  #INPUT DATA
  #INPUT RECEIVE EMAILS
  print("Đây là thông tin soạn email: (nếu không điền vui lòng nhấn enter để bỏ qua)")
  to_list_str = input("To: ")
  tos_list = to_list_str.split(", ")
  # tra ra 1 mang gom cac email -> lap qua cac email
  cc_list_str = input("CC: ")
  ccs_list = cc_list_str.split(", ")
  bcc_list_str = input("BCC: ")
  bccs_list = bcc_list_str.split(", ")

  for to in tos_list:
    rcptTo = f"RCPT TO:{to}\r\n"
    client.send(rcptTo.encode())
    recv3 = client.recv(1024)
    recv3 = recv3.decode()
  #for ccs in ccs_list:
  #for bccs in bccs_list:

  #INPUT SUBJECT AND CONTENT
  subject = input("Subject: ")
  content = input("Content: ")

  #INPUT FILES ATTACHED
  while True:
    attachFiles = input("Có gửi kèm file (1. có, 2. không): ")
    if (attachFiles == "1"):
      numberofFiles = input("Số lượng file muốn gửi: ")
      #for statement
      break
    elif (attachFiles == "2"): break;
    else: print("Lựa chọn không hợp lệ, bạn hãy nhập lại")

  #DATA
  dataSend = 'DATA' + '\r\n'
  client.send(dataSend.encode())
  recv4 = client.recv(1024)
  recv4 = recv4.decode()
  #print("Message after RCPT TO command:" + recv4)

  # INPUTING DATA
  unique_id = uuid.uuid4()
  named_tuple = time.localtime()
  local_time = time.strftime("%a, %d %b %Y %H:%M:%S", named_tuple)

  MessageID = f"Message ID: {unique_id}@example.com\r\n"
  Date = f"Date: {local_time} +0700\r\n\r\n"
  To = f"To: {to_list_str}\r\n"
  From = f"From: {username} <{emailFrom}>\r\n"
  Subject = f"Subject: {subject}\r\n\r\n"
  Content = f"{content}\r\n"
  endMSG = ".\r\n"

  Message = MessageID + Date + To + From + Subject + Content + endMSG
  client.send(Message.encode())
  # client.send(MessageID.encode())
  # client.send(Date.encode())
  # client.send(To.encode())
  # client.send(From.encode())
  # client.send(Subject.encode())
  # client.send(Content.encode())
  # client.send(endMSG.encode())

  recv5 = client.recv(1024)
  recv5 = recv5.decode()
  print("Đã gửi email thành công")
  client.close()
