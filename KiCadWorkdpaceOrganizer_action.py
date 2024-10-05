import pcbnew
import os
import re
import datetime
import wx
import wx.aui

from .WindowsContext import WindowsContext
from .WorkspaceDialog import WorkspaceDialog
from .Splits import Splits, SplitsTypes

def debug_init():
    global Application1
    Application1 = wx.App()

def debug_loop():
    global Application1
    Application1.MainLoop()

class KiCadWorkdpaceOrganizerAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "KiCad Workspace Organizer"
        self.category = "Quality of life"
        self.description = "Working on KiCad on one screen but easier"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'img/icon.png') # Optional

    def Run(self):
        # wc = WindowsContext(wx.GetTopLevelWindows())
        # Splits(SplitsTypes.twoToOne)
        
        frame2 = WorkspaceDialog(None)
        frame2.Show()
        
        print("Hello World")
