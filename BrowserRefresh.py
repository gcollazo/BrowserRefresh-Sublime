import sublime
import sublime_plugin
import platform
from utils import import_module


class BrowserRefreshCommand(sublime_plugin.TextCommand):
    def run(self, args, activate_browser=True,
        browser_name="Google Chrome", auto_save=True,
        delay=None):

        # Auto-save
        if auto_save == True and self.view and self.view.is_dirty():
            self.view.run_command("save")

        # Cache Platform
        self.platform = platform.system()

        # Detect OS and import Module
        if self.platform == 'Darwin':
            mod = import_module('mac')
            refresher = mod.MacBrowserRefresh(activate_browser)
        elif self.platform == 'Windows':
            mod = import_module('windows')
            refresher = mod.WinBrowserRefresh(activate_browser)
        else:
            sublime.error_message('Your operating system is not supported')

        # Delay refresh
        if delay is not None:
            import time
            time.sleep(delay)

        # Actually refresh browsers
        if browser_name == "Google Chrome":
            refresher.chrome()

        elif browser_name == "Safari":
            refresher.safari()

        elif browser_name == "Firefox":
            refresher.firefox()

        elif browser_name == "Opera":
            refresher.opera()

        elif browser_name == 'IE' and self.platform == 'Windows':
            refresher.ie()

        elif browser_name == 'all':
            refresher.chrome()
            refresher.safari()
            refresher.firefox()
            refresher.opera()

            if self.platform == 'Windows':
                refresher.ie()
