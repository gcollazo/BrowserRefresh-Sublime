# Browser Refresh for Sublime Text

This plugin adds a keyboard shortcut to Sublime Text that will refresh the browser of your choice. Optionally the plugin can "auto save" your current file and bring the desired browser to the foreground.

The default keyboard shortcuts are:

- **⌘ + Shift + R** (Mac)
- **Ctrl + Shift + R** (Windows, Linux)

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
sudo apt-get install xdotool wmctrl
```

### 2. Configure Key Bindings
You need to add the following to your `Key Bindings - User`. Go to `Preferences > Key Bindings - User` and add the following to that file and save. Without this step the plugin will not work.

```json
[
    {
        "keys": ["command+shift+r"], "command": "browser_refresh", "args": {
            "auto_save": true,
            "delay": 0.5,
            "activate": true,
            "browsers" : ["chrome"]
        }
    }
]
```

**auto_save**
If set to `true` you current file in Sublime Text will be saved before refreshing the browser window.

**delay**
Adds a delay (in seconds) before triggering the refresh. Seems to be useful if you are using a CSS or JavaScript pre-processor. The default is 0.0 seconds.

**activate**
If set to `true` when you press the keys it will bring the browser to the foreground. **Note:** On Windows this setting is always `true`.

**browsers**
Specify which browsers to refresh on command. The default is `chrome` which will try to refresh Google Chrome. You can change to be more specific using one of the following:

| Browser                   | Setting      | Platforms       |
|---------------------------|--------------|-----------------|
| Google Chrome             | `chrome`     | Mac, Win, Linux |
| Google Chrome Canary      | `canary`     | Mac, Win        |
| Chromium                  | `chromium    | Linux           |
| Safari                    | `safari`     | Mac, Win        |
| WebKit                    | `webkit`     | Mac             |
| Firefox                   | `firefox`    | Mac, Win, Linux |
| Firefox Developer Edition | `firefoxdev` | Mac             |
| Firefox Nightly           | `nightly`    | Linux           |
| Opera                     | `opera`      | Mac, Win, Linux |
| Internet Explorer         | `ie`         | Win             |
| SRWare Iron               | `iron`       | Win             |
| Yandex                    | `yandex`     | Mac             |
| Pale Moon                 | `palemoon`   | Win,Linux       |
| Konqueror                 | `konqueror`  | Linux           |
| Midori                    | `midori`     | Linux           |
| Qupzilla                  | `qupzilla`   | Linux           |
| Vivaldi                   | `vivaldi`    | Linux           |

**Linux special**

You can optionnally try to send any key on any window with a special browser argument
**"browsers" : ["custom:opera,ctrl+F5"]**

Keep in mind this is only for convenience purpose, it is absolutely not garranteed this method actually works

## Contributions
If you have the time to make this plugin better feel free to fork and submit a pull request.

### Contributors
* [Enrique Ramirez (enriquein)](https://github.com/enriquein)
* [generalov](https://github.com/generalov)
* [Tomáš Votruba (TomasVotruba)](https://github.com/tomasvotruba)

## License
All of Browser Refresh for Sublime Text is licensed under the MIT license.

Copyright (c) 2012 - 2015 Giovanni Collazo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
