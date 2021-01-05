# coding:utf-8
import os
import signal
import sys

from mfrc522 import MFRC522

from bmob.bmob import *

reload(sys)
sys.setdefaultencoding('utf8')
from picamera import PiCamera
import wx

import RPi.GPIO as GPIO
import time

ID_CALC = 300


class LoginFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='登录界面', size=(400, 400), pos=(500, 200))

        self.UpdateUI = UpdateUI
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self, -1)
        global ID_CALC
        self.Init()
        GPIO.output(11, GPIO.HIGH)
        self.num = 0
        vbox = wx.BoxSizer(wx.VERTICAL)

        button_list = [u'借书', u'还书', u'借阅查询', u'馆藏查询', u'修改密码']
        buttons = []
        for i, button in enumerate(button_list):
            buttons.append((wx.Button(self.panel, ID_CALC, label="{}".format(button), size=(50, 40)), 0, wx.EXPAND))
            self.Bind(wx.EVT_BUTTON, self.OnCalcClick, id=ID_CALC)
            ID_CALC = ID_CALC + 1

        gs = wx.GridSizer(5, 1, 20, 0)
        gs.AddMany(buttons)

        vbox.Add(gs, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)
        self.panel.SetSizer(vbox)

        self.Detct()

    def OnCalcClick(self, event):
        if event.GetEventObject().GetLabel() == u'借书':
            self.UpdateUI(1)
        elif event.GetEventObject().GetLabel() == u'还书':
            self.UpdateUI(3)
        elif event.GetEventObject().GetLabel() == u'借阅查询':
            self.UpdateUI(4)
        elif event.GetEventObject().GetLabel() == u'馆藏查询':
            self.UpdateUI(5)
        elif event.GetEventObject().GetLabel() == u'修改密码':
            self.UpdateUI(6)

    def Init(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.IN)
        GPIO.setup(11, GPIO.OUT)
        pass

    def Beep(self):
        self.num = self.num + 1
        if not os.path.exists('/home/pi/Image/' + str(self.num)):
            os.mkdir('/home/pi/Image/' + str(self.num))
        for i in range(1, 6):
            GPIO.output(11, GPIO.LOW)
            camera = PiCamera()
            camera.rotation = 180
            camera.start_preview()
            camera.capture('/home/pi/Image/' + str(self.num) + '/image%s.jpg' % i)
            camera.stop_preview()
            camera.close()
            GPIO.output(11, GPIO.HIGH)
            time.sleep(0.5)
            print "the Buzzer will make sound"

    def Detct(self):

        while True:
            self.Init()

            if GPIO.input(12):
                for i in range(1, 5):
                    id = self.ReadUserOrBook()
                    if id is not None:

                        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Someone is closing!"
                        self.Beep()

                    else:
                        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Normal"
            else:
                GPIO.output(11, GPIO.HIGH)
                print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Noanybody!"
            time.sleep(1)
        GPIO.output(11, GPIO.HIGH)

        GPIO.cleanup()

    def Comfort(self, id):
        if id >= 100:
            return str(id)
        elif id >= 10:
            return "0" + str(id)
        elif id >= 1:
            return "00" + str(id)
        else:
            return "000"

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
                    id = self.Comfort(uid[0]) + self.Comfort(uid[1]) + self.Comfort(uid[2]) + self.Comfort(uid[3])
                    b = Bmob("57f90426c26325c00142548619a79b64", "f70e16d5cef5f241737cb6cd311ac762")
                    account = b.find(
                        "Book",
                        BmobQuerier().
                            addWhereEqualTo("id", id)
                    )
                    print account.err
                    if account.err is None:
                        data2 = json.loads(account.stringData)
                        d1 = data2["results"]
                        for i, d2 in enumerate(d1):
                            if d2["status"] is True:
                                return id
                            else:
                                return None

                else:
                    print "Authentication error"
        return None
