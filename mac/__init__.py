from subprocess import call


class MacBrowserRefresh:
    def __init__(self, activate_browser, running_browsers):
        if activate_browser:
            self.activate = 'activate'
        else:
            self.activate = ''

        self.browsers = running_browsers

        self._chrome_applescript = """
            tell application "{name}"
                {activate}
                set winref to a reference to (first window whose title does not start with "Developer Tools - ")
                set winref's index to 1
                reload active tab of winref
            end tell
            """

    def _chrome(self, app_name, browser_name):
        command = self._chrome_applescript.format(
            name=app_name, activate=self.activate)

        if browser_name in self.browsers:
            self._call_applescript(command)

    def chrome(self):
        self._chrome("Google Chrome", "chrome")

    def canary(self):
        self._chrome("Google Chrome Canary", "canary")

    def yandex(self):
        self._chrome("Yandex", "yandex")

    def safari(self):
        command = """
            tell application "Safari"
                {activate}
                tell its first document
                    set its URL to (get its URL)
                end tell
            end tell
            """.format(activate=self.activate)

        if 'safari' in self.browsers:
            self._call_applescript(command)

    def webkit(self):
        command = """
            tell application "WebKit"
                {activate}
                tell its first document
                    set its URL to (get its URL)
                end tell
            end tell
            """.format(activate=self.activate)

        if 'webkit' in self.browsers:
            self._call_applescript(command)

    def firefox(self):
        command = """
            tell application "Firefox"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
            """

        if 'firefox' in self.browsers:
            self._call_applescript(command)

    def firefox_dev(self):
        command = """
            tell application "FirefoxDeveloperEdition"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
            """

        if 'firefox-dev' in self.browsers:
            self._call_applescript(command)

    def opera(self):
        command = """
            tell application "Opera"
                activate
                tell application "System Events" to keystroke "r" using command down
            end tell
            """

        if 'opera' in self.browsers:
            self._call_applescript(command)

    def _call_applescript(self, command):
        call(['osascript', '-e', command])
