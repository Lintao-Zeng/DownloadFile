#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import requests
from tqdm import tqdm

def download(url: str, fname: str):
    # 用流stream的方式获取url的数据
    resp = requests.get(url, stream=True)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)



download("https://github.com/git-for-windows/git/releases/download/v2.37.1.windows.1/Git-2.37.1-64-bit.exe", "file.exe")



sender = '2070047236@qq.com'
my_pass='mwzcpfwrixjecfbj'
receivers = '2534324260@qq.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("Github Actions", 'utf-8')
message['To'] = Header("You", 'utf-8')
subject = '文件下载完毕'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
#message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('file.exe', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="file.exe"'
message.attach(att1)

server=smtplib.SMTP_SSL("smtp.qq.com", 465) # 发件人邮箱中的SMTP服务器，端口是25
server.login(sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
server.sendmail(sender,[receivers,],message.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
server.quit() # 关闭连接

print("文件下载完毕！")
