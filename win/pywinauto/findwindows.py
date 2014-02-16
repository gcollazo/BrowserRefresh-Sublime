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

"""Provides functions for iterating and finding windows

"""

__revision__ = "$Revision: 689 $"

import re

import ctypes

from . import win32functions
from . import win32structures
from . import handleprops

from . import findbestmatch

from . import controls


# todo: we should filter out invalid windows before returning

#=========================================================================
class WindowNotFoundError(Exception):
    "No window could be found"
    pass

#=========================================================================
class WindowAmbiguousError(Exception):
    "There was more then one window that matched"
    pass



#=========================================================================
def find_window(**kwargs):
    """Call findwindows and ensure that only one window is returned

    Calls find_windows with exactly the same arguments as it is called with
    so please see find_windows for a description of them."""
    windows = find_windows(**kwargs)

    if not windows:
        raise WindowNotFoundError()

    if len(windows) > 1:
        #for w in windows:
        #    print "ambig", handleprops.classname(w), \
        #    handleprops.text(w), handleprops.processid(w)
        exception =  WindowAmbiguousError(
            "There are %d windows that match the criteria %s"% (
            len(windows),
            str(kwargs),
            )
        )

        exception.windows = windows
        raise exception

    return windows[0]

#=========================================================================
def find_windows(class_name = None,
                class_name_re = None,
                parent = None,
                process = None,
                title = None,
                title_re = None,
                top_level_only = True,
                visible_only = True,
                enabled_only = False,
                best_match = None,
                handle = None,
                ctrl_index = None,
                predicate_func = None,
                active_only = False,
                control_id = None,
    ):
    """Find windows based on criteria passed in

    Possible values are:

    * **class_name**  Windows with this window class
    * **class_name_re**  Windows whose class match this regular expression
    * **parent**    Windows that are children of this
    * **process**   Windows running in this process
    * **title**     Windows with this Text
    * **title_re**  Windows whose Text match this regular expression
    * **top_level_only** Top level windows only (default=True)
    * **visible_only**   Visible windows only (default=True)
    * **enabled_only**   Enabled windows only (default=True)
    * **best_match**  Windows with a title similar to this
    * **handle**      The handle of the window to return
    * **ctrl_index**  The index of the child window to return
    * **active_only**  Active windows only (default=False)
    * **control_id**  Windows with this control id
   """

    # allow a handle to be passed in
    # if it is present - just return it
    if handle is not None:
        return [handle, ]

    if top_level_only:
        # find the top level windows
        windows = enum_windows()

        # if we have been given a parent
        if parent:
            windows = [win for win in windows
                if handleprops.parent(win) == parent]

    # looking for child windows
    else:
        # if not given a parent look for all children of the desktop
        if not parent:
            parent = win32functions.GetDesktopWindow()

        # look for all children of that parent
        windows = enum_child_windows(parent)

        # if the ctrl_index has been specified then just return
        # that control
        if ctrl_index is not None:
            return [windows[ctrl_index]]

    if control_id is not None and windows:
        windows = [win for win in windows if
            handleprops.controlid(win) == control_id]
            
    if active_only:
        gui_info = win32structures.GUITHREADINFO()
        gui_info.cbSize = ctypes.sizeof(gui_info)

        # get all the active windows (not just the specified process)
        ret = win32functions.GetGUIThreadInfo(0, ctypes.byref(gui_info))

        if not ret:
            raise ctypes.WinError()

        if gui_info.hwndActive in windows:
            windows = [gui_info.hwndActive]
        else:
            windows = []

    if class_name is not None and windows:
        windows = [win for win in windows
            if class_name == handleprops.classname(win)]

    if class_name_re is not None and windows:
        class_name_regex = re.compile(class_name_re)
        windows = [win for win in windows
            if class_name_regex.match(handleprops.classname(win))]

    if process is not None and windows:
        windows = [win for win in windows
            if handleprops.processid(win) == process]

    if title is not None and windows:
        windows = [win for win in windows
            if title == handleprops.text(win)]

    elif title_re is not None and windows:
        title_regex = re.compile(title_re)
        windows = [win for win in windows
            if title_regex.match(handleprops.text(win))]

    if visible_only and windows:
        windows = [win for win in windows if handleprops.isvisible(win)]

    if enabled_only and windows:
        windows = [win for win in windows if handleprops.isenabled(win)]

    if best_match is not None and windows:
        wrapped_wins = []
        
        for win in windows:
            try:
                wrapped_wins.append(controls.WrapHandle(win))
            except controls.InvalidWindowHandle:
                # skip invalid handles - they have dissapeared 
                # since the list of windows was retrieved
                pass
        windows = findbestmatch.find_best_control_matches(
            best_match, wrapped_wins)
        
        # convert window back to handle
        windows = [win.handle for win in windows]

    if predicate_func is not None and windows:
        windows = [win for win in windows if predicate_func(win)]

    return windows

#=========================================================================
def enum_windows():
    "Return a list of handles of all the top level windows"
    windows = []

    # The callback function that will be called for each HWND
    # all we do is append the wrapped handle
    def EnumWindowProc(hwnd, lparam):
        "Called for each window - adds handles to a list"
        windows.append(hwnd)
        return True

    # define the type of the child procedure
    enum_win_proc = ctypes.WINFUNCTYPE(
        ctypes.c_int, ctypes.c_long, ctypes.c_long)

    # 'construct' the callback with our function
    proc = enum_win_proc(EnumWindowProc)

    # loop over all the children (callback called for each)
    win32functions.EnumWindows(proc, 0)

    # return the collected wrapped windows
    return windows


#=========================================================================
def enum_child_windows(handle):
    "Return a list of handles of the child windows of this handle"

    # this will be filled in the callback function
    child_windows = []

    # callback function for EnumChildWindows
    def EnumChildProc(hwnd, lparam):
        "Called for each child - adds child hwnd to list"

        # append it to our list
        child_windows.append(hwnd)

        # return true to keep going
        return True

    # define the child proc type
    enum_child_proc = ctypes.WINFUNCTYPE(
        ctypes.c_int, 			# return type
        win32structures.HWND, 	# the window handle
        win32structures.LPARAM)	# extra information

    # update the proc to the correct type
    proc = enum_child_proc(EnumChildProc)

    # loop over all the children (callback called for each)
    win32functions.EnumChildWindows(handle, proc, 0)

    return child_windows

