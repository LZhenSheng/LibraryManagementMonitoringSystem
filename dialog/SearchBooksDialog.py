# coding=utf-8
import sqlite3 as sl
import wx.grid

from bmob.bmob import *
from dialog.FailDialog import FailDialog

ID_CALC = 300
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import wx

ID_CALC = 300


class SearchResultDialog(wx.Dialog):
    def __init__(self, parent, id, name):
        super(SearchResultDialog, self).__init__(parent, id, u"图书管理系统", size=(400, 500))
        self.name=name
        self.CreateGrid(self)

    def OnCalcClick(self, event):
        self.Close()

    def CreateGrid(self, parent):
        column_names = ["书号", "书名", "书架位置"]
        self.data = []
        b = Bmob("57f90426c26325c00142548619a79b64", "f70e16d5cef5f241737cb6cd311ac762")
        account = b.find(
            "Book",
        )
        if account.err is None:
            print 666
            data2 = json.loads(account.stringData)
            d1 = data2["results"]
            for i, d2 in enumerate(d1):
                print d2
                print 999
                print d2["name"]
                print self.name
                if self.name in d2["name"]:
                    print 000
                    self.data.append([d2["id"], d2["name"], d2["position"]])

        if len(self.data) != 0:
            print self.data
            # for row in self.data:
            #     self.uid = row[0]
            #     self.uname = row[1]
            grid = wx.grid.Grid(parent)
            grid.CreateGrid(len(self.data), len(self.data[0]))
            for r in range(len(self.data)):
                for c in range(len(self.data[r])):
                    grid.SetColLabelValue(c, column_names[c])
                    grid.SetCellValue(r, c, self.data[r][c])

            grid.AutoSize()
            return grid
        else:
            dlg = FailDialog(None, -1)
            dlg.ShowModal()
            dlg.Destroy()
            self.Destroy()
        return None
