from curses import window
import wx

class WindowsContext():
    def __init__(self, windows):
        for w in windows:
            wName = w.GetName()
            if (wName.__contains__("PcbFrame")) :
                self.PcbFrame = w
        #         #w.EnableFullScreenView(False) #desactive maximize window
            elif (wName.__contains__("SchematicFrame")) :
                self.SchematicFrame = w

    def __del__( self ):
        pass
