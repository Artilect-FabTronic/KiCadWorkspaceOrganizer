import wx
from workspaceDialog import MyFrame1
from windowsContext import WindowsContext

Application1 = wx.App()

frame2 = MyFrame1(None)
frame2.Show()

windows = wx.GetTopLevelWindows()
WindowsContext(windows)

Application1.MainLoop()