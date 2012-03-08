import sublime_plugin
from subprocess import call


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, view):
        if self.view and self.view.is_dirty():
            self.view.run_command("save")
        browser_command = """
        tell application "Google Chrome" to tell the active tab of its first window
            reload
        end tell
        tell application "Google Chrome" to activate
        """
        call(['osascript', '-e', browser_command])
