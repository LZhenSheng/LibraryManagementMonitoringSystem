# coding=utf-8
import sqlite3 as sl
import wx.grid

from bmob.bmob import *

ID_CALC = 300
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import wx

ID_CALC = 300


class SearchResultDialog(wx.Dialog):
    def __init__(self, parent, id):
        super(SearchResultDialog, self).__init__(parent, id, u"图书管理系统", size=(400, 500))

        self.CreateGrid(self)

    def OnCalcClick(self, event):
        self.Close()

    def CreateGrid(self, parent):
        column_names = ["书号", "书名", "借阅时间"]

        self.data = []
        con = sl.connect("user.db")
        data = con.execute("SELECT * FROM USER")
        for row in data:
            self.uid = row[0]
        print self.uid
        b = Bmob("57f90426c26325c00142548619a79b64", "f70e16d5cef5f241737cb6cd311ac762")
        account = b.find(  # 查找数据库
            "BorrowBooks",  # 表名
            BmobQuerier().  # 新建查询逻辑
                addWhereEqualTo("userId", str(self.uid))  # user不存在
        )  # 输出string格式的内容
        # print account.err + str(111)
        if account.err is None:
            print 666
            data2 = json.loads(account.stringData)
            d1 = data2["results"]
            for i, d2 in enumerate(d1):
                books = b.find(
                    "Book",
                    BmobQuerier().
                        addWhereEqualTo("id", d2["bookId"])
                )
                if books.err is None:
                    data3 = json.loads(books.stringData)
                    d4 = data3["results"]
                    for i, d3 in enumerate(d4):
                        print 999
                        self.data.append([d3["id"], d3["name"], d2["time"]])
                        if True:
                            break

        if self.data is not None:

            grid = wx.grid.Grid(parent)
            grid.CreateGrid(len(self.data), len(self.data[0]))
            for r in range(len(self.data)):
                for c in range(len(self.data[r])):
                    grid.SetColLabelValue(c, column_names[c])
                    grid.SetCellValue(r, c, self.data[r][c])
            grid.AutoSize()
            return grid
        return None
