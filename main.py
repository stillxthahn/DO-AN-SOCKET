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
        print("Đăng nhập thành công!")
        return username, email_input, password_input


if __name__ == "__main__":
    while True:
        print("1. Đăng nhập")
        print("2. Thoát")
        choice = input("Bạn chọn: ")
        if (choice == "2"):
            exit(0)
        if (choice != "1"):
            print("Lựa chọn không hợp lệ, vui lòng chọn lại")
            continue
        username, email, password = client_login()
        event = threading.Event()
        autoload = threading.Thread(target=thread_load_email, daemon=True, args=(HOST, RECV_PORT, email, password, event, int(AUTOLOAD)))
        if (threading.active_count() == 1):
            autoload.start()
        while True:
            print("\r\nVui lòng chọn Menu:")
            print("1. Để gửi email")
            print("2. Để xem danh sách các email đã nhận")
            print("3. Đăng xuất")
            choice = input("Bạn chọn: ")
            
            if (choice == "1"):
                send_email(username, email, HOST, SEND_PORT)    
            elif (choice == "2"):
                read_email(email, password, HOST, RECV_PORT)
            elif (choice == "3"):
                event.set()
                print("Đang đăng xuất")
                autoload.join()
                break
        print("Đăng xuất thành công")
    