# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PBO 2", pos = wx.DefaultPosition, size = wx.Size( 561,483 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"HELLO WX" ), wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Haii, aku Muhammad Ahsan Hilmi ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		sbSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"NIM :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"192410101097", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Angkatan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = [ u"2016", u"2017", u"2018", u"2019", u"2020" ]
		self.m_comboBox1 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer6.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Status :" ), wx.VERTICAL )
		
		self.m_radioBtn3 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Mahasiswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Mahasaja", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
		
		self.m_radioBtn5 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Siswasaja", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_radioBtn5, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Save )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizer3.Add( m_sdbSizer1, 1, wx.EXPAND, 1 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

