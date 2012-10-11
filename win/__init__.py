from pywinauto.application import Application, ProcessNotFoundError
from pywinauto.findwindows import WindowNotFoundError

import platform

if platform.architecture()[0] == '64bit':
    import ctypes
    import time
    user32 = ctypes.windll.user32

class WinBrowserRefresh:
    def __init__(self, activate_browser):
        # For now we ignore the activate option
        # we need to find out how to implement
        self.is64bit = platform.architecture()[0] == '64bit'
        self.activate = activate_browser

    def chrome(self):
        try:
            app = Application()
            app.connect_(title_re='.*- Google Chrome')
            chrome = app.window_(title_re='.*- Google Chrome')
            chrome.TypeKeys('{F5}')
            if self.is64bit:
                self.TypeKeys64()
        except WindowNotFoundError:
            pass

    def iron(self):
        try:
            app = Application()
            app.connect_(title_re='.*- Iron')
            iron = app.window_(title_re='.*- Iron')
            iron.TypeKeys('{F5}')
            if self.is64bit:
                self.TypeKeys64()
        except WindowNotFoundError:
            pass

    def safari(self):
        try:
            app = Application()
            app.connect_(path=r'C:\Program Files\Safari\Safari.exe') 
            ie = app.top_window_()
            ie.TypeKeys('{F5}')
            if self.is64bit:
                self.TypeKeys64()
        except (WindowNotFoundError, ProcessNotFoundError):
            self.safari64()
            pass

    def safari64(self):
        # Safari can be installed under either Program Files directories when
        # running 64bit Windows. We call this method if the other one errors out.
        try:
            app = Application()
            app.connect_(path=r'C:\Program Files (x86)\Safari\Safari.exe')
            ie = app.top_window_()
            ie.TypeKeys('{F5}')
            if self.is64bit:
                self.TypeKeys64()
        except (WindowNotFoundError, ProcessNotFoundError):
            pass

    def firefox(self):
        try:
            app = Application()
            app.connect_(title_re='.*Mozilla Firefox')
            firefox = app.window_(title_re='.*Mozilla Firefox')
            firefox.TypeKeys('{F5}')
            if self.is64bit:
                self.TypeKeys64()
        except WindowNotFoundError:
            pass

    def opera(self):
        try:
            app = Application()
            app.connect_(title_re='.*Opera')
            ie = app.window_(title_re='.*Opera')
            ie.TypeKeys('{F5}')
            if self.is64bit:
                self.TypeKeys64()
        except WindowNotFoundError:
            pass

    def ie(self):
        try:
            app = Application()
            app.connect_(title_re='.*Internet Explorer')
            ie = app.window_(title_re='.*Internet Explorer')
            ie.TypeKeys('{F5}')
            if self.is64bit:
                self.TypeKeys64()
        except WindowNotFoundError:
            pass

    def TypeKeys64(self):
        # This hack is only necessary when running SublimeText2 64bit.
        # The other method works fine on SublimeText2 32bit, 
        # even when running 64bit Windows. 
        time.sleep(1)
        user32.keybd_event(0x74,0,2,0)  #2 is the code for KEYDOWN
        user32.keybd_event(0x74,0,0,0)  #0 is the code for KEYUP