# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FirstFrame
###########################################################################

class FirstFrame( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tool Condition Monitoring System", pos = wx.DefaultPosition, size = wx.Size( 1095,750 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Training_Tab = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter4 = wx.SplitterWindow( self.Training_Tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )

		self.Grapher = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook4 = wx.Notebook( self.Grapher, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Table = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.DataGrid = wx.grid.Grid( self.Table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.DataGrid.CreateGrid( 100, 20 )
		self.DataGrid.EnableEditing( True )
		self.DataGrid.EnableGridLines( True )
		self.DataGrid.EnableDragGridSize( False )
		self.DataGrid.SetMargins( 0, 0 )

		# Columns
		self.DataGrid.EnableDragColMove( False )
		self.DataGrid.EnableDragColSize( True )
		self.DataGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.DataGrid.EnableDragRowSize( True )
		self.DataGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.DataGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.DataGrid, 1, wx.ALL, 5 )


		self.Table.SetSizer( bSizer6 )
		self.Table.Layout()
		bSizer6.Fit( self.Table )
		self.m_notebook4.AddPage( self.Table, u"DataFrame", False )
		self.Plot = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )


		self.Plot.SetSizer( bSizer10 )
		self.Plot.Layout()
		bSizer10.Fit( self.Plot )
		self.m_notebook4.AddPage( self.Plot, u"Distribution Plot", True )

		bSizer4.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )


		self.Grapher.SetSizer( bSizer4 )
		self.Grapher.Layout()
		bSizer4.Fit( self.Grapher )
		self.TrainCtrl = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.ShowDF = wx.Button( self.TrainCtrl, wx.ID_ANY, u"Show Original Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.ShowDF, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1 = wx.StaticText( self.TrainCtrl, wx.ID_ANY, u"Range Filter ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer41.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText2 = wx.StaticText( self.TrainCtrl, wx.ID_ANY, u"Enter Number of Standard Deviations", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer41.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.Span = wx.TextCtrl( self.TrainCtrl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Span, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Filterer = wx.Button( self.TrainCtrl, wx.ID_ANY, u"Create Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Filterer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer41.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ShowFilter = wx.Button( self.TrainCtrl, wx.ID_ANY, u"Show Filtered Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.ShowFilter, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.TrainCtrl, wx.ID_ANY, u"Plot Tools", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer9.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button14 = wx.Button( self.TrainCtrl, wx.ID_ANY, u"Show Original Data Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button15 = wx.Button( self.TrainCtrl, wx.ID_ANY, u"Show Filtered Data Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.TrainCtrl.SetSizer( bSizer41 )
		self.TrainCtrl.Layout()
		bSizer41.Fit( self.TrainCtrl )
		self.m_splitter4.SplitVertically( self.Grapher, self.TrainCtrl, 736 )
		bSizer3.Add( self.m_splitter4, 1, wx.EXPAND, 5 )


		self.Training_Tab.SetSizer( bSizer3 )
		self.Training_Tab.Layout()
		bSizer3.Fit( self.Training_Tab )
		self.m_notebook2.AddPage( self.Training_Tab, u"Training", True )
		self.Model = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook2.AddPage( self.Model, u"Model", False )
		self.Prediction = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook2.AddPage( self.Prediction, u"Prediction", False )

		bSizer2.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.MenuBar = wx.MenuBar( 0 )
		self.FileMenu = wx.Menu()
		self.TrainImport = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Open Training Set", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.Append( self.TrainImport )

		self.MenuBar.Append( self.FileMenu, u"File" )

		self.SetMenuBar( self.MenuBar )


		self.Centre( wx.BOTH )

		# Connect Events
		self.ShowDF.Bind( wx.EVT_BUTTON, self.DisplayDF )
		self.Filterer.Bind( wx.EVT_BUTTON, self.FilterMake )
		self.ShowFilter.Bind( wx.EVT_BUTTON, self.FilterShow )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OGPlotShow )
		self.m_button15.Bind( wx.EVT_BUTTON, self.FilterPlotShow )
		self.Bind( wx.EVT_MENU, self.FilePick, id = self.TrainImport.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def DisplayDF( self, event ):
		event.Skip()

	def FilterMake( self, event ):
		event.Skip()

	def FilterShow( self, event ):
		event.Skip()

	def OGPlotShow( self, event ):
		event.Skip()

	def FilterPlotShow( self, event ):
		event.Skip()

	def FilePick( self, event ):
		event.Skip()

	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 736 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )


