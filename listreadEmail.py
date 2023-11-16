import socket

def listreadEmail(data):
    list = data.split('\r\n')
    list = list[1:]
    list = list[:-2]
    tmp = []
    for i in range(0, len(list)):
        listnoSpace = list[i].split(' ')
        tmp.append(listnoSpace[1])
    return tmp
