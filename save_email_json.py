import json

def save_email_json(data_parse, filename):
    dataEnroll = dict();
    dataEnroll['Status'] = "0"
    dataEnroll['From'] = data_parse['From']
    dataEnroll['Subject'] = data_parse['Subject']
    dataEnroll['Filename'] = filename
    try:
        f = open('email_infor.json', "r")
        data = json.load(f)
        f.close()
        data.append(dataEnroll)
        f = open('email_infor.json', 'w')
        f.write(json.dumps(data))
        f.close()
    except Exception as FileNotFoundError:
        f = open('email_infor.json', 'w')
        data = []
        data.append(dataEnroll)
        f.write(json.dumps(data))
        f.close()