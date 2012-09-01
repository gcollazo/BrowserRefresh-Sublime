import sublime_plugin
from subprocess import call


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, args, activate_browser=True, browserName="Google Chrome"):
        if self.view and self.view.is_dirty():
            self.view.run_command("save")

        myFilename = "file://localhost" + self.view.file_name()
        print myFilename
        activate = ""
        if(activate_browser == True):
            activate = "activate"

        if(browserName == "Google Chrome"):
            command = """
                tell application "Google Chrome"
                    %s
                    set theUrl to "%s"

                    if (count every window) = 0 then
                        make new window
                    end if

                    set found to false
                    set theTabIndex to -1
                    repeat with theWindow in every window
                        set theTabIndex to 0
                        repeat with theTab in every tab of theWindow
                            set theTabIndex to theTabIndex + 1
                            if theTab's URL = theUrl then
                                set found to true
                                exit
                            end if
                        end repeat

                        if found then
                            exit repeat
                        end if
                    end repeat

                    if found then
                        tell theTab to reload
                        set theWindow's active tab index to theTabIndex
                        set index of theWindow to 1
                    else
                        tell window 1 to make new tab with properties {URL:theUrl}
                    end if
                end tell
            """ % (activate, myFilename)

        elif(browserName == "Safari"):
            command = """
                tell application "Safari"
                    %s
                    tell its first document
                        set its URL to (get its URL)
                    end tell
                end tell
            """ % (activate, myFilename)

        call(['osascript', '-e', command])

