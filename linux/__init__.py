import sublime
from subprocess import call, Popen, PIPE, STDOUT

class LinuxBrowserRefresh:
    def __init__(self, activate_browser):
        self.activate_browser = activate_browser

    def chrome(self):
        # need to force ctrl+F5 here
        self.SendKeyToAllWebkitBasedNavigators('google-chrome', 'ctrl+F5')

    def chromium(self):
        # need to force ctrl+F5 here
        self.SendKeyToAllWebkitBasedNavigators('chromium-browser', 'ctrl+F5')

    def konqueror(self):
        # need to force ctrl+F5 here
        self.SendKeyToAllWebkitBasedNavigators('konqueror', 'ctrl+F5')

    def midori(self):
        self.SendKeyToAllWindows('midori', 'F5')

    def palemoon(self):
        # need to force ctrl+F5 here
        self.SendKeyToAllWindows('pale moon', 'F5')

    def qupzilla(self):
        # need to force ctrl+F5 here
        self.SendKeyToAllWebkitBasedNavigators('qupzilla', 'ctrl+F5')

    def iron(self):
        pass
        # except NotImplemented("Iron support not implemented yet.")

    def safari(self):
        pass
        # except NotImplemented("Safary support not implemented yet.")

    def safari64(self):
        pass
        # except NotImplemented("Safari64 support not implemented yet.")

    def firefox(self):
        self.SendKeysToAllNamedWindows('firefox', 'F5')

    def nightly(self):
        self.SendKeysToAllNamedWindows('nightly', 'F5')

    def vivaldi(self):
        # need to force ctrl+F5 here
        self.SendKeyToAllWebkitBasedNavigators('vivaldi', 'ctrl+F5')

    def opera(self):
        # need to force ctrl+F5 here
        self.SendKeyToAllWebkitBasedNavigators('opera', 'ctrl+F5')

    def ie(self):
        pass
        # except NotImplemented("IE support not implemented yet.")

    def custom(self, customWindow, customCommand):
        customCommand = customCommand if customCommand else 'ctrl+R'
        # Use the safer method
        self.SendKeyToAllWebkitBasedNavigators(customWindow, customCommand)

    def getDesktop(self):
        '''This method is here for compatibilty purpose
        because sometime xdotool would throw
        XGetWindowProperty[_NET_WM_DESKTOP] failed (code=1)'''
        cmd = ['xdotool', 'get_desktop']
        try:
            process = Popen(cmd, stdout=PIPE)
            out, err = process.communicate()
            return out.decode(encoding='UTF-8')
        except Exception:
            self.print_error(cmd)
            return False

    def SendKeyToAllWebkitBasedNavigators(self, cls, key):
        cmd = ['xdotool',   'search',
                            '--desktop', self.getDesktop(),
                            '--onlyvisible',
                            '--class', cls,
                            'windowactivate', 'key', key]

        if self.activate_browser:
            cmd += ['windowactivate']
        else:
            # trick to bring sublime text back to front
            # this avoids the webkit bug where you have
            # to activatewindow before inputing key
            call(['subl'])

        try:
            call(cmd)
        except Exception:
            self.print_error(cmd)

    def SendKeyToAllWindows(self, cls, key):
        cmd = ['xdotool',   'search',
                            '--desktop', self.getDesktop(),
                            '--onlyvisible',
                            '--class', cls,
                            'key', key]

        if self.activate_browser:
            cmd += ['windowactivate']

        try:
            call(cmd)
        except Exception:
            self.print_error(cmd)

    def SendKeysToAllNamedWindows(self, cls, key):
        "Sends the keystroke to all windows whose title matches the regex"

        cmd = ['wmctrl', '-l']
        try:
            process = Popen(cmd, stdout=PIPE)
            out, err = process.communicate()
        except Exception:
            self.print_error(cmd)
            return

        process = Popen(['grep', '-ie',
                        '[-]\?[a-z0-9 ]*%s[a-z0-9 ]*$' % cls],
                        stdout=PIPE, stdin=PIPE)
        process.stdin.write(out)
        out, err = process.communicate()

        wID = ""
        try:
            wID = out.split()[0].decode(encoding='UTF-8')
        except Exception:
            # no window found
            return

        cmd = ['xdotool', 'key', '--window', wID, key]
        try:
            call(cmd)
        except Exception:
            self.print_error(cmd)
            return

        if self.activate_browser:
            cmd = ['xdotool', 'windowactivate', wID]
            try:
                call(cmd)
            except Exception:
                self.print_error(cmd)
                return

    def print_error(prog, cmd):
        sublime.error_message(
            'Browser Refresh cannot execute the specified program.\n\n'
            '%s\n\n'
            'If program \'%s\' is currently not installed '
            'you can install it by typing:\n\n'
            'sudo apt-get install %s' % (' '.join(cmd), cmd[0], cmd[0]))
