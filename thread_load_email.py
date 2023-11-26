import socket
from send_email import send_command
from print_list_email import print_list_email
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
  list = get_list_emails(client, email, password)
  get_email(client, list)
def thread_load_email(host, port, email, password, choice, _time):
    while choice != 3:
        time.sleep(_time)
        auto_load_email(host, port, email, password)