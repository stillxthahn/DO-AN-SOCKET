from read_json_file import read_json_file
from send_email import send_email
from read_email import read_email

#READ CONFIG FILE
data = read_json_file("config.json")
USERNAME = data["Username"]
EMAIL = data["Email"]
PASSWORD = data["Password"]
HOST = data["MailServer"]
SEND_PORT = int(data["SMTP"])
RECV_PORT = int(data["POP3"])
AUTOLOAD = data["Autoload"]
#MAIL CLIENT CONSOLE

while True:
    print("Vui lòng chọn Menu:\r\n")
    print("1. Để gửi email\r\n")
    print("2. Để xem danh sách các email đã nhận\r\n")
    print("3. Thoát\r\n")
    choice = input("Bạn chọn: ")
    if (choice == "1"):
        #SEND EMAIL
        send_email(USERNAME, EMAIL, HOST, SEND_PORT)
    elif (choice == "2"):
        #READ EMAIL
        read_email(EMAIL, PASSWORD, HOST, RECV_PORT)
    elif (choice == "3"):
        exit(0)