# Browser Refresh for Sublime Text

After installing this plugin you can hit `command + shift + r` on Mac OS X or `ctrl + shift + r` on Windows while using your favorite browser, the last active window will come to the foreground *(optional in Chrome, Canary, Safari and WebKit on Mac)* and reload the active tab. If the current file is unsaved, it will be saved before the browser is activated and reloaded.

## Settings
To edit settings go to `Preferences > Package Settings > Browser Refresh`

```json
[
    {
        "keys": ["command+shift+r"], "command": "browser_refresh", "args": {
            "auto_save": true,
            "delay": 0.5,
            "activate_browser": true,
            "browser_name" : "Google Chrome"
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
Specify which browser to use. The default is `all` which will try to refresh all running browser on your system. You can change to be more specific: `Google Chrome`, `Google Chrome Canary`, `Safari`, `WebKit`, `Firefox`, `Opera`, `IE`, `Iron`.

**Note**: on Windows use `Google Chrome` if you want to use Canary, because at the moment it's very hard to distinguish between them as both report themselves as Chrome. This also means that if you have both Chrome and Canary running, it will refresh the active tab on both browsers.

## Supported Browsers
- Google Chrome (Mac, Win)
- Google Chrome Canary (Mac, Win - see note above)
- Safari (Mac, Win)
- WebKit (Mac)
- Firefox (Mac, Win)
- Opera (Mac, Win)
- Internet Explorer (Win)
- SRWare Iron (Win)


## How to install
**With the Package Control plugin**  
The easiest way to install **Browser Refresh** is through Package Control, which can be found at [http://wbond.net/sublime_packages/package_control](http://wbond.net/sublime_packages/package_control).

**Without Git**  
Download the latest source from GitHub and copy the BrowserRefresh folder to your Sublime Text "Packages" directory.

**With Git**  
Clone the repository in your Sublime Text "Packages" directory:

```
git clone https://github.com/gcollazo/BrowserRefresh-Sublime.git
```

## Contributions
If you have the time to make this plugin better feel free to fork and submit a pull request. Good pull request will be published to Package Manager within 24hrs.

### Contributors
* [Enrique Ramirez (enriquein)](https://github.com/enriquein)

## License
All of Browser Refresh for Sublime Text 2 is licensed under the MIT license.

Copyright (c) 2012 Giovanni Collazo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.