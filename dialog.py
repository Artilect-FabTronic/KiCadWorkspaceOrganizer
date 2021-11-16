import wx
import MyFrame1

 # creaing application object with the Python object
Application1 = wx.App()
 # creating a frame with the Python object
 ##TODO: find the parent
frame = MyFrame1.MyFrame1(None)

frame.Show()

 # start the event loop to run the application
Application1.MainLoop()