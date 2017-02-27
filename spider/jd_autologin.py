# coding:utf-8


import requests
import bs4



url1 = 'https://passport.jd.com/uc/loginService'
url = 'https://passport.jd.com/new/login.aspx'
s = requests.Session()                             # 注意session会话的位置设置也有关系
html = s.get(url).text
soup = bs4.BeautifulSoup(html, "html.parser")
logname = raw_input("please input your usrname:")
logpwd = raw_input("please input your passwd:")
argv_t = soup.find_all('input', {'name': '_t'})[0]['value']
argv_uuid = soup.find_all('input', {'name': 'uuid'})[0]['value']
argv_Net = soup.find_all('input', {'name': 'machineNet'})[0]['value']
argv_Cpu = soup.find_all('input', {'name': 'machineCpu'})[0]['value']
argv_Disk = soup.find_all('input', {'name': 'machineDisk'})[0]['value']
argv_eid = soup.find_all('input', {'name': 'eid'})[0]['value']
argv_fp = soup.find_all('input', {'name': 'fp'})[0]['value']
argv_logType = soup.find_all('input', {'name': 'loginType'})[0]['value']
argv = soup.find_all('input', {'type': 'hidden'})
argv_key = argv[8]['name']
argv_value = argv[8]['value']
argv_authcode = soup.find_all('input', {'name': 'fp'})[0]['value']
imgurl = "https://authcode.jd.com/verify/image?a=1&acid="+argv_uuid
img = s.get(imgurl)
with open('img.jpg', 'wb') as i:
    i.write(img.content)
auth = raw_input("please input authcode:")
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
data = {
    'uuid': argv_uuid,
    'machineNet': argv_Net,
    'machineCpu': argv_Cpu,
    'machineDisk': argv_Disk,
    'eid': argv_eid,
    'fp':  argv_fp,
    '_t': argv_t,
    'loginType': argv_logType,
     argv_key: argv_value,
    'loginname': logname,
    'nloginpwd': logpwd,
    'loginpwd': logpwd,
    'chkRememberMe': 'on',
    'authcode': auth
}
res = s.post(url1, headers=header, data=data)
print res.text
