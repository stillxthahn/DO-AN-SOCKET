import threading 
from send_email import send_email
from read_email import read_email
from thread_load_email import thread_load_email
from read_json_file import read_json_file
data = read_json_file('config.json')
USERNAME = data["Username"]
EMAIL = data["Email"]
PASSWORD = data["Password"]
HOST = data["MailServer"]
SEND_PORT = int(data["SMTP"])
RECV_PORT = int(data["POP3"])
AUTOLOAD = data["Autoload"]

while True:
    print("Vui lòng chọn Menu:\r\n")
    print("1. Để gửi email\r\n")
    print("2. Để xem danh sách các email đã nhận\r\n")
    print("3. Thoát\r\n")
    choice = input("Bạn chọn: ")
    autoload = threading.Thread(target=thread_load_email, daemon=True, args=(HOST, RECV_PORT, EMAIL, PASSWORD, choice, int(AUTOLOAD)))
    if (choice == "1"):
        if (threading.active_count() == 1):
            autoload.start()
        send_email(USERNAME, EMAIL, HOST, SEND_PORT)    
    elif (choice == "2"):
        if (threading.active_count() == 1):
            autoload.start()
        read_email(EMAIL, PASSWORD, HOST, RECV_PORT)
    elif (choice == "3"):
        exit(0)