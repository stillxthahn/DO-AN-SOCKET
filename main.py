import threading 
from send_email import send_email
from read_email import read_email
from thread_load_email import thread_load_email
from read_json_file import read_json_file
data = read_json_file('config.json')
USER = data["User"]
HOST = data["MailServer"]
SEND_PORT = int(data["SMTP"])
RECV_PORT = int(data["POP3"])
AUTOLOAD = data["Autoload"]


def client_login():
    while True:
        print("Vui lòng đăng nhập")
        email_input = input("Email: ")
        password_input = input("Mật khẩu: ")
        check_email = False
        check_password = ''
        check_username = ''
        for user in USER:
            if (email_input == user["Email"]):
                check_email = True
                check_password = user["Password"]
                username = user["Username"]
                break
        if (check_email == False):
            print("Email không hợp lệ, vui lòng nhập lại")
            continue
        if (password_input != check_password):
            print("Mật khẩu không chính xác, vui lòng nhập lại")
            continue
        return username, email_input, password_input;


username, email, password = client_login()

while True:
    print("Đăng nhập thành công!")
    print("Vui lòng chọn Menu:\r\n")
    print("1. Để gửi email\r\n")
    print("2. Để xem danh sách các email đã nhận\r\n")
    print("3. Thoát\r\n")
    choice = input("Bạn chọn: ")
    autoload = threading.Thread(target=thread_load_email, daemon=True, args=(HOST, RECV_PORT, email, password, choice, int(AUTOLOAD)))
    if (choice == "1"):
        if (threading.active_count() == 1):
            autoload.start()
        send_email(username, email, HOST, SEND_PORT)    
    elif (choice == "2"):
        if (threading.active_count() == 1):
            autoload.start()
        read_email(email, password, HOST, RECV_PORT)
    elif (choice == "3"):
        exit(0)