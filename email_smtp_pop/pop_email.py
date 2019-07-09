import poplib, os.path, mimetypes
from email.parser import BytesParser, Parser
from email.policy import default

email = 'tedulivevideo@163.com'
password = 'tedu@2019'
pop_server = 'pop.163.com'

# 连接到POP 3服务器
conn = poplib.POP3_SSL(pop_server, 995)

print('欢迎信息：')
print(conn.getwelcome().decode('utf-8'))

print()

conn.user(email)
conn.pass_(password)

message_num, total_size = conn.stat()
print('统计信息：')
print(f'邮件数量：{message_num}, 总大小：{total_size}')

print()

# 获取服务器上的邮件列表，相当于发送POP3的list命令
# resp 保存服务器的响应码
# mails列表保存每封邮件的编号、大小
resp, mails, octets = conn.list()
print('列表信息：')
print(f'响应代码：{resp}, 邮件列表：{mails}')

print()

# 获取指定邮件的内容（此处传入总长度，也就是获取最后一封邮件）
# 相当于发送POP 3的retr命令
# resp 保存服务器的响应码
# data 保存该邮件的内容
resp, data, octets = conn.retr(len(mails))

# 将data的所有数据（原本是一个字节列表）拼接在一起
msg_data = b'\r\n'.join(data)

# 将字符串内容解析成邮件，此处一定要指定 policy=default
msg = BytesParser(policy=default).parsebytes(msg_data)

conn.quit()

print(f'邮件标题：{msg["subject"]}')
print(f'发件人：{msg["from"]}')
print(f'收件人：{msg["to"]}')

for part in msg.walk():
    counter = 1

    # 如果maintype是multipart，说明是容器（用于包含正文、附件等）
    if part.get_content_maintype() == 'multipart':
        continue

    # 如果maintype是multipart，说明是邮件正文部分
    elif part.get_content_maintype() == 'text':
        print(part.get_content())

    # 处理附件
    else:
        # 获取附件的文件名
        filename = part.get_filename()
        # 如果没有文件名，程序要负责为附件生成文件名
        if not filename:
            # 根据附件的contnet_type来推测它的后缀名
            ext = mimetypes.guess_extension(part.get_content_type())
            # 如果推测不出后缀名
            if not ext:
                # 使用.bin作为后缀名
                ext = '.bin'
            # 程序为附件来生成文件名
            filename = 'part-%03d%s' % (counter, ext)
            print(filename)
        counter += 1