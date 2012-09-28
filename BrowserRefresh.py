import sublime_plugin
from subprocess import call


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, args, activate_browser=True, browser_name="Google Chrome", auto_save=True):
        if auto_save == True and self.view and self.view.is_dirty():
            self.view.run_command("save")

        self.activate = ""
        if activate_browser == True:
            self.activate = "activate"

        if browser_name == "Google Chrome":
            self._chrome()

        elif browser_name == "Safari":
            self._safari()

        elif browser_name == "Firefox":
            self._firefox()

        elif browser_name == "Opera":
            self._opera()

        elif browser_name == 'all':
            self._chrome()
            self._safari()
            self._firefox()
            self._opera()

    def _chrome(self):
        command = """
            tell application "Google Chrome"
                %s
                reload active tab of window 1
            end tell
        """ % (self.activate)

        self._call_applescript(command)

    def _safari(self):
        command = """
            tell application "Safari"
                %s
                tell its first document
                    set its URL to (get its URL)
                end tell
            end tell
        """ % (self.activate)

        self._call_applescript(command)

    def _firefox(self):
        command = """
            tell application "Firefox"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
        """

        self._call_applescript(command)

    def _opera(self):
        command = """
            tell application "Opera"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
        """

        self._call_applescript(command)

    def _call_applescript(self, command):
        call(['osascript', '-e', command])
