'''
#import socket
import extract_msg

def displayEmail_Infor(LIST):
    for i in LIST:
'''
import os
import json
def load_email_json(client, List):
    feeds = []
    with open("Email_Infor.json", mode='w', encoding='utf-8') as f:
        for i in range(1, len(List) + 1):
            retrCommand = f"RETR {i}\r\n"
            #print(retrCommand)
            client.send(retrCommand.encode())
            data = client.recv(1024)
            data = data.decode()
            dataList = data.split('\r\n')
            dataList[5] = dataList[5][6:]
            dataList[6] = dataList[6][9:]
            data = { 'status' : "0", "from" : dataList[5], "subject" : dataList[6]}
            feeds.append(data)
        
        json.dump(feeds, f)
        