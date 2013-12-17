#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(539, 250), size=wx.Size(815, 552),
              style=wx.DEFAULT_FRAME_STYLE, title='OrderExtract')
        self.SetClientSize(wx.Size(799, 514))
        self.SetToolTipString('')
        self.SetBackgroundColour(wx.Colour(254, 249, 231))

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='Extract >>',
              name='button1', parent=self, pos=wx.Point(320, 232),
              size=wx.Size(144, 24), style=0)
        self.button1.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(16, 16), size=wx.Size(768, 208),
              style=wx.TE_MULTILINE, value='')
        self.textCtrl1.SetToolTipString('')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(16, 264), size=wx.Size(768, 232),
              style=wx.TE_MULTILINE, value='')
        self.textCtrl2.SetToolTipString('')

    def __init__(self, parent):
        self._init_ctrls(parent)
