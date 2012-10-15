import subprocess
import re


def running_browsers():
    ps = check_output(['ps', 'aux'])
    running_browsers = []

    if re.search(r'Google Chrome\.app\/Contents\/MacOS\/Google Chrome', ps) is not None:
        running_browsers.append('chrome')

    if re.search(r'Google Chrome Canary\.app\/Contents\/MacOS\/Google Chrome Canary', ps) is not None:
        running_browsers.append('canary')

    if re.search(r'Firefox\.app', ps) is not None:
        running_browsers.append('firefox')

    if re.search(r'Safari\.app', ps) is not None:
        running_browsers.append('safari')

    if re.search(r'Opera\.app', ps) is not None:
        running_browsers.append('opera')

    return running_browsers if len(running_browsers) > 0 else None


# Got this from http://stackoverflow.com/a/2924457/124852
def check_output(*popenargs, **kwargs):
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(retcode, cmd, output=output)
    return output


class CalledProcessError(Exception):
    def __init__(self, returncode, cmd, output=None):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output

    def __str__(self):
        return "Command '%s' returned non-zero exit status %d" % (
            self.cmd, self.returncode)
# overwrite CalledProcessError due to `output` keyword might be not available
subprocess.CalledProcessError = CalledProcessError


if __name__ == '__main__':
    print running_browsers()
