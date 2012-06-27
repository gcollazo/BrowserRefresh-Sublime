import sublime_plugin
from subprocess import call


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, args, activate_browser=True, browserName="Google Chrome"):
        if self.view and self.view.is_dirty():
            self.view.run_command("save")

        # ApplicationIsRunnning from, http://vgable.com/blog/2009/04/24/how-to-check-if-an-application-is-running-with-applescript/
        browser_command = """
        on ApplicationIsRunning(appName)
            tell application "System Events" to set appNameIsRunning to exists (processes where name is appName)
            return appNameIsRunning
        end ApplicationIsRunning

        if ApplicationIsRunning("%s")
            tell application "%s" to activate
            tell application "System Events"
                delay .5
                keystroke "r" using {command down}
            end tell
        end if
        """ % (browserName, browserName)

        call(['osascript', '-e', browser_command])
