from subprocess import call
from utils import running_browsers

browsers = running_browsers()


class MacBrowserRefresh:
    def __init__(self, activate_browser):
        if activate_browser == True:
            self.activate = 'activate'
        self._chrome_applescript = """
            tell application "{name}"
                {activate}
                reload active tab of window 1
            end tell
            """

    def _chrome(self, app_name, browser_name):
        command = self._chrome_applescript.format(
            name=app_name, activate=self.activate)

        if browser_name in browsers:
            self._call_applescript(command)

    def chrome(self):
        self._chrome("Google Chrome", "chrome")

    def canary(self):
        self._chrome("Google Chrome Canary", "canary")

    def safari(self):
        command = """
            tell application "Safari"
                activate
                tell its first document
                    set its URL to (get its URL)
                end tell
            end tell
            """.format(activate=self.activate)

        if 'safari' in browsers:
            self._call_applescript(command)

    def firefox(self):
        command = """
            tell application "Firefox"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
            """

        if 'firefox' in browsers:
            self._call_applescript(command)

    def opera(self):
        command = """
            tell application "Opera"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
            """

        if 'opera' in browsers:
            self._call_applescript(command)

    def _call_applescript(self, command):
        call(['osascript', '-e', command])
