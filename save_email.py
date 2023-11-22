import os
from send_email import send_command
from read_json_file import read_json_file

def parse_email(data):
  lines = data.split('\n')
  boundary = ""
  message_id = ""
  date = ""
  tos = []
  _from = ""
  subject = ""
  attachment_arr = []
  content = ""
  start_idx_attach = 0
  if (lines[0].startswith("Content-Type: multipart/mixed") == 1):
    boundary = lines[0][lines[0].find('"') + 1:len(lines[0]) - 1]
    for i in range(1, len(lines)):
      if lines[i].startswith("Message-ID"): message_id = lines[i].split(": ", 1)[1]
      elif lines[i].startswith("Date"): date = lines[i].split(": ", 1)[1]
      elif lines[i].startswith("To"): 
        to = lines[i].split(": ", 1)[1]
        tos = to.split(',')
      elif lines[i].startswith("From"): _from = lines[i].split(": ", 1)[1]
      elif lines[i].startswith("Subject"): subject = (lines[i].split(": ", 1)[1]).strip()
      elif boundary in lines[i]:
        start_idx_attach = i
        break

    for j in range(start_idx_attach + 1, len(lines), 1):
      if lines[j].startswith("Content-Transfer-Encoding: 7bit"):
        for k in range(j + 2, len(lines)):
          if boundary in lines[k]:
            break
          content = content + lines[k]
      elif lines[j].startswith("Content-Disposition: attachment"):
        attachment_data = ""
        file_name = lines[j][lines[j].find('"') + 1:len(lines[j]) + 1]
        for k in range(j + 2, len(lines)):
          if boundary in lines[k]:
            break
          attachment_data = attachment_data + lines[k]
        attachment_data.strip()
        attachment = {"name": file_name, "data": attachment_data}
        attachment_arr.append(attachment)
    return {"ID": message_id, "date": date, "tos": tos, "from": _from, "subject": subject, "content": content, "attachment": attachment_arr}
    