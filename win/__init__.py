from .pywinauto.application import Application, ProcessNotFoundError
from .pywinauto.findwindows import WindowNotFoundError
from .pywinauto.controls.HwndWrapper import ControlNotVisible

import platform
import time

class WinBrowserRefresh:
    def __init__(self, activate_browser):
        # activate_browser is always true on Windows since you can't
        # send keys to an inactive window programmatically. We ignore it.
        self.activate = activate_browser

    def chrome(self):
        try:
            self.SendKeysToAllWindows('.*- (Google )?Chrome')
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
            safari = app.top_window_()
            safari.TypeKeys('{F5}')
        except (WindowNotFoundError, ProcessNotFoundError):
            self.safari64()
            pass

    def safari64(self):
        # Safari can be installed under either Program Files directories when
        # running 64bit Windows. We call this method if the other one errors out.
        try:
            app = Application()
            app.connect_(path=r'C:\Program Files (x86)\Safari\Safari.exe')
            safari = app.top_window_()
            safari.TypeKeys('{F5}')
        except (WindowNotFoundError, ProcessNotFoundError):
            pass

    def firefox(self):
        try:
            self.SendKeysToAllWindows('.*Mozilla Firefox')
        except WindowNotFoundError:
            pass

    def palemoon(self):
        try:
            self.SendKeysToAllWindows('.*Pale Moon')
        except WindowNotFoundError:
            pass
            
    def opera(self):
        try:
            self.SendKeysToAllWindows('.*Opera')
        except (WindowNotFoundError, ControlNotVisible):
            pass

    def ie(self):
        try:
            self.SendKeysToAllWindows('.*Internet Explorer')
        except WindowNotFoundError:
            pass

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
                processed_handles.append(openwin.handle) 
                time.sleep(1)

