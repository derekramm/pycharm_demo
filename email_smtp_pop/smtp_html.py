import smtplib
from email.message import EmailMessage

smtp_server = 'smtp.163.com'
from_addr = 'tedulivevideo@163.com'
password = 'tedu@2019'
to_addr = ['g-dongxy@tedu.cn', '992700808@qq.com', 'derek_ramm@icloud.com']

conn = smtplib.SMTP_SSL(smtp_server, 465)
conn.set_debuglevel(1)
conn.login(from_addr, password)

msg = EmailMessage()
msg.set_content('<h2>邮件标题</h2><p>你好，这是一封来自Python的邮件</p>', 'html', 'utf-8')
msg['subject'] = '一封邮件'
msg['from'] = f'domkn <{from_addr}>'
msg['to'] = f'大蜥蜴 <{to_addr}>'

conn.sendmail(from_addr, to_addr, msg.as_string())
conn.quit()
