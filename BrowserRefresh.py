import sublime_plugin
from subprocess import call


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, args, activate_browser=True, browserName="Google Chrome"):
        if self.view and self.view.is_dirty():
            self.view.run_command("save")
        
        activate = ""
        if(activate_browser == True):
            activate = "activate"

        if(browserName == "Google Chrome"):
            command = """
                tell application "Google Chrome"
                    %s
                    reload active tab of window 1
                end tell
            """ % (activate)

        elif(browserName == "Safari"):
            command = """
                tell application "Safari"
                    %s
                    tell its first document
                        set its URL to (get its URL)
                    end tell
                end tell
            """ % (activate)

        elif(browserName == "Firefox"):
            command = """
                tell application "Firefox"
                    %s
                    tell application "System Events" to keystroke "r" using command down
                end tell
            """ % (activate)

        elif(browserName == "Opera"):
            command = """
                tell application "Opera"
                    %s
                    tell application "System Events" to keystroke "r" using command down
                end tell
            """ % (activate)    

        call(['osascript', '-e', command])

