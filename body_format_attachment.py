from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import mimetypes
def body_format_attachment(client, to, subject, content, num_files, file_path):
  msg = MIMEMultipart()
  msg['To'] = to
  msg['Subject'] = subject
  msg.attach(MIMEText(content, 'plain'))
  for path in file_path:
    with open(path, 'rb') as attachment:
      attachment_part = MIMEApplication(attachment.read())
      file_type = mimetypes.guess_type(path)
      attachment_part.set_type(str(file_type[0]), header='Content-Type')
      attachment_part.add_header("Content-Disposition", "attachment", filename=path)
      msg.attach(attachment_part)
  return msg.as_bytes()

