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
              name='button1', parent=self, pos=wx.Point(312, 232),
              size=wx.Size(144, 24), style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

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
        
        self.textCtrl1.SetValue(u'\nOrder Details\nOrder ID:493\nDate Added:12/12/2013\nPayment Method:Wholesale (add your Purchase Order Number / Drop-ship Address / Special Instruction to the Comments below)\tEmail:scott@techworld.co.nz\nTelephone:1233344\nIP Address:60.234.160.37\n\n\nInstructions\nOrder: TW-4283\n\nAddress:\n\n18 Wallingford road\nTemuka, 7920\n\n\n\nPayment Address\n\nddddddd\n48 Woodman Drive\nTawa\nWellington 5028\nWellington\nNew Zealand\n\n\nProduct\tModel\tQuantity\tPrice\tTotal\nNZXT Switch 810 Hybrid Full Tower Chassis, White\tSWIT810-WT\t1\t$218.70\t$218.70\nSub-Total:\t$218.70\nTotal:\t$218.70\n')
        
        
        

    def OnButton1Button(self, event):
        text = self.textCtrl1.GetValue()
        print [text]
        
        text = text.replace("\n\n", "\n")
        
        i = text.find("Order Details")
        j = text.find("Instructions")
        Order_Details_str = text[i+len("Order Details"):j].strip().replace("\t", "\n")
        
        i = text.find("Instructions")
        j = text.find("Payment Address")
        Instructions_str = text[i+len("Instructions"):j].strip()
        
        i = text.find("Payment Address")
        j = text.find("\nProduct\t")
        Payment_Address_str = text[i+len("Payment Address"):j].strip()
        
        i = text.find("\nProduct\t")
        j = text.find("Sub-Total:")
        Table_str = text[i+1:j]
        i = Table_str.find("\n")
        Table_str = Table_str[i:].strip()
        
        Product_str, Model_str, Quantity_str, Price_str, Total_str = Table_str.split("\t")
        
        i = text.find("Sub-Total:")
        j = text.find("\nTotal:\t")
        Sub_Total_str = text[i+len("Sub-Total:"):j].strip()
        
        i = text.find("\nTotal:\t")
        Total_str = text[i+len("\nTotal:\t"):].strip()
        
        
        print Order_Details_str
        print Instructions_str
        print Payment_Address_str
        print Product_str, Model_str, Quantity_str, Price_str, Total_str 
        print Sub_Total_str
        print Total_str
        
        output = ""
        
        output += "[Order Details]\n"
        output += Order_Details_str
        output += "\n\n"
        
        output += "[Instructions]\n"
        output += Instructions_str
        output += "\n\n"
        
        output += "[Payment Address]\n"
        output += Payment_Address_str
        output += "\n\n"
        
        output += "[Product]\n"
        output += Product_str
        output += "\n\n"
        
        output += "[Model]\n"
        output += Model_str
        output += "\n\n"
        
        output += "[Quantity]\n"
        output += Quantity_str
        output += "\n\n"
        
        output += "[Price]\n"
        output += Price_str
        output += "\n\n"
        
        output += "[Sub_Total]\n"
        output += Sub_Total_str
        output += "\n\n"
        
        output += "[Total]\n"
        output += Total_str
        output += "\n\n"
        
        self.textCtrl2.SetValue(output)
        
        
        
        event.Skip()
        
        
        
        
        
        
        
