# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 466,357 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Split" ), wx.VERTICAL )

		self.m_split = wx.BitmapButton( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_split.SetBitmap( wx.Bitmap( u"../img/slipt_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer1.Add( self.m_split, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"1:2" ), wx.VERTICAL )

		self.m_TWO_to_ONE = wx.BitmapButton( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_TWO_to_ONE.SetBitmap( wx.Bitmap( u"../img/TWO_to_ONE_icon.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer2.Add( self.m_TWO_to_ONE, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orga" ), wx.VERTICAL )

		self.m_orga = wx.BitmapButton( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_orga.SetBitmap( wx.Bitmap( u"../img/orga_icon.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer3.Add( self.m_orga, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"1:1:1" ), wx.VERTICAL )

		self.m_ONE_to_ONE_to_ONE = wx.BitmapButton( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_ONE_to_ONE_to_ONE.SetBitmap( wx.Bitmap( u"../img/ONE_to_ONE_to_ONE_icon.png", wx.BITMAP_TYPE_ANY ) )
		sbSizer4.Add( self.m_ONE_to_ONE_to_ONE, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer2.Add( sbSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_split.Bind( wx.EVT_LEFT_UP, self.SplitAction )
		self.m_TWO_to_ONE.Bind( wx.EVT_LEFT_UP, self.2to1Action )
		self.m_orga.Bind( wx.EVT_LEFT_UP, self.OrgaAction )
		self.m_ONE_to_ONE_to_ONE.Bind( wx.EVT_LEFT_UP, self.1to1to1Action )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def SplitAction( self, event ):
		event.Skip()

	def 2to1Action( self, event ):
		event.Skip()

	def OrgaAction( self, event ):
		event.Skip()

	def 1to1to1Action( self, event ):
		event.Skip()


