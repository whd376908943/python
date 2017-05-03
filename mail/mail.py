# coding=utf-8 
from smtplib import * 
from email.mime.text import MIMEText 



from_address = 'wanghuidong@cmcaifu.com' 
to_address = ['wanghd.dlc@outlook.com','sysadmin@cmcaifu.com'] 
server = 'mail.cmcaifu.com' 
passwd = '****' 
subject = u'邮件推送测试' 

msg = MIMEText(''' hello!<br/> test!<hr/> ''', 'html', 'utf-8') 
msg['Subject'] = subject 
msg['From'] = from_address 
msg['To'] = ','.join(to_address) 


server = SMTP(server, 25) 
server.set_debuglevel(1) 
server.login(from_address, passwd)

server.sendmail(from_address, to_address, msg.as_string()) # 把MIMEText类型转化为字符串 server.quit()
