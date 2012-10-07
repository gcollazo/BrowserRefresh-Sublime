from subprocess import call


class MacBrowserRefresh:
    def __init__(self, activate_browser):
        self.activate = activate_browser

    def chrome(self):
        command = """
            tell application "Google Chrome"
                %s
                reload active tab of window 1
            end tell
        """ % (self.activate)

        self._call_applescript(command)

    def safari(self):
        command = """
            tell application "Safari"
                %s
                tell its first document
                    set its URL to (get its URL)
                end tell
            end tell
        """ % (self.activate)

        self._call_applescript(command)

    def firefox(self):
        command = """
            tell application "Firefox"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
        """

        self._call_applescript(command)

    def opera(self):
        command = """
            tell application "Opera"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
        """

        self._call_applescript(command)

    def _call_applescript(self, command):
        call(['osascript', '-e', command])
