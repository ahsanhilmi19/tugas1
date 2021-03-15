import wx
import bebas

app = wx.App()
frame = bebas.MyFrame1(parent=None)
frame.Show()
app.MainLoop()
