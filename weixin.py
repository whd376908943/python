# coding:utf-8

import requests


def get_token():
    values = {
        'corpid': 'wx3811723127b64d48',
        'corpsecret': 'kMQMdnd72ah_Aovqu6Q3fHG_oMpCHuLBoDFoJ7laeMZ9VeT9s1qdOLa5T-UTVnVo'
    }
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    r = requests.get(url, params=values)
    return r.json()['access_token']


def send_msg(token, msg):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token)
    data = {

        "touser": "@all",
        "agentid": '1',
        "msgtype": "text",
        "text": {
            "content": msg
        },
        'safe': '0'

    }
    requests.post(url, json=data)


if __name__ == '__main__':
    msg = 'Hello!'
    send_msg(get_token(), msg)
