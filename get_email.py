import os
from read_json_file import read_json_file
from save_email_json import save_email_json
JSON_FILTER = read_json_file('filter.json')
BUFF_SIZE = 4096

def parse_email(data, spliter):
  lines = data.split(spliter)
  boundary = ""
  message_id = ""
  date = ""
  tos = []
  ccs = []
  _from = ""
  subject = ""
  attachment_arr = []
  content = ""
  start_idx_attach = -1

  for i in range(0, len(lines)):
    if (lines[i].find("Content-Type: multipart/mixed") != -1):
      boundary = lines[0][lines[0].find('"') + 1:len(lines[0]) - 1]
    elif lines[i].startswith("Message-ID"): message_id = lines[i].split(": ", 1)[1]
    elif lines[i].startswith("Date"): date = lines[i].split(": ", 1)[1]
    elif lines[i].startswith("To"): 
      to = lines[i].split(": ", 1)[1]
      tos = to.split(',')
    elif lines[i].startswith("Cc"): 
      cc = lines[i].split(": ", 1)[1]
      ccs = cc.split(',')
    elif lines[i].startswith("From"): _from = lines[i].split(": ", 1)[1]
    elif lines[i].startswith("Subject"): 
      subject = (lines[i].split(": ", 1)[1]).strip()
    if subject != '' and lines[i] == '':
      start_idx_attach = i
      break
  if (boundary == ""):
    for i in range(start_idx_attach, len(lines)):
      content = content + lines[i] + '\n'
    content = content[1:content.rfind('.') - 2]
    return {"ID": message_id, "Date": date, "To": tos, "Cc": ccs, "From": _from, "Subject": subject, "Content": content}

  else:
    for j in range(start_idx_attach, len(lines), 1):
      if lines[j].startswith("Content-Transfer-Encoding: 7bit"):
        for k in range(j + 2, len(lines)):
          if boundary in lines[k]:
            break
          content = content + lines[k]
      elif lines[j].startswith("Content-Disposition: attachment"):
        attachment_data = ""
        file_name = ""
        if (lines[j].find("filename") != -1):
          file_name = lines[j][lines[j].find('"') + 1:len(lines[j]) - 1]
        else:
          file_name = lines[j + 1][lines[j + 1].find('"') + 1:len(lines[j + 1])- 1]
        for k in range(j + 2, len(lines)):
          if boundary in lines[k]:
            break
          attachment_data = attachment_data + lines[k]
        attachment_data.strip()
        attachment = {"name": file_name, "data": attachment_data}
        attachment_arr.append(attachment)
    return {"ID": message_id, "Date": date, "To": tos, "Cc": ccs, "From": _from, "Subject": subject, "Content": content, "Attachment": attachment_arr}
    
def save_email_msg(data, filename, user_folder, folderfilter):
  file_path = os.path.join(user_folder, "mailbox", folderfilter, filename)
  data_arr = data.split('\r\n')
  with open(file_path, "w") as f:
    for item in data_arr:
      item = item + '\n'
      f.write(item)


def filtering_email(data, filename, user_folder):
  data_parse = parse_email(data, '\r\n')
  save_email_json(data_parse, filename, user_folder)
  check_filter = False
  for object in JSON_FILTER:
    for category in object["type"]:
      for value in object["value"]:
        if (value in data_parse[category]):    
          save_email_msg(data, filename, user_folder, object["folder"])
          check_filter = True
  if not check_filter:
    save_email_msg(data, filename, user_folder, "Inbox")

def check_existed_file(filename, mailbox_folder):
  list_folder = os.listdir(mailbox_folder)
  for folder in list_folder:
    mails_in_folder = os.listdir(os.path.join(mailbox_folder, folder))
    if filename in mails_in_folder:
      return True
  return False

def get_email(client, user_folder, list):
  mailbox_folder = os.path.join(user_folder, "mailbox")
  for i in range(1, len(list) + 1):
      if (check_existed_file(list[i - 1], mailbox_folder) == True):
        continue
      client.send(f"RETR {i}\r\n".encode())
      data_server = b""
      while True:
        chunk = client.recv(BUFF_SIZE)
        data_server += chunk
        if len(chunk) < BUFF_SIZE:
          break
      data_server = data_server.decode()
      data_server = data_server[data_server.find('\n') + 1:]
      filtering_email(data_server, list[i - 1], user_folder)
