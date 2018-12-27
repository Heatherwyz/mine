# -*- coding:utf-8 -*-

__author__ = 'Heather'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":
    print ("发送HTML邮件示例")
    # 邮件发送者
    sender = "deep_test@126.com"

    # 邮件接收地址列表
    # 请将xxx改为你的126邮箱名或整个改为你的目标接收邮箱地址
    receivers = "xxx@126.com"

    # 发送内容构建
    # html标识发送内容为文本格式
    msg = MIMEMultipart ()
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header ("开源优测_DeepTest", "utf-8")

    # 构建邮件正文内容
    msg.attach (MIMEText ("微信公众号：开源优测", "plain", "utf-8"))

    # 构造附件,多个附件同理
    attach1 = MIMEText (open ("发送附件邮件.py", 'rb').read (), "base64", "utf-8")
    attach1["Content-Type"] = "application/octet-stream"

    # 这里filename随意写，将会在邮件中显示
    attach1["Content-Disposition"] = "attrachment;filename=code.py"

    # 关联附件到邮件中
    msg.attach (attach1)

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "deep_test"

    # 发送人邮件密码或专用于smtp账户的密码
    password = "123456a"

    # 构建smtp对象
    smtp = smtplib.SMTP ()

    # 连接到smtp服务
    con = smtp.connect (smtpserver, smtpport)
    print ("连接结果： ", con)

    # 登录smtp服务
    log = smtp.login (username, password)

    print ("登录结果：", log)

    # 发送邮件
    print (receivers)
    res = smtp.sendmail (sender, receivers, msg.as_string ())

    print ("邮件发送结果： ", res)

    # 退出
    smtp.quit ()

    print ("send email finish")