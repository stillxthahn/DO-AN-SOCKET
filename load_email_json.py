'''
#import socket
import extract_msg

def displayEmail_Infor(LIST):
    for i in LIST:
'''
import os
import json
from read_json_file import read_json_file
def load_email_json(client, List):
    feeds = []
    
    print(existing_data_json)
    print("JSON: ", existing_data_json)
    with open("Email_Infor.json", mode='w', encoding='utf-8') as f:
        existing_data = existing_data.join(f.read())
    print(existing_data)
    
    with open("Email_Infor.json", mode='w', encoding='utf-8') as f:
        for i in range(1, len(List) + 1):
            retrCommand = f"RETR {i}\r\n"
            #print(retrCommand)
            client.send(retrCommand.encode())
            data = client.recv(1024)
            data = data.decode()
            dataList = data.split('\r\n')
            CONTENT = ''
            TO = ''
            FROM = ''
            DATE = ''
            SUBJECT = ''
            index_Content = 0
            for j in range(0, len(dataList)):
                if index_Content == 0:
                    if dataList[j][0:2] == 'To':
                        TO = dataList[j][4:]
                    if dataList[j][0:4] == 'From':
                        FROM = dataList[j][6:]
                    if dataList[j][0:7] == 'Subject':
                        SUBJECT = dataList[j][9:]
                        index_Content = j
                        break
                    if dataList[j][0:4] == 'Date':
                        DATE = dataList[j][6:]
            for i in range(index_Content + 1, len(dataList) - 2):
                if dataList[i][0:7] == 'Content':
                    continue
                #if dataList[i] == '\r\n':
                    #continue
                CONTENT = CONTENT + dataList[i]
            data = {'status' : "0", 'date' : DATE, 'from' : FROM, 'to' : TO, 'subject' : SUBJECT, 'content' : CONTENT}
        json.dump(feeds, f)
        