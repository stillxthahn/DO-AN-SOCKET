def print_list_email(data):
    list = data.split('\r\n')
    list = list[1:]
    list = list[:-2]
    tmp = []
    for i in range(0, len(list)):
        list_no_Space = list[i].split(' ')
        tmp.append(list_no_Space[1])
    return tmp
#C:\Users\LENOVO\OneDrive\Máy tính\09.pdf
#C:\Users\LENOVO\OneDrive\Hình ảnh\22127404-P.jpg
#C:\Users\LENOVO\OneDrive\Máy tính\img.zip