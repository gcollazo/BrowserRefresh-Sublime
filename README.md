# Browser Refresh for Sublime Text 2

After installing this plugin you can hit `command + shift + r` on any window in **Sublime Text 2** and your **Google Chrome** or **Safari** window will come to the foreground *(optional)* and reload the tab with the saved file or open a new one if don't have any(for Safari, only reload the active tab for now). If the current file is unsaved, it will be saved before the browser is activated and reloaded.

## Settings
All of the settings are in the **Default (OSX).sublime-keymap** file.

```json
[
    {
        "keys": ["super+shift+r"], 
        "command": "browser_refresh", 
        "args": {
            "activate_browser": true,
            "browserName" : "Google Chrome"
        }
    }
]
```

`activate_browser` - If set to `True` when you press the keys it will bring the browser to the foreground.

`browserName` - Specify which browser to use. The default is `Google Chrome` but you can change it to `Safari`.


## Requirements
Currently it only works on **Mac OS X** with **Google Chrome** and **Safari**. I don't really plan to extend it for now. If you want to make it better, please feel free to fork and request a pull.

## How to install

**Without Git:** Download the latest source from GitHub and copy the BrowserRefresh folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

```
git clone git@github.com:pumisake/BrowserRefresh-Sublime.git
```

## License
All of Browser Refresh for Sublime Text 2 is licensed under the MIT license.

Copyright (c) 2012 Giovanni Collazo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.