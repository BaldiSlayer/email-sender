import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(data):    
    msg = MIMEMultipart()
    msg['From'] = data['email_for_spam']
    msg['To'] = data['email']
    msg['Subject'] = data['theme']  
    body = data['text']

    msg.attach(MIMEText(body, 'plain'))    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(data['email_for_spam'], data['password'])
    text = msg.as_string()

    for _ in range(int(data['number_of_cycles'])):
        server.sendmail(data['email_for_spam'], data['email'], text)
    server.quit()