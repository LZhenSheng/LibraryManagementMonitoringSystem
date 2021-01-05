# coding=utf-8
import loginFrame
import passwordFrame
import borrowBooksFrame
import returnBooksFrame
import borrowBooksHistoryFrame
import bookSearchFrame
import updatePassword


class GuiManager():
    def __init__(self, UpdateUI):
        self.UpdateUI = UpdateUI
        self.frameDict = {}

    def GetFrame(self, type):
        frame = self.frameDict.get(type)
        if frame is None:
            frame = self.CreateFrame(type)
            self.frameDict[type] = frame

        return frame

    def CreateFrame(self, type):
        if type == 0:
            return loginFrame.LoginFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 1:
            return passwordFrame.PasswordFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 2:
            return borrowBooksFrame.BorrowBooksFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 3:
            return returnBooksFrame.ReturnBooksFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 4:
            return borrowBooksHistoryFrame.BorrowBooksHistoryFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 5:
            return bookSearchFrame.BookSearchFragment(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 6:
            return updatePassword.UpdatePassword(parent=None, id=type, UpdateUI=self.UpdateUI)
