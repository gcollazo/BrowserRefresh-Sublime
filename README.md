# Browser Refresh for Sublime Text 2

After installing this plugin you can hit `command + shift + r` on any window in **Sublime Text 2** and your **Google Chrome** or **Safari** window will come to the foreground *(optional)* and reload the active tab. If the current file is unsaved, it will be saved before the browser is activated and reloaded.

## Settings
All of the settings are in the **Default (OSX).sublime-keymap** file.

```json
[
    {
        "keys": ["command+shift+r"], "command": "browser_refresh", "args": {
            "activate_browser": true,
            "browserName" : "Google Chrome"
        }
    }
]
```

`activate_browser` - If set to `True` when you press the keys it will bring the browser to the foreground.

`browserName` - Specify which browser to use. The default is `Google Chrome` but you can change it to `Safari`,`Firefox` or `Opera`.


## Requirements
Currently it only works on **Mac OS X** with **Google Chrome**, **Safari**, **Firefox** and **Opera**. I don't really plan to extend it for now. If you want to make it better, please feel free to fork and request a pull.

## How to install
**With the Package Control plugin:** The easiest way to install BrowserRefresh is through Package Control, which can be found at [http://wbond.net/sublime_packages/package_control](http://wbond.net/sublime_packages/package_control)

**Without Git:** Download the latest source from GitHub and copy the BrowserRefresh folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

```
git clone git@github.com:gcollazo/BrowserRefresh-Sublime.git
```

## License
All of Browser Refresh for Sublime Text 2 is licensed under the MIT license.

Copyright (c) 2012 Giovanni Collazo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.