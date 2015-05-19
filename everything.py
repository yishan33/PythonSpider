#!/usr/bin/python
#-*-<coding=UTF-8>-*-

"""
本例为windows下everything程序的linux版本的GUI.后端基于locate实现.
"""

import wx

class GuiMainFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self,parent=None,id=-1,title="",pos=wx.DefaultPosition,size=wx.DefaultSize)
        
        #添加面板.
        panel = wx.Panel(self)
        
        menubar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        fileMenu.Append(-1,"&Open","")
        menubar.Append(fileMenu,"&File")

        #Edit menu
        editMenu = wx.Menu()
        editMenu.Append(-1,"&Copy","")
        menubar.Append(editMenu,"&Edit")

        #Help/About menu
        helpMenu = wx.Menu()
        helpMenu.Append(-1,"About","")
        menubar.Append(helpMenu,"&Help")
        
        #调用SetMenuBar，使其在框架中显示出来
        self.SetMenuBar(menubar)
        
        #在面板中添加文本输入框
        filterInput = wx.TextCtrl(panel,-1,"")
        self.filter = wx.SearchCtrl(panel,style=wx.TE_PROCESS_ENTER)
        self.filter.ShowCanelButton(True)
        self.filter.Bind(wx.EVT_TEXT,self.RefeshText)
        self.filter.Bind(wx.EVT_TEXT_ENTER,self.DoSearch)
        fileType = wx.TextCtrl(panel,-1,"")
        #输出结果显示框
        mutiText = wx.TextCtrl(panel,-1,"",style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        mutiText.SetMinSize((800,600))

        #添加状态栏,是否要加入到sizer中管理.
        statusbar = self.CreateStatusBar()
    
        #管理布局.
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        filterSizer = wx.GridSizer(rows=1,cols=2)
        filterSizer.Add(filterInput,0,wx.EXPAND)
        filterSizer.Add(fileType,0,wx.EXPAND)

        #这句话导致文本框显示有空隙. 为什么不能这样用? menubar是否不需要添加进mainSizer
        #mainSizer.Add(menubar)
        mainSizer.Add(filterSizer,0,wx.EXPAND)
        mainSizer.Add(mutiText,2,wx.EXPAND|wx.ALL)
        #frame中创建的statusbar,不需要添加到sizer中进行管理.
        #mainSizer.Add(statusbar,0,wx.EXPAND)
        
        #这个是关键之处，将sizer与frame关联起来.
        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = GuiMainFrame()
    frame.Show()
    app.MainLoop()