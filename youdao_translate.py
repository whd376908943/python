# coding:utf-8

import urllib
import json


content = raw_input('please input content to translate:\n')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
data = {
    'type': 'AUTO',
    'i': content,
    'doctype': 'json',
    'xmlVersion': '1.8',
    'keyfrom': 'fanyi.web',
    'ue': 'UTF-8',
    'action': 'FY_BY_CLICKBUTTON',
    'typoResult': 'true'
}
data = urllib.urlencode(data).encode('utf-8')
html = urllib.urlopen(url, data)
res = html.read()
target = json.loads(res)
print target['translateResult'][0][0]['tgt']




