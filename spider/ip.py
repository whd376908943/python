# coding:utf-8


import urllib
from bs4 import BeautifulSoup


def get_ip():
    ip = raw_input('please input your ip:\n')
    return ip


def get_url(ip):
    url = 'http://www.ip138.com/ips1388.asp?ip={0}&action=2'.format(ip)
    return url


def get_content(url):
    res = urllib.urlopen(url)
    return res.read().decode('gbk').encode('utf-8')


def get_addr(content):
    soup = BeautifulSoup(content, 'html.parser')
    li = soup.find_all('li')
    return li[0].string[5:]

if __name__ == '__main__':
    ip = get_ip()
    url = get_url(ip)
    html = get_content(url)
    print get_addr(html)
