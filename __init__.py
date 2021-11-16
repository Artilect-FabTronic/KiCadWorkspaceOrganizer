import pcbnew
import re
import datetime
import wx
import wx.aui
import os
import logging

class KiCadWorkspaceOrganizerPlugin(pcbnew.ActionPlugin):
    def defaults( self ):
        self.name = "KiCad Workspace Organizer"
        self.category = "Tool"
        self.description = "Automaticaly split your screen with pcbnew and the schematic editor"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') #need to be 32x32
    def Run( self ):
        #frame = wx.Frame(None, title ="Display Control Plugin")
        #panel = wx.Panel(frame)
        #wx.StaticText(panel, label ="Fenêtres ouvertes sur kicad", pos =(100, 50))
        d = wx.ClientDisplayRect()
        #wx.StaticText(panel, label =str(d[0]), pos =(100, 70))
        #frame.SetSize(10, 10, 300, 300)
        #logging.basicConfig(filename="/Users/guigur/log.txt", level=logging.DEBUG)
        #logging.debug("Debug logging test...")
        
        #board = pcbnew.GetBoard()
        #logging.debug(board)

        #pcb_file_name = board.GetFileName()
        #logging.debug(pcb_file_name)

        windows = wx.GetTopLevelWindows()
        #logging.debug("===== WINDOWS =====")
        i = 90
        for w in windows:
            wtitle = str(w.GetTitle().encode('utf-8'))
            #wx.StaticText(panel, label =wtitle, pos =(100, i))
            i = i + 20
            if (wtitle.__contains__("PCB Editor")) :
                #logging.debug("yes")
                #wx.StaticText(panel, label ="oui !", pos =(100, i))
                i = i + 20
                #w.EnableFullScreenView(False) #desactive maximize window
                w.SetSize(d[0], d[1], d[2]/2, d[3])
            if (wtitle.__contains__("Schematic Editor")) :
                i = i + 20
                w.SetSize(d[0]+(d[2]/2), d[1], d[2]/2, d[3])

        #logging.debug("=== END WINDOWS ===")

        #pcbwin = findPcbnewWindow()
        #top_tb = pcbwin.FindWindowById(6038)
        #frame.Show()


def findPcbnewWindow():
    
    windows = wx.GetTopLevelWindows()
    pcbnew = [w for w in windows if w.GetTitle() == "Pcbnew"]

    if len(pcbnew) != 1:
        raise Exception("Cannot find pcbnew window from title matching!")
    return pcbnew[0]


#Application1 = wx.App()
#frame = wx.Frame(None, title ="TUTORIALANDEXAMPLE")
#panel = wx.Panel(frame)
#text1 = wx.StaticText(panel, label ="Hello Python Developers, This is a simple GUI for TutorialandExample!", pos =(100, 50))
#frame.Show()
#Application1.MainLoop()

KiCadWorkspaceOrganizerPlugin().register()