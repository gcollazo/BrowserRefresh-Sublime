import sublime_plugin
from subprocess import call


class BrowserRefreshCommand(sublime_plugin.WindowCommand):
    def run(self):
        browser_command = """
        tell application "Google Chrome" to tell the active tab of its first window
            reload
        end tell
        tell application "Google Chrome" to activate
        """
        call(['osascript', '-e', browser_command])
