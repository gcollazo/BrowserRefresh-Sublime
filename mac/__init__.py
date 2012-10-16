from subprocess import call
from utils import running_browsers

browsers = running_browsers()


class MacBrowserRefresh:
    def __init__(self, activate_browser):
        if activate_browser == True:
            self.activate = 'activate'
        else:
            self.activate = ''

    def chrome(self):
        command = """
            tell application "Google Chrome"
                {activate}
                reload active tab of window 1
            end tell
            """.format(activate=self.activate)

        if 'chrome' in browsers:
            self._call_applescript(command)

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
