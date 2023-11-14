from readConfig import readConfig
from sendEmail import sendEmail
from readEmail import readEmail
#READ CONFIG FILE
data = readConfig()
USERNAME = data["Username"]
EMAIL = data["Email"]
PASSWORD = data["Password"]
HOST = data["MailServer"]
SEND_PORT = int(data["SMTP"])
RECV_PORT = int(data["POP3"])
AUTOLOAD = data["Autoload"]
#confict
#MAIL CLIENT CONSOLE

while True:
    print("Vui lòng chọn Menu:\r\n")
    print("1. Để gửi email\r\n")
    print("2. Để xem danh sách các email đã nhận\r\n")
    print("3. Thoát\r\n")
    choice = input("Bạn chọn: ")
    if (choice == "1"):
        #SEND EMAIL
        sendEmail(USERNAME, EMAIL, HOST, SEND_PORT)
    elif (choice == "2"):
        #READ EMAIL
        readEmail(EMAIL, PASSWORD, HOST, RECV_PORT)
    elif (choice == "3"):
        exit(0)
        #hehe
        