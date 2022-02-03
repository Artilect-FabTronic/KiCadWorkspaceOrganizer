# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from curses import window
import wx
import wx.xrc
import os
#import windowsContext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	def __init__( self, parent):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 466,357 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		path = os.path.dirname(__file__)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Split" ), wx.VERTICAL )

		self.m_split = wx.BitmapButton( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_split.SetBitmap( wx.Bitmap( path + "/img/slipt_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer1.Add( self.m_split, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"1:2" ), wx.VERTICAL )

		self.m_2to1 = wx.BitmapButton( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_2to1.SetBitmap( wx.Bitmap( path + "/img/2to1_icon.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer2.Add( self.m_2to1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orga" ), wx.VERTICAL )

		self.m_orga = wx.BitmapButton( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_orga.SetBitmap( wx.Bitmap( path + "/img/orga_icon.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer3.Add( self.m_orga, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"1:1:1" ), wx.VERTICAL )

		self.m_1to1to1 = wx.BitmapButton( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_1to1to1.SetBitmap( wx.Bitmap( path + "/img/1to1to1_icon.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer4.Add( self.m_1to1to1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_split.Bind( wx.EVT_BUTTON, self.SplitAction )
		self.m_2to1.Bind( wx.EVT_BUTTON, self.TwoToOneAction )
		self.m_orga.Bind( wx.EVT_BUTTON, self.OrgaAction )
		self.m_1to1to1.Bind( wx.EVT_BUTTON, self.OneToOneToOneAction )


	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class
	def SplitAction( self, event ):
		windowsContext.Splits(windowsContext.SplitsTypes.split)
		event.Skip()

	def TwoToOneAction( self, event ):
		event.Skip()

	def OrgaAction( self, event ):
		event.Skip()

	def OneToOneToOneAction( self, event ):
		event.Skip()


