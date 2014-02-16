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


"""Translation Test

**What is checked**
This checks for controls which appear not to be translated.

**How is it checked**
It compares the text of the localised and reference controls.

If there are more than string in the control then each item is searched for in
the US list of titles (so checking is not order dependent).
The indices for the untranslated strings are returned in a comma separated
string.
Also the untranslated strings themselves are returned (all as one string).
These strings are not escaped and are delimited as
"string1","string2",..."stringN".

**When is a bug reported**

 If the text of the localised control is identical to the reference control
 (in case, spacing i.e.  a binary compare) then it will be flagged as
 untranslated. Otherwise the control is treated as translated.

Note: This is the method to return the least number of bugs. If there are
differences in any part of the string (e.g. a path or variable name) but the
rest of the string is untranslated then a bug will not be highlighted

**Bug Extra Information**
The bug contains the following extra information
Name	Description
Strings		The list of the untranslated strings as explained above
StringIndices		The list of indices (0 based) that are untranslated.
This will usually be 0 but if there are many strings in the control
untranslated it will report ALL the strings e.g. 0,2,5,19,23

**Is Reference dialog needed**
The reference dialog is always necessary.

**False positive bug reports**
False positive bugs will be reported in the following cases.
-	The title of the control stays the same as the US because the
translation is the same as the English text(e.g. Name: in German)
-	The title of the control is not displayed (and not translated).
This can sometimes happen if the programmer displays something else on the
control after the dialog is created.

**Test Identifier**
The identifier for this test/bug is "Translation" """

__revision__ = "$Revision: 221 $"

testname = "TextChanged"

import re

#-----------------------------------------------------------------------------
def TextChangedTest(windows):
    "Returns just one bug for each control"

    bugs = []
    for win in windows:
        if not win.ref:
            continue

        # get if any items are untranslated
        changedTitles, changedIndices = _GetTranslations(win)

        if changedTitles:
            indicesAsString = ",".join([unicode(idx) for idx in changedIndices])

            bugs.append((
                [win,],
                {
                    "StringIndices": indicesAsString,
                    "Strings": ('"%s"' % '","'.join(changedTitles))
                },
                testname,
                0)
            )


    return bugs

def _GetChangedTexts(win):
    "Find the text items that have changed"
 
    changedTitles = []
    changedIndices = []

    # loop over each of the cleaned loc title
    for index, title in enumerate(win.Texts()):

        # if that title is in the cleaned Ref Titles
        if title not in win.ref.Texts():
            # add this as one of the bugs
            changedTitles.append(title)
            changedIndices.append(index)

    # return all the untranslated titles and thier indices
    return changedTitles, changedIndices


TextChangedTest.TestsMenus = True

