import sublime
from subprocess import call


class LinuxBrowserRefresh:
    def __init__(self, activate_browser):
        # activate_browser is always true on Windows since you can't
        # send keys to an inactive window programmatically. We ignore it.
        self.activate_browser = activate_browser

    def chrome(self):
        self.SendKeysToAllWindows('google-chrome', 'F5')

    def iron(self):
        pass
        #except NotImplemented("Iron support not implemented yet.")

    def safari(self):
        pass
        #except NotImplemented("Safary support not implemented yet.")

    def safari64(self):
        pass
        #except NotImplemented("Safari64 support not implemented yet.")

    def firefox(self):
        self.SendKeysToAllWindows('firefox', 'F5')

    def opera(self):
        pass
        #except NotImplemented("Opera support not implemented yet.")

    def ie(self):
        pass
        #except NotImplemented("IE support not implemented yet.")

    def SendKeysToAllWindows(self, cls, key):
        "Sends the keystroke to all windows whose title matches the regex"

        cmd = ['xdotool', 'search', '--sync', '--onlyvisible', '--class', cls, 'key', key]

        if self.activate_browser:
            cmd += ['windowactivate']

        status_code = call(cmd)

        if status_code != 0:
            sublime.error_message(
                'Browser Refresh cannot execute the specified program.\n\n'
                '%s\n\n'
                'If program \'xdotool\' is currently not installed '
                'you can install it by typing:\n\n'
                'sudo apt-get install xdotool' % " ".join(cmd))
