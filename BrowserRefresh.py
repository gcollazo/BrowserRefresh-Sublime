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


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, args, activate=True,
            browsers=['chrome'], auto_save=True, delay=None):

        _os = platform.system()

        # Auto-save
        if auto_save and self.view and self.view.is_dirty():
            self.view.run_command('save')

        # Detect OS and import
        if _os == 'Darwin':
            from mac import MacBrowserRefresh
            refresher = MacBrowserRefresh(activate)
        elif _os == 'Windows':
            from win import WinBrowserRefresh
            refresher = WinBrowserRefresh(activate)
        elif _os == 'Linux':
            from linux import LinuxBrowserRefresh
            refresher = LinuxBrowserRefresh(activate)
        else:
            sublime.error_message('Your operating system is not supported')

        # Delay refresh
        if delay is not None:
            import time
            time.sleep(delay)

        # Actually refresh browsers
        if 'chrome' in browsers:
            refresher.chrome()

        if 'canary' in browsers and _os == 'Darwin':
            refresher.canary()

        if 'yandex' in browsers and _os == 'Darwin':
            refresher.yandex()

        if 'safari' in browsers:
            refresher.safari()

        if 'webkit' in browsers and _os == 'Darwin':
            refresher.webkit()

        if 'firefox' in browsers:
            refresher.firefox()

        if 'firefoxdev' in browsers and _os == 'Darwin':
            refresher.firefox_dev()

        if 'opera' in browsers:
            refresher.opera()

        if 'ie' in browsers and _os == 'Windows':
            refresher.ie()

        if 'iron' in browsers and _os == 'Windows':
            refresher.iron()

        if 'palemoon' in browsers and _os == 'Windows':
            refresher.palemoon()

        if 'brave' in browsers:
            refresher.brave()
