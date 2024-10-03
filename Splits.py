import enum
from .WindowsContext import WindowsContext
import wx

class SplitsTypes(enum.Enum):
	split = 1
	oneToOneToOne = 2
	orga = 3
	twoToOne = 4

class Splits():
	def __init__(self, splitType):
		wc = WindowsContext(wx.GetTopLevelWindows())
		d = wx.ClientDisplayRect()

		s_lsplit = (d[0], 						d[1],			 	d[2]/2,					d[3]	)
		s_rsplit = (d[0] + (d[2]/2), 			d[1], 				d[2]/2, 				d[3]	)

		s_looo = (d[0], 						d[1], 				d[2]/3, 				d[3]	)
		s_mooo = (d[0] + (d[2]/3), 				d[1], 				d[2]/3, 				d[3]	)
		s_rooo = (d[0] + (d[2]/3) + (d[2]/3) , 	d[1], 				d[2]/3, 				d[3]	)

		s_or = (d[0] + (d[2]/3), 				d[1], 				(d[2]/2) + (d[2]/2),	d[3]	)
		s_otl = (d[0], 							d[1], 				d[2]/2, 				d[3]/2	)
		s_obl = (d[0], 							d[1] + (d[3]/2), 	d[2]/2, 				d[3]/2)

		if (splitType == SplitsTypes.split):
			#windowsContext.getPcbEditorWindow.SetSize()
			wc.PcbFrame.SetSize(s_lsplit)
			wc.SchematicFrame.SetSize(s_rsplit)

		elif (splitType == SplitsTypes.oneToOneToOne):
			#windowsContext.getPcbEditorWindow.SetSize()
			wc.PcbFrame.SetSize(s_looo)
			wc.SchematicFrame.SetSize(s_rooo)

		elif (splitType == SplitsTypes.orga):
			#windowsContext.getPcbEditorWindow.SetSize()
			wc.PcbFrame.SetSize(s_otl)
			wc.SchematicFrame.SetSize(s_obl)

		elif (splitType == SplitsTypes.twoToOne):
			#windowsContext.getPcbEditorWindow.SetSize()
			wc.PcbFrame.SetSize(s_lsplit)
			wc.SchematicFrame.SetSize(s_rsplit)

	def __del__(self):
		pass