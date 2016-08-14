# coding:utf-8

import sys
import easygui as g

title = '小游戏'
msg = 'Shall I continue'
choices = ['a', 'b', 'c']
# g.msgbox(msg, title)
# if g.ccbox(msg, title):
#   g.msgbox('继续', title)
# else:
#   g.msgbox('byebye', title)
# a = g.buttonbox(msg, title, choices)
# print a
# a = g.boolbox(msg, title)
# print a
# a = g.indexbox(msg, title)
# print a
# a = g.boolbox(msg, title)
# print a
# a = g.enterbox(msg, title,strip=False)
# a = g.multenterbox(msg, title, ('user', 'passwd', 'QQ'))
# a = g.passwordbox(msg, title)
# a = g.multpasswordbox(msg, title, ('user', 'passwd', 'QQ'))

# a = g.textbox(msg, title, 'content')
# a = g.fileopenbox(msg, title, 'E:\\', ["*.doc"])
a = g.filesavebox(msg, title, 'E:\\简历.doc')
print a
