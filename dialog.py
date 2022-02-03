import wx
import WorkspaceDialog
import WindowsContext

Application1 = wx.App()

frame2 = WorkspaceDialog.WorkspaceDialog(None)
frame2.Show()

windows = wx.GetTopLevelWindows()
WindowsContext.WindowsContext(windows)

Application1.MainLoop()