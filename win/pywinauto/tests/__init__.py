# GUI Application automation and testing library
# Copyright (C) 2006 Mark Mc Mahon
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA

"Package of tests that can be run on controls or lists of controls"

__revision__ = "$Revision: 615 $"


def run_tests(controls, tests_to_run = None, test_visible_only = True):
    "Run the tests"

    # allow either a string or list to be passed
    try:
        tests_to_run = tests_to_run.split()
    except AttributeError:
        pass

    # if no tests specified run them all
    if tests_to_run is None:
        tests_to_run = list(_registered.keys())

    # Filter out hidden controls if requested
    if test_visible_only:
        controls = [ctrl for ctrl in controls if ctrl.IsVisible()]

    bugs = []
    # run each test
    for test_name in tests_to_run:
        #print test_name
        bugs.extend(_registered[test_name](controls))

    return bugs


def get_bug_as_string(bug):
    ctrls, info, bug_type, is_in_ref = bug
    
    header = ["BugType:", str(bug_type), str(is_in_ref)]

    for i in info:
        header.append(str(i))
        header.append(str(info[i]))
    
    lines = []
    lines.append(" ".join(header))
    
    for i, ctrl in enumerate(ctrls):
        lines.append('\t"%s" "%s" (%d %d %d %d) Vis: %d'% (
            ctrl.WindowText(),
            ctrl.FriendlyClassName(),
            ctrl.Rectangle().left,
            ctrl.Rectangle().top,
            ctrl.Rectangle().right,
            ctrl.Rectangle().bottom,
            ctrl.IsVisible(),))
    
    return "\n".join(lines)


def write_bugs(bugs, filename = "BugsOutput.txt"):
    f = open(filename, "w")
    for b in bugs:
        f.write(get_bug_as_string(b).encode('utf-8') + "\n")
        
    f.close()

def print_bugs(bugs):
    "Print the bugs"
    for (ctrls, info, bug_type, is_in_ref) in bugs:
        print("BugType:", bug_type, is_in_ref, end=' ')

        for i in info:
            print(str(i).encode('utf-8'), str(info[i]).encode('utf-8'), end=' ')
        print()


        for i, ctrl in enumerate(ctrls):
            print('\t"%s" "%s" (%d %d %d %d) Vis: %d'% (
                ctrl.WindowText().encode('utf-8'),
                ctrl.FriendlyClassName().encode('utf-8'),
                ctrl.Rectangle().left,
                ctrl.Rectangle().top,
                ctrl.Rectangle().right,
                ctrl.Rectangle().bottom,
                ctrl.IsVisible(),))

            try:
                ctrl.DrawOutline()
            except (AttributeError, KeyError):
                #print e
                pass

        print()


# we need to register the modules
_registered = {}
def __init_tests():
    "Initialize each test by loading it and then register it"
    global _registered

    standard_test_names = (
            "AllControls",
            "AsianHotkey",
            "ComboBoxDroppedHeight",
            "CompareToRefFont",
            "LeadTrailSpaces",
            "MiscValues",
            "Missalignment",
            "MissingExtraString",
            "Overlapping",
            "RepeatedHotkey",
            "Translation",
            "Truncation",
        #   "menux",
    )

    for test_name in standard_test_names:

        test_module = __import__(test_name.lower(), globals(), locals(), [], 1)

        # class name is the test name + "Test"
        test_class = getattr(test_module, test_name + "Test")

        _registered[test_name] = test_class

    # allow extension of the tests available through a separate file
    try:
        import extra_tests
        extra_tests.ModifyRegisteredTests(_registered)
    except ImportError:
        pass


if not _registered:
    __init_tests()

