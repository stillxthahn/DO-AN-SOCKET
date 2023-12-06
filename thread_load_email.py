import socket
import os
#from print_list_email import print_list_email
from get_email import get_email
from read_email import get_list_emails
import time
def auto_load_email(host, port, email, password):
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
  
def thread_load_email(host, port, email, password, choice, _time):
  while True:
    time.sleep(_time)
    auto_load_email(host, port, email, password)
    
    