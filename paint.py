# coding:utf-8


import numpy as np
import matplotlib.pyplot as plt

# 类似于range函数，指定开始值，终值，和步长来创建数组，不包括终值
# print np.arange(0, 1, 0.1)
# 指定开始值，终值，和数组长度来创建数组，不包括终值，缺省包括终值，默认长度为50
# print np.linspace(1, 10)
# π值
# print np.pi
# 传入一个列表，对列表的每一个数据sin运算
# print np.sin([1, 2, 3, 4])
# 线条颜色
'''
    'b'         blue
    'g'         green
    'r'         red
    'c'         cyan
    'm'         magenta
    'y'         yellow
    'k'         black
    'w'         white
'''
# 线条样式
'''
    '-'         solid
    '--'        dashed
    '-.'        dash_dot
    ':'         dotted
    'None'
'''
# 线条marker样式
'''
    's'
    'p'
    '*.'
    'h'
    'H'
    '+'
    'x'
    'D'
    'd'
'''

'''
x = np.arange(-np.pi, np.pi, 0.01)
y1 = np.sin(x)
# y2 = np.cos(x)
# 传入列表，描点
plt.plot(x, y1, 'ro')
# plt.plot(x, y2, 'k*')
# o表示为画散点图
# plt.plot(x, y, 'o')
# plt.plot(x, y, 'or')
# plt.plot(x, y, 'or')
# 指定坐标的刻度值
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# plt.yticks([-1, 0, +1])
# axis参数格式是[x轴最小值，x轴最大值，y轴最小值，y轴最大值]等价于xlim和ylim
# plt.axis([-3, 0, -3, 3])
# 文字提示说明:文字提示符，坐标位置，文字位置，文字颜色
# plt.annotate('local max', xy=(0, 0), xytext=(0, 0.5), arrowprops=dict(facecolor='green'),)
plt.show()
'''

'''
x = np.arange(-5, 5, 0.01)
y = map(lambda a: a**3, x)
# 创建绘图对象，长，宽单位为英寸，不写该语句时系统会自动创建绘图对象
plt.figure(figsize=(8, 4))
plt.plot(x, y, color="green", linewidth=1.0, linestyle="-")
# 画表格线
plt.grid(True)
# 文件保存，dpi指定分辨率，每英寸多少个像素
# plt.savefig("2.png", dpi=72)
# 设置文字提示信息
plt.title('title')
plt.xlabel('Score')
plt.ylabel('Score')
# 设置坐标轴取值范围
plt.xlim(-4, 4)
plt.ylim(-100, 100)
plt.legend()
plt.show()
'''

'''
x = np.arange(-np.pi, np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# 传入列表，描点
plt.plot(x, y1, 'b', label='consine')
plt.plot(x, y2, 'o', label='sine')
# 使用图例，loc表示图例的位置，0表示合适的位置，使用之前在plot中指定label标签
plt.legend(loc=0)
plt.show()
'''

'''
# 使用子视图
# 第一个视图窗口
plt.figure(1)
# 第一个视图窗口中的第一个子视图
# 211表示该窗口两个横行子视图,一列子视图，切换到第一个子视图
plt.subplot(211)
plt.plot([1, 2, 3])
# 地一个视图窗口中的第二个子视图
plt.subplot(212)
plt.plot([4, 5, 6])
# 第二个视图窗口
plt.figure(2)
# 默认创建subplot(111)
plt.plot([4, 5, 6])
# 切换到第一个视图窗口，并且当前的子视图还是subplot(212)
plt.figure(1)
# 使第一个视图窗口的subplot(211)及第一个子视图为当前子视图
plt.subplot(211)
# 第一个子视图的标题
plt.title('Easy as 1,2,3')
plt.show()
'''

'''
# 切换子视图，并且绘图
plt.subplot(321, axisbg='k')
plt.subplot(322, axisbg='g')
plt.subplot(323, axisbg='b')
plt.subplot(324, axisbg='y')
plt.subplot(325, axisbg='r')
plt.subplot(326, axisbg='c')
plt.show()
'''
