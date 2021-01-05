# coding=utf-8
import wx
import guiManager
from bmob.bmob import *
import sqlite3 as sl


class MainAPP(wx.App):
    def OnInit(self):
        self.manager = guiManager.GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(0)
        self.frame.Show()
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type)
        self.frame.Show(True)

    def CreateUser(self):
        b = Bmob("57f90426c26325c00142548619a79b64", "f70e16d5cef5f241737cb6cd311ac762")
        print b.insert(
            'Account',
            BmobUpdater.increment(
                "count",
                2,
                {
                    "user": "李振生",
                    "password": "123456",
                    "id": "131240142012"
                }
            )
        ).jsonData

    def CreateBook(self):
        b = Bmob("57f90426c26325c00142548619a79b64", "f70e16d5cef5f241737cb6cd311ac762")
        print b.insert(
            'Book',
            BmobUpdater.increment(
                "count",
                2,
                {
                    "id": "041224038179",
                    "name": "第一行代码",
                    "position": "第一架第一行",
                    "author": "周会",
                    "wordFrom": "清华出版社",
                    "price": 43
                }
            )
        ).jsonData

    def CreateSqliteUser(self):
        con = sl.connect("user.db")
        con.execute("DROP TABLE USER")
        with con:
            con.execute("CREATE TABLE USER (id TEXT,name TEXT)")


def main():
    app = MainAPP()
    app.MainLoop()


if __name__ == '__main__':
    main()
