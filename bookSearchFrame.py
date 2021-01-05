# coding:utf-8
import sys

from dialog.SearchBooksDialog import SearchResultDialog

reload(sys)
sys.setdefaultencoding('utf8')
import wx

ID_CALC = 300


class BookSearchFragment(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title=u'图书管理系统', size=(400, 400), pos=(500, 200))

        self.UpdateUI = UpdateUI
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self, -1)
        global ID_CALC

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.panel.inputMessage = wx.StaticText(self.panel, -1, u'请输入书名', pos=(30, 30), style=wx.ALIGN_CENTER)

        self.panel.calcResult = wx.TextCtrl(self.panel, -1, '', pos=(20, 10), size=(250, 50),
                                            style=wx.TE_MULTILINE | wx.TE_RICH2)

        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.BOLD, underline=False)
        self.panel.calcResult.SetFont(font)

        vbox.Add(self.panel.inputMessage, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.FIXED_MINSIZE, border=5)
        vbox.Add(self.panel.calcResult, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        button_list = [u'搜索', u'退出']
        buttons = []
        for i, button in enumerate(button_list):
            buttons.append((wx.Button(self.panel, ID_CALC, label="{}".format(button), size=(50, 40)), 0, wx.EXPAND))
            self.Bind(wx.EVT_BUTTON, self.OnCalcClick, id=ID_CALC)
            ID_CALC = ID_CALC + 1

        gs = wx.GridSizer(1, 2, 20, 50)
        gs.AddMany(buttons)
        
        vbox.Add(gs, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        self.panel.SetSizer(vbox)

    def OnCalcClick(self, event):
        if event.GetEventObject().GetLabel() == u'退出':
            self.panel.calcResult.SetValue("")
            self.UpdateUI(0)
        elif event.GetEventObject().GetLabel() == u'搜索':
            dlg = SearchResultDialog(None, -1, self.panel.calcResult.GetValue())
            dlg.ShowModal()
            dlg.Destroy()