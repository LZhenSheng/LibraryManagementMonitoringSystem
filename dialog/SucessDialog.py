# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import wx
ID_CALC = 300

class SucessDialog(wx.Dialog):
    def __init__(self, parent, id):
        super(SucessDialog, self).__init__(parent, id, u"图书管理系统", size=(300, 150))

        self.panel = wx.Panel(self, -1)
        global ID_CALC

        vbox = wx.BoxSizer(wx.VERTICAL)

        result = [u'成功', u'OK']
        results = []

        self.panel.name = wx.StaticText(self.panel, -1, result[0], pos=(30, 30), style=wx.ALIGN_CENTER)
        vbox.Add(self.panel.name, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.FIXED_MINSIZE, border=5)

        results.append((wx.Button(self.panel, ID_CALC, label=result[1], size=(50, 40)), 0, wx.EXPAND))
        self.Bind(wx.EVT_BUTTON, self.OnCalcClick, id=ID_CALC)

        gs = wx.GridSizer(1, 1, 20, 50)
        gs.AddMany(results)

        vbox.Add(gs, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        self.panel.SetSizer(vbox)

    def OnCalcClick(self, event):
        self.Close()