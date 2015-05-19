#!user/bin/env python
#coding:utf-8

import wx
import images


class MouseEventFrame(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame with Button', pos = (900, 450), size = (300, 100))
        self.panel = wx.Panel(self)
        
        self.button1 = wx.Button(self.panel, label = 'Not Over', pos = (100, 15))
        self.button2 = wx.Button(self.panel, label = 'seconde', pos = (10, 15))
        self.Bind(wx.EVT_BUTTON, self.OnFrame)
        self.panel.Bind(wx.EVT_BUTTON, self.OnPanel, self.button1)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        
        self.button1.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button1.Bind(wx.EVT_BUTTON, self.OnLeaveWindow)
        
    def OnButtonClick(self, event):
        print ' do onbuttonClick '
        self.panel.SetBackgroundColour('Green') 
        
        self.panel.Refresh()
        event.Skip()
        
    
    def OnEnterWindow(self, event):
        self.button1.SetLabel('Over me!')
        print 'do onenterwindow'
        event.Skip()
        
    def OnLeaveWindow(self, event):
        self.button1.SetLabel('Not Over!!!!')
        print 'do onLeaveWindow' 
        event.Skip()
    
    def OnPanel(self, event):
        self.button2.SetLabel('panle is do')
        print 'do OnPanel'
        event.Skip()
        
    def OnFrame(self, event):
        self.Title = 'just change'
        print 'do Onframe'
        event.Skip()
        
        
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MouseEventFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()















'''class Frame(wx.Frame):
    
    def __init__(self, image, parent = None, id = -1, 
                 pos = wx.DefaultPosition,
                 title = 'Hello.wxPython!'):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent = self, bitmap = temp)
        
class App(wx.App):
    
    def OnInit(self):
        image = wx.Image('wxPython1.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)        
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
def main():
        app = App()
        app.MainLoop()
        
if __name__ == '__main__':
    main()'''
        