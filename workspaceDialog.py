from ._generatedWorkspaceDialog import MyFrame1
from . import WindowsContext
import logging

class WorkspaceDialog( MyFrame1 ):
	# Virtual event handlers, override them in your derived class
	def SplitAction( self, event ):
		logging.basicConfig(filename="/Users/guigur/log.txt", level=logging.DEBUG)
		logging.debug("split")
		WindowsContext.Splits(WindowsContext.SplitsTypes.split)
		event.Skip()

	def TwoToOneAction( self, event ):
		WindowsContext.Splits(WindowsContext.SplitsTypes.twoToOne)
		event.Skip()

	def OrgaAction( self, event ):
		WindowsContext.Splits(WindowsContext.SplitsTypes.orga)
		event.Skip()

	def OneToOneToOneAction( self, event ):
		WindowsContext.Splits(WindowsContext.SplitsTypes.oneToOneToOne)
		event.Skip()
