import socket
import uuid
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
def send_command(client, command):
  try:
    client.send(command.encode())
    response = client.recv(1024).decode()
    return response
  except Exception as e:
    print(f"Lỗi: {e}")
    return ""

def input_email():
  tos_list = []
  ccs_list = []
  bccs_list = []
  subject = ""
  content = ""
  num_files = 0
  file_path = []
  print("Đây là thông tin soạn email: (nếu không điền vui lòng nhấn enter để bỏ qua)")
  to_list_str = input("To: ")
  tos = to_list_str.split(", ")
  for to in tos:
    tos_list.append(to)
  cc_list_str = input("CC: ")
  if (cc_list_str != ''):
    ccs = cc_list_str.split(", ")
    for cc in ccs:
      ccs_list.append(cc)
  bcc_list_str = input("BCC: ")
  if (bcc_list_str != ''):
    bccs = bcc_list_str.split(", ")
    for bcc in bccs:
      bccs_list.append(bcc)
  subject = input('Subject: ')
  content = input('Content: ')
  while True:
    attach_files = input("Có gửi kèm file (1. có, 2. không): ")
    if (attach_files == "1"):
      num_files = input("Số lượng file muốn gửi: ")
      num_files = int(num_files)
      for num in range(1, num_files + 1):
        attachment_path = input(f"Nhập đường dẫn file đính kèm cho file {num}: ")
        file_path.append(attachment_path)
      break
    elif (attach_files == "2"): break
    else: print("Lựa chọn không hợp lệ, bạn hãy nhập lại")
  return tos_list, ccs_list, bccs_list, subject, content, num_files, file_path

def body_format(tos_list, ccs_list, username, emailFrom, subject, content):
    unique_id = uuid.uuid4()
    named_tuple = time.localtime()
    local_time = time.strftime("%a, %d %b %Y %H:%M:%S", named_tuple)
    messageID = f"Message-ID: {unique_id}@example.com\r\n"
    date = f"Date: {local_time} +0700\r\n"
    to = f"""To: {",".join(tos_list)}\r\n"""
    cc = ''
    if len(ccs_list):
      cc = f"""Cc: {",".join(ccs_list)}\r\n"""
    from_ = f"""From: {username} <{emailFrom}>\r\n"""
    subject = f"""Subject: {subject}\r\n\r\n"""
    content = f"""{content}\r\n"""
    endMSG = ".\r\n"
    return messageID + date + to + cc + from_ + subject + content + endMSG

def body_format_attachment(to, cc, username, emailfrom, subject, content, file_path):
  msg = MIMEMultipart()
  local_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
  msg['Message-ID'] = f"{uuid.uuid4()}@example.com"
  msg['Date'] = f"{local_time} +0700"
  msg['To'] = "".join(to)
  if cc != '' :
    msg['Cc'] = "".join(cc)
  msg['From'] = f"{username} <{emailfrom}>"
  msg['Subject'] = "".join(subject)
  msg.attach(MIMEText("".join(content), 'plain'))
  for path in file_path:
    with open(path, 'rb') as attachment:
      attachment_part = MIMEApplication(attachment.read())
      file_type = path[path.rfind('.') + 1:] + "/None"
      file_name = path[path.rfind("\\") + 1:len(path)]
      attachment_part.set_type(file_type, header='Content-Type')
      attachment_part.add_header("Content-Disposition", "attachment",filename=file_name)
      msg.attach(attachment_part)
  return msg.as_bytes()

def send_data(client, host, username, emailFrom, tos_list, ccs_list, bccs_list, subject, content, num_files, file_path):
  send_command(client, f"EHLO [{host}]\r\n")
  send_command(client, f"MAIL FROM:<{emailFrom}>\r\n")
  for to in tos_list:
    send_command(client, f"RCPT TO:<{to}>\r\n")
  for cc in ccs_list:
    send_command(client, f"RCPT TO:<{cc}>\r\n")
  for bcc in bccs_list:
    send_command(client, f"RCPT TO:<{bcc}>\r\n")
  send_command(client, f"DATA\r\n")
  if (num_files == 0):
    body = body_format(tos_list, ccs_list, username, emailFrom, subject, content)
    send_command(client, body)
  else:
    body_attachment = body_format_attachment(tos_list, ccs_list, username, emailFrom, subject, content, file_path)
    client.send(body_attachment)
    send_command(client, "\r\n.\r\n")

def send_email(username, emailFrom, host, port):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  try:
    client.connect(server_address)
    client.recv(1024).decode()
  except Exception as e:
     print(f"Lỗi: {e}")
     return
  tos_list, ccs_list, bccs_list, subject, content, num_files, file_path = input_email()
  send_data(client, host, username, emailFrom, tos_list, ccs_list, bccs_list, subject, content, num_files, file_path)
  print("Đã gửi email thành công")
  client.close()
