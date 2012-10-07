from pywinauto.application import Application, ProcessNotFoundError
from pywinauto.findwindows import WindowNotFoundError


class WinBrowserRefresh:
    def __init__(self, activate_browser):
        # For now we ignore the activate option
        # we need to find out how to implement
        self.activate = activate_browser

    def chrome(self):
        try:
            app = Application()
            app.connect_(title_re='.*- Google Chrome')
            chrome = app.window_(title_re='.*- Google Chrome')
            chrome.TypeKeys('{F5}')
        except WindowNotFoundError:
            pass

    def safari(self):
        try:
            app = Application()
            app.connect_(path=r'C:\Program Files\Safari\Safari.exe')
            ie = app.top_window_()
            ie.TypeKeys('{F5}')
        except (WindowNotFoundError, ProcessNotFoundError):
            pass

    def firefox(self):
        try:
            app = Application()
            app.connect_(title_re='.*Mozilla Firefox')
            firefox = app.window_(title_re='.*Mozilla Firefox')
            firefox.TypeKeys('{F5}')
        except WindowNotFoundError:
            pass

    def opera(self):
        try:
            app = Application()
            app.connect_(title_re='.*Opera')
            ie = app.window_(title_re='.*Opera')
            ie.TypeKeys('{F5}')
        except WindowNotFoundError:
            pass

    def ie(self):
        try:
            app = Application()
            app.connect_(title_re='.*Internet Explorer')
            ie = app.window_(title_re='.*Internet Explorer')
            ie.TypeKeys('{F5}')
        except WindowNotFoundError:
            pass
