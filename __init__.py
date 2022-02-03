import pcbnew
import re
import datetime
import wx
import wx.aui
import os
import logging
from . import workspaceDialog 
from . import windowsContext

class KiCadWorkspaceOrganizerPlugin(pcbnew.ActionPlugin):
    def defaults( self ):
        self.name = "KiCad Workspace Organizer"
        self.category = "Tool"
        self.description = "Automaticaly split your screen with pcbnew and the schematic editor"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'img/icon.png') #need to be 32x32
    def Run( self ):
        frame = wx.Frame(None, title ="Display Control Plugin")
        panel = wx.Panel(frame)
        wx.StaticText(panel, label ="Fenêtres ouvertes sur KiCad", pos =(100, 50))
        
        #wx.StaticText(panel, label =str(d[0]), pos =(100, 70))
        #frame.SetSize(10, 10, 300, 300)
        #logging.basicConfig(filename="/Users/guigur/log.txt", level=logging.DEBUG)
        #logging.debug("Debug logging test...")
        
        #board = pcbnew.GetBoard()
        #logging.debug(board)

        #pcb_file_name = board.GetFileName()
        #logging.debug(pcb_file_name)

        wc = windowsContext.WindowsContext(wx.GetTopLevelWindows())
        #windowsContext.Splits(windowsContext.SplitsTypes.split, wc)
        #wx.StaticText(panel, label =str(type(windows)), pos =(100, 100))


        #pcbwin = findPcbnewWindow()
        #top_tb = pcbwin.FindWindowById(6038)
        frame2 = workspaceDialog.MyFrame1(None)
        #frame.Show()
        frame2.Show()



#Application1 = wx.App()
#frame = wx.Frame(None, title ="TUTORIALANDEXAMPLE")
#panel = wx.Panel(frame)
#text1 = wx.StaticText(panel, label ="Hello Python Developers, This is a simple GUI for TutorialandExample!", pos =(100, 50))
#frame.Show()
#Application1.MainLoop()

KiCadWorkspaceOrganizerPlugin().register()