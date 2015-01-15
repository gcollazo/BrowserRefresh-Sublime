# Browser Refresh for Sublime Text

After installing this plugin you can hit `command + shift + r` on Mac OS X or `ctrl + shift + r` on Windows and Linux while using your favorite browser, the last active window will come to the foreground *(you can turn this off in Chrome, Canary, Safari, WebKit and Yandex on Mac)* and reload the active tab. If the current file is unsaved, it will be saved before the browser is activated and reloaded.

### 1. Install the package
**With the Package Control plugin**
The easiest way to install **Browser Refresh** is through Package Control, which can be found at [http://wbond.net/sublime_packages/package_control](http://wbond.net/sublime_packages/package_control).

```
Using Package Manager search for "Browser Refresh"
```

**Without Git**
Download the latest source from GitHub and copy the BrowserRefresh folder to your Sublime Text "Packages" directory.

**With Git**
Clone the repository in your Sublime Text "Packages" directory:

```
git clone https://github.com/gcollazo/BrowserRefresh-Sublime.git "Browser Refresh"
```

#### 1.1 On Linux
Install xdotool:

```
sudo apt-get install xdotool
```

### 2. Configure Key Bindings
You need to add the following to your `Key Bindings - User`. Go to `Preferences > Key Bindings - User` and add the following to that file and save. Without this step the plugin will not work.

```json
[
    {
        "keys": ["command+shift+r"], "command": "browser_refresh", "args": {
            "auto_save": true,
            "delay": 0.5,
            "activate_browser": true,
            "browser_name" : "all"
        }
    }
]
```

**auto_save**
If set to `true` you current file in Sublime Text will be save before refreshing the browser window.

**delay**
Adds a delay (in seconds) before triggering the refresh. Seems to be useful if you are using a CSS or JavaScript pre-processor. The default is 0.0 seconds.

**activate_browser**
If set to `true` when you press the keys it will bring the browser to the foreground. **Note:** On Windows this setting is always `true`.

**browser_name**
Specify which browser to use. The default is `all` which will try to refresh all running browser on your system. You can change to be more specific: `Google Chrome`, `Google Chrome Canary`, `Safari`, `WebKit`, `Firefox`, `Firefox Developer Edition`, `Opera`, `IE`, `Iron`, `Yandex`, `Pale Moon`.

**Note**: on Windows use `Google Chrome` if you want to use Canary, because at the moment it's very hard to distinguish between them as both report themselves as Chrome. This also means that if you have both Chrome and Canary running, it will refresh the active tab on both browsers.

## Supported Browsers
- Google Chrome (Mac, Win, Linux)
- Google Chrome Canary (Mac, Win - see note above)
- Safari (Mac, Win)
- WebKit (Mac)
- Firefox (Mac, Win, Linux)
- Firefox Developer Edition (Mac)
- Opera (Mac, Win)
- Internet Explorer (Win)
- SRWare Iron (Win)
- Yandex (Mac)
- Pale Moon (Win)

## Contributions
If you have the time to make this plugin better feel free to fork and submit a pull request.

### Contributors
* [Enrique Ramirez (enriquein)](https://github.com/enriquein)
* [generalov](https://github.com/generalov)
* [Tomáš Votruba (TomasVotruba)](https://github.com/tomasvotruba)

## License
All of Browser Refresh for Sublime Text 2 is licensed under the MIT license.

Copyright (c) 2012 - 2014 Giovanni Collazo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
