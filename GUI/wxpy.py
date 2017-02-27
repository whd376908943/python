# coding:utf-8
# 导入wxpython模块
# 一个应用程序App必须要有一个顶级窗口，否则没有可显示的界面，而顶级窗口则是Frame的子类
import wx

'''
# 实例化wx模块App类，表示一个应用程序的实例
app = wx.App()
# 实例化Frame类，可以接受参数，parent表示父窗口，没有则表示顶级窗口
# Frame是所有窗口的父类
frame = wx.Frame(parent = None, title = 'GUI')
# 展现窗口
frame.Show()
# 时间循环，接收各种事件，如拖动，最小化，最大化窗口
app.MainLoop()
'''

'''
# 除了使用系统的App类，还可以自定义自己的App类
class MyApp(wx.App):
    def __init__(self):
		wx.App.__init__(self)
# OnInit方法在实例化该类的时候就会调用，不需要手动调用
# 该方法返回True程序正常执行，返回False程序就会退出
	def OnInit(self):
		self.frame = wx.Frame(parent = None, title = 'GUI')
		self.frame.Show()
# 指定某个窗口为顶级窗口，默认第一个窗口为顶级窗口
		self.SetTopWindow(self.frame)
		return True
app = MyApp()
app.MainLoop()
'''

'''
# 自定义Frame类
class myFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'GUI',size=(300,200))
# Panel面板可以作为一个容器，作为其他控件的父类，其他控件引用了该容器后，整个面板(窗口)会变成白色
		panel = wx.Panel(self,-1)
# 创建一个标签用于显示文本信息,坐标是相对于窗口的位置		
		label = wx.StaticText(panel,-1,'Hello Wxpython',(0,10))
# 设置文本字体标签背景色		
		label.SetBackgroundColour('black')
# 设置字体颜色
		label.SetForegroundColour('white')

# 创建一个标签用于显示文本信息,坐标是标签相对于窗口的位置,(160,-1)为文本标签的长度，-1表示高度默认
# wx.ALIGN_LEFT表示字体在标签内居左,wx.ALIGN_CENTER表示居中
		labe2 = wx.StaticText(panel,-1,'Hello Wxpython!',(0,50),(160,-1),wx.ALIGN_LEFT)
# 设置文本字体标签背景色		
		labe2.SetBackgroundColour('green')
# 设置字体颜色
		labe2.SetForegroundColour('yellow')
app = wx.App()
xframe = myFrame()
xframe.Show()
app.MainLoop()
'''

'''
class myFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'GUI',size=(300,200))
		panel = wx.Panel(self,-1)
# 设置一个文本输入框，(100,50)表示文本输入框相对于面板的位置
		text = wx.TextCtrl(panel,-1,'Input your name:',(100,50))
# 设置光标插入的位置，待验证
#		text.SetInsertionPoint(3)
app = wx.App()
xframe = myFrame()
xframe.Show()
app.MainLoop()
'''

'''
class myFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'GUI',size=(300,200))
		panel = wx.Panel(self,-1)
# 定义按钮
		button = wx.Button(panel,-1,'submit',(100,50))
app = wx.App()
xframe = myFrame()
xframe.Show()
app.MainLoop()
'''

class myFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'GUI',size=(700,700))
		panel = wx.Panel(self,-1)
# 定义图片格式的按钮，图片格式必须为bmp
		bmp = wx.Image(r'E:\button.bmp',wx.BITMAP_TYPE_BMP).ConvertToBitmap()
		button = wx.BitmapButton(panel,-1,bmp,(100,50))
app = wx.App()
xframe = myFrame()
xframe.Show()
app.MainLoop()

