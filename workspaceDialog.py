from ._generatedWorkspaceDialog import MyFrame1
from .Splits import Splits, SplitsTypes

class WorkspaceDialog(MyFrame1):
	# Virtual event handlers, override them in your derived class
	def SplitAction( self, event ):
		# logging.basicConfig(filename="/Users/guigur/log.txt", level=logging.DEBUG)
		# logging.debug("split")
		Splits(SplitsTypes.split)
		event.Skip()

	def TwoToOneAction( self, event ):
		Splits(SplitsTypes.twoToOne)
		event.Skip()

	def OrgaAction( self, event ):
		Splits(SplitsTypes.orga)
		event.Skip()

	def OneToOneToOneAction( self, event ):
		Splits(SplitsTypes.oneToOneToOne)
		event.Skip()
