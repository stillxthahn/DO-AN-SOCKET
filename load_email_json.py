'''
#import socket
import extract_msg

def displayEmail_Infor(LIST):
    for i in LIST:
'''
import os
import json

def load_email_json(data_parse, filename):
    dataEnroll = dict();
    dataEnroll['Status'] = "0"
    dataEnroll['From'] = data_parse['From']
    dataEnroll['Subject'] = data_parse['Subject']
    dataEnroll['Filename'] = filename

    try:
        f = open('Email_Infor.json', "r")
        data = json.load(f)
        f.close()
        data.append(dataEnroll)
        f = open('Email_Infor.json', 'w')
        f.write(json.dumps(data))
        f.close()
    except Exception as FileNotFoundError:
        f = open('Email_Infor.json', 'w')
        data = []
        data.append(dataEnroll)
        f.write(json.dumps(data))
        f.close()