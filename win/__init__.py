from pywinauto.application import Application, ProcessNotFoundError
from pywinauto.findwindows import WindowNotFoundError

import platform
import time

if platform.architecture()[0] == '64bit':
    import ctypes
    user32 = ctypes.windll.user32

class WinBrowserRefresh:
    def __init__(self, activate_browser):
        # For now we ignore the activate option
        # we need to find out how to implement
        self.is64bit = platform.architecture()[0] == '64bit'
        self.activate = activate_browser

    def chrome(self):
        try:
            self.SendKeysToAllWindows('.*- Google Chrome')
        except WindowNotFoundError:
            pass

    def iron(self):
        try:
            self.SendKeysToAllWindows('.*- Iron')
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
            self.SendKeysToAllWindows('.*Mozilla Firefox')
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
            self.SendKeysToAllWindows('.*Internet Explorer')
        except WindowNotFoundError:
            pass

    def TypeKeys64(self):
        # This hack is only necessary when running SublimeText2 64bit.
        # The other method works fine on SublimeText2 32bit,
        # even when running 64bit Windows.
        time.sleep(1)
        user32.keybd_event(0x74, 0, 2, 0)  # 2 is the code for KEYDOWN
        user32.keybd_event(0x74, 0, 0, 0)  # 0 is the code for KEYUP

    def SendKeysToAllWindows(self, title_regex):
        "Sends the keystroke to all windows whose title matches the regex"

        # We need to call find_windows on our own because Application.connect_ will
        # call find_window and throw if it finds more than one match.
        all_matches = pywinauto.findwindows.find_windows(title_re = title_regex)

        # We need to store all window handles that have been sent keys in order
        # to avoid reactivating windows and doing unnecesary refreshes. This is a
        # side effect of having to call Application.connect_ on each regex match.
        # We need to loop through each open window collection to support edge 
        # cases like Google Canary where the Window title is identical to Chrome.
        processed_handles = []
        
        for win in all_matches:
            app = Application()
            app.connect_(handle = win)
            open_windows = app.windows_(title_re = title_regex)

            for openwin in open_windows:
                if openwin.handle in processed_handles:
                    continue

                openwin.TypeKeys('{F5}')
                time.sleep(1)
                if self.is64bit:
                    self.TypeKeys64()

                processed_handles.append(openwin.handle)

