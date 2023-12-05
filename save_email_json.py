import json
import os
def save_email_json(data_parse, filename, user_folder):
    dataEnroll = dict();
    dataEnroll['Status'] = "0"
    dataEnroll['From'] = data_parse['From']
    dataEnroll['Subject'] = data_parse['Subject']
    dataEnroll['Filename'] = filename
    json_file_path = os.path.join(user_folder,'email_infor.json')
    try:
        f = open(json_file_path, "r")
        data = json.load(f)
        f.close()
        data.append(dataEnroll)
        f = open(json_file_path, 'w')
        f.write(json.dumps(data))
        f.close()
    except Exception as FileNotFoundError:
        f = open(json_file_path, 'w')
        data = []
        data.append(dataEnroll)
        f.write(json.dumps(data))
        f.close()