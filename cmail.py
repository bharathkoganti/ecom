import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('bharathkoganti26@gmail.com','agap kqzy zzwd mbkv')
    msg=EmailMessage()
    msg['FROM']='janardhanb322@gmail.com'
    msg['To']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()