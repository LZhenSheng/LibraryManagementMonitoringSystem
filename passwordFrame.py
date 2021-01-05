# coding=utf-8
import wx
import sqlite3 as sl
from bmob.bmob import *
import json
import RPi.GPIO as GPIO
import signal

from mfrc522 import MFRC522

from dialog.FailDialog import FailDialog

ID_CALC = 300


class PasswordFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, -1, title=u'图书管理系统', size=(400, 500), pos=(500, 200))

        self.UpdateUI = UpdateUI
        self.InitUI()

    def InitUI(self):

        self.panel = wx.Panel(self, -1)

        global ID_CALC

        self.panel.resultStr = ''

        self.panel.name = wx.StaticText(self.panel, -1, u'姓名:      ', pos=(30, 30), style=wx.ALIGN_CENTER)
        self.panel.id = wx.StaticText(self.panel, -1, u'卡号:               ', pos=(30, 30), style=wx.ALIGN_CENTER)
        self.panel.inputMessage = wx.StaticText(self.panel, -1, u'请输入密码', pos=(30, 30), style=wx.ALIGN_CENTER)

        self.panel.calcResult = wx.TextCtrl(self.panel, -1, '', pos=(20, 10), size=(250, 50),
                                            style=wx.TE_MULTILINE | wx.TE_RICH2)
        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.BOLD, underline=False)
        self.panel.calcResult.SetFont(font)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.panel.name, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.FIXED_MINSIZE, border=5)
        vbox.Add(self.panel.id, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.FIXED_MINSIZE, border=5)
        vbox.Add(self.panel.inputMessage, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.FIXED_MINSIZE, border=5)
        vbox.Add(self.panel.calcResult, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        self.button_list = [u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'退格', u'0', u'清空']

        buttons = []
        for i, button in enumerate(self.button_list):
            buttons.append((wx.Button(self.panel, ID_CALC, label="{}".format(button), size=(50, 40)), 0, wx.EXPAND))
            self.Bind(wx.EVT_BUTTON, self.OnCalcClick, id=ID_CALC)
            ID_CALC = ID_CALC + 1

        gs = wx.GridSizer(4, 3, 5, 5)
        gs.AddMany(buttons)

        vbox.Add(gs, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        button_result = [u'确定', u'退出']

        button_results = []
        for i, button in enumerate(button_result):
            button_results.append(
                (wx.Button(self.panel, ID_CALC, label="{}".format(button), size=(50, 40)), 0, wx.EXPAND))
            self.Bind(wx.EVT_BUTTON, self.OnCalcClick, id=ID_CALC)
            ID_CALC = ID_CALC + 1

        gs = wx.GridSizer(1, 2, 5, 5)
        gs.AddMany(button_results)

        vbox.Add(gs, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(3000, wx.TIMER_CONTINUOUS)
        self.Notify()

        self.panel.SetSizer(vbox)

    def Notify(self):
        id = self.ReadUserOrBook()
        if id != None:
            self.UpdateMessage(id)

    def OnCalcClick(self, event):
        if event.GetEventObject().GetLabel() == u'1':
            self.UpdatePassword(0)
        elif event.GetEventObject().GetLabel() == u'2':
            self.UpdatePassword(1)
        elif event.GetEventObject().GetLabel() == u'3':
            self.UpdatePassword(2)
        elif event.GetEventObject().GetLabel() == u'4':
            self.UpdatePassword(3)
        elif event.GetEventObject().GetLabel() == u'5':
            self.UpdatePassword(4)
        elif event.GetEventObject().GetLabel() == u'6':
            self.UpdatePassword(5)
        elif event.GetEventObject().GetLabel() == u'7':
            self.UpdatePassword(6)
        elif event.GetEventObject().GetLabel() == u'8':
            self.UpdatePassword(7)
        elif event.GetEventObject().GetLabel() == u'9':
            self.UpdatePassword(8)
        elif event.GetEventObject().GetLabel() == u'退格':
            self.Delete()
        elif event.GetEventObject().GetLabel() == u'0':
            self.UpdatePassword(10)
        elif event.GetEventObject().GetLabel() == u'清空':
            self.Clear()
        elif event.GetEventObject().GetLabel() == u'确定':
            self.Detail()
        elif event.GetEventObject().GetLabel() == u'退出':
            self.Exit()

    def GetMText(self):
        return self.panel.calcResult.GetValue()

    def SetMText(self, result):
        self.panel.calcResult.SetValue(result)

    def UpdatePassword(self, index):
        self.SetMText(self.GetMText() + self.button_list[index])

    def Clear(self):
        self.SetMText(u'')

    def Delete(self):
        self.SetMText(self.GetMText()[:-1])

    def Exit(self):
        self.panel.name.SetLabel("姓名:   ")
        self.ClearUI()
        self.UpdateUI(0)

    def Detail(self):

        if len(self.panel.name.GetLabel().strip()) > 4 and self.GetMText() == self.password:
            self.UpdateUI(2)
            self.ClearUI()
        else:
            dlg = FailDialog(None, -1)
            dlg.ShowModal()
            dlg.Destroy()

    def ReadUserOrBook(self):
        continue_reading = True

        def end_read(signal, frame):
            global continue_reading
            print
            "Ctrl+C captured, ending read."
            continue_reading = False
            GPIO.cleanup()

        signal.signal(signal.SIGINT, end_read)

        MIFAREReader = MFRC522()

        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        if status == MIFAREReader.MI_OK:
            print "Card detected"

            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            if status == MIFAREReader.MI_OK:

                print self.Comfort(uid[0]) + self.Comfort(uid[1]) + self.Comfort(uid[2]) + self.Comfort(uid[3])

                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                MIFAREReader.MFRC522_SelectTag(uid)

                status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

                if status == MIFAREReader.MI_OK:
                    MIFAREReader.MFRC522_Read(8)
                    MIFAREReader.MFRC522_StopCrypto1()
                    return self.Comfort(uid[0]) + self.Comfort(uid[1]) + self.Comfort(uid[2]) + self.Comfort(uid[3])
                else:
                    print "Authentication error"
        return None

    def Comfort(self, id):
        if id >= 100:
            return str(id)
        elif id >= 10:
            return "0" + str(id)
        elif id >= 1:
            return "00" + str(id)
        else:
            return "000"

    def UpdateMessage(self, id):

        b = Bmob("57f90426c26325c00142548619a79b64", "f70e16d5cef5f241737cb6cd311ac762")
        account = b.find(
            "Account",
            BmobQuerier().
                addWhereEqualTo("id", id).
        )
        print account.err
        if account.err is None:
            data2 = json.loads(account.stringData)
            d1 = data2["results"]
            for i, d2 in enumerate(d1):
                self.panel.name.SetLabel("姓名:" + d2["user"])
                self.panel.id.SetLabel("卡号:" + d2["id"])
                self.password = d2["password"]
                con = sl.connect("user.db")
                sql = 'INSERT INTO USER (id, name) values(?,?)'
                data = [(buffer(d2["id"]), buffer(d2["user"]))]
                with con:
                    con.executemany(sql, data)

                data1 = con.execute("SELECT * FROM USER")

                for row in data1:
                    print(row)
                print "dlfkj"

    def ClearUI(self):
        self.panel.name.SetLabel("姓名:      ")
        self.panel.id.SetLabel("卡号:               ")
        self.panel.calcResult.SetValue("")