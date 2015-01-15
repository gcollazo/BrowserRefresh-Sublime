import os
import sys
import platform

import sublime
import sublime_plugin


# Fix windows imports
__file__ = os.path.normpath(os.path.abspath(__file__))
__path__ = os.path.dirname(__file__)

if __path__ not in sys.path:
    sys.path.insert(0, __path__)

_pywinauto = os.path.join(__path__ + os.path.sep + 'win')
if _pywinauto not in sys.path:
    sys.path.insert(0, _pywinauto)

# Cache user operating system
_os = platform.system()


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, args, activate_browser=True,
            browser_name='all', auto_save=True, delay=None):

        # Auto-save
        if auto_save and self.view and self.view.is_dirty():
            self.view.run_command('save')

        # Detect OS and import
        if _os == 'Darwin':
            from mac import MacBrowserRefresh
            from mac.utils import running_browsers
            print(running_browsers())
            refresher = MacBrowserRefresh(activate_browser, running_browsers())
        elif _os == 'Windows':
            from win import WinBrowserRefresh
            refresher = WinBrowserRefresh(activate_browser)
        elif _os == 'Linux':
            from linux import LinuxBrowserRefresh
            refresher = LinuxBrowserRefresh(activate_browser)
        else:
            sublime.error_message('Your operating system is not supported')

        # Delay refresh
        if delay is not None:
            import time
            time.sleep(delay)

        # Actually refresh browsers
        if browser_name == 'Google Chrome':
            refresher.chrome()

        elif browser_name == 'Google Chrome Canary' and _os == 'Darwin':
            refresher.canary()

        elif browser_name == 'yandex' and _os == 'Darwin':
            refresher.yandex()

        elif browser_name == 'Safari':
            refresher.safari()

        elif browser_name == 'WebKit' and _os == 'Darwin':
            refresher.webkit()

        elif browser_name == 'Firefox':
            refresher.firefox()

        elif browser_name == 'Firefox Developer Edition' and _os == 'Darwin':
            refresher.firefox_dev()

        elif browser_name == 'Opera':
            refresher.opera()

        elif browser_name == 'IE' and _os == 'Windows':
            refresher.ie()

        elif browser_name == 'Iron' and _os == 'Windows':
            refresher.iron()

        elif browser_name == 'Pale Moon' and _os == 'Windows':
            refresher.palemoon()

        elif browser_name == 'all':
            refresher.chrome()
            refresher.safari()
            refresher.firefox()
            refresher.opera()

            if _os == 'Darwin':
                refresher.canary()
                refresher.yandex()
                refresher.webkit()
                refresher.firefox_dev()

            if _os == 'Windows':
                refresher.ie()
                refresher.iron()
                refresher.palemoon()
