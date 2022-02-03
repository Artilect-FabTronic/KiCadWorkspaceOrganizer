from curses import window
import wx
import enum

class WindowsContext():
    def __init__( self, windows ):
        print("test")
        for w in windows:
            wtitle = str(w.GetTitle().encode('utf-8'))
            if (wtitle.__contains__("PCB Editor")) :
                self.pcbEditorWindow = w
        #         #w.EnableFullScreenView(False) #desactive maximize window
        #         w.
            elif (wtitle.__contains__("Schematic Editor")) :
                self.schematicEditorWindow = w
        #         i = i + 20
        #         w.

    def __del__( self ):
        pass

class SplitsTypes(enum.Enum):
    split = 1
    oneToOneToOne = 2
    orga = 3
    twoToOne = 4

class Splits():
    def __init__( self, splitType ):
        wc = WindowsContext(wx.GetTopLevelWindows())

        frame = wx.Frame(None, title ="Display Control Plugin")
        panel = wx.Panel(frame)
        wx.StaticText(panel, label ="Fenêtres ouvertes sur KiCad", pos =(100, 50))
        #frame.Show()
        d = wx.ClientDisplayRect()
        
        s_lsplit = (d[0], d[1], d[2]/2, d[3])
        s_rsplit = (d[0] + (d[2]/2), d[1], (d[2]/2), d[3])

        s_looo = (d[0], d[1], (d[2]/3), d[3])
        s_mooo = (d[0] + (d[2]/3), d[1], (d[2]/3), d[3])
        s_rooo = (d[0] + (d[2]/3) + (d[2]/3) , d[1], (d[2]/3), d[3])

        s_or = (d[0] + (d[2]/3), d[1], (d[2]/2) + (d[2]/2), d[3])
        s_otl = (d[0], d[1], (d[2]/2), d[3]/2)
        s_obl = (d[0], d[1] + (d[3]/2), (d[2]/2), d[3]/2)

        if (splitType == SplitsTypes.split):
            #windowsContext.getPcbEditorWindow.SetSize()
            wc.pcbEditorWindow.SetSize(s_lsplit)
            wc.schematicEditorWindow.SetSize(s_rsplit)


        
    def __del__( self ):
        pass