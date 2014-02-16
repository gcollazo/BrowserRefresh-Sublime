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

"""Timing settings for all of pywinauto

This module has one object that should be used for all timing adjustments
  timings.Timings

There are a couple of predefined settings

timings.Timings.Fast()
timings.Timings.Defaults()
timings.Timings.Slow()

The Following are the individual timing settings that can be adjusted:

* window_find_timeout	(default 3)
* window_find_retry (default .09)

* app_start_timeout (default 10)
* app_start_retry   (default .90)

* exists_timeout    (default .5)
* exists_retry  (default .3)

* after_click_wait  (default .09)
* after_clickinput_wait (default .01)

* after_menu_wait   (default .05)

* after_sendkeys_key_wait   (default .01)

* after_button_click_wait   (default 0)

* before_closeclick_wait    (default .1)
* closeclick_retry  (default .05)
* closeclick_dialog_close_wait  (default .05)
* after_closeclick_wait (default .2)

* after_windowclose_timeout (default 2)
* after_windowclose_retry (default .5)

* after_setfocus_wait   (default .06)

* after_setcursorpos_wait   (default .01)

* sendmessagetimeout_timeout   (default .001)

* after_tabselect_wait   (default .01)
* after_listviewselect_wait   (default .01)
* after_listviewcheck_wait  default(.001)

* after_treeviewselect_wait  default(.001)

* after_toobarpressbutton_wait  default(.01)

* after_updownchange_wait  default(.001)

* after_movewindow_wait  default(0)
* after_buttoncheck_wait  default(0)
* after_comboselect_wait  default(0)
* after_listboxselect_wait  default(0)
* after_listboxfocuschange_wait  default(0)
* after_editsetedittext_wait  default(0)
* after_editselect_wait  default(0)

"""

import time
import operator


__revision__ = "$Revision: 453 $"


#=========================================================================
class TimeConfig(object):
    "Central storage and minipulation of timing values"
    __default_timing = {
        'window_find_timeout' : 3,
        'window_find_retry' : .09,

        'app_start_timeout' : 10,
        'app_start_retry' : .90,

        'exists_timeout' : .5,
        'exists_retry' : .3,

        'after_click_wait' : .09,
        'after_clickinput_wait' : .01,

        'after_menu_wait' : .05,

        'after_sendkeys_key_wait' : .01,

        'after_button_click_wait' : 0,

        'before_closeclick_wait' : .1,
        'closeclick_retry' : .05,
        'closeclick_dialog_close_wait' : .05,
        'after_closeclick_wait' : .2,

        'after_windowclose_timeout': 2,
        'after_windowclose_retry':  .5,

        'after_setfocus_wait' : .06,

        'after_setcursorpos_wait' : .01,

        'sendmessagetimeout_timeout' : .001,

        'after_tabselect_wait': .01,

        'after_listviewselect_wait': .01,
        'after_listviewcheck_wait': .001,

        'after_treeviewselect_wait': .001,

        'after_toobarpressbutton_wait': .01,

        'after_updownchange_wait': .001,

        'after_movewindow_wait': 0,
        'after_buttoncheck_wait': 0,
        'after_comboboxselect_wait': 0,
        'after_listboxselect_wait': 0,
        'after_listboxfocuschange_wait': 0,
        'after_editsetedittext_wait': 0,
        'after_editselect_wait': 0,
    }


    _timings = __default_timing.copy()
    _cur_speed = 1

    def __getattr__(self, attr):
        "Get the value for a particular timing"
        if attr in TimeConfig.__default_timing:
            return TimeConfig._timings[attr]
        else:
            raise KeyError(
                "Unknown timing setting: %s" % attr)

    def __setattr__(self, attr, value):
        "Set a particular timing"
        if attr in TimeConfig.__default_timing:
            TimeConfig._timings[attr] = value
        else:
            raise KeyError(
                "Unknown timing setting: %s" % attr)

    def Fast(self):
        """Set fast timing values

        Currently this changes the timing in the following ways:
        timeouts = 1 second
        waits = 0 seconds
        retries = .001 seconds (minimum!)

        (if existing times are faster then keep existing times)
        """

        for setting in TimeConfig.__default_timing:
            # set timeouts to the min of the current speed or 1 second
            if "_timeout" in setting:
                TimeConfig._timings[setting] = \
                    min(1, TimeConfig._timings[setting])

            if "_wait" in setting:
                TimeConfig._timings[setting] = TimeConfig._timings[setting] / 2

            elif setting.endswith("_retry"):
                TimeConfig._timings[setting] = 0.001

            #self._timings['app_start_timeout'] = .5


    def Slow(self):
        """Set slow timing values

        Currently this changes the timing in the following ways:
        timeouts = default timeouts * 10
        waits = default waits * 3
        retries = default retries * 3

        (if existing times are slower then keep existing times)
        """
        for setting in TimeConfig.__default_timing:
            if "_timeout" in setting:
                TimeConfig._timings[setting] = max(
                    TimeConfig.__default_timing[setting] * 10,
                    TimeConfig._timings[setting])

            if "_wait" in setting:
                TimeConfig._timings[setting] = max(
                    TimeConfig.__default_timing[setting] * 3,
                    TimeConfig._timings[setting])

            elif setting.endswith("_retry"):
                TimeConfig._timings[setting] = max(
                    TimeConfig.__default_timing[setting] * 3,
                    TimeConfig._timings[setting])

            if TimeConfig._timings[setting] < .2:
                TimeConfig._timings[setting]= .2

    def Defaults(self):
        "Set all timings to the default time"
        TimeConfig._timings = TimeConfig.__default_timing.copy()


Timings = TimeConfig()


#=========================================================================
class TimeoutError(RuntimeError):
    pass


#=========================================================================
def WaitUntil(
    timeout, 
    retry_interval, 
    func, 
    value = True, 
    op = operator.eq,
    *args):
    
    """Wait until ``op(function(*args), value)`` is True or until timeout 
       expires
    
     * **timeout**  how long the function will try the function
     * **retry_interval**  how long to wait between retries
     * **func** the function that will be executed
     * **value**  the value to be compared against (defaults to True)
     * **op** the comparison function (defaults to equality)\
     * **args** optional arguments to be passed to func when called
     
     Returns the return value of the function
     If the operation times out then the return value of the the function 
     is in the 'function_value' attribute of the raised exception.
     
     e.g. ::
      
      try:
         # wait a maximum of 10.5 seconds for the 
         # the objects ItemCount() method to return 10
         # in increments of .5 of a second
         WaitUntil(10.5, .5, self.ItemCount, 10)
      except TimeoutError, e:
         print "timed out"
     
    """
    
    start = time.time()

    func_val = func(*args)
    # while the function hasn't returned what we are waiting for    
    while not op(func_val, value):
            
        # find out how much of the time is left
        time_left = timeout - ( time.time() - start)
    
        # if we have to wait some more        
        if time_left > 0:
            # wait either the retry_interval or else the amount of
            # time until the timeout expires (whichever is less)
            time.sleep(min(retry_interval, time_left))
            func_val = func(*args)
        else:
            err = TimeoutError("timed out")
            err.function_value = func_val
            raise err
            
    return func_val


#def WaitUntilNot(timeout, retry_interval, func, value = True)
#    return WaitUntil(timeout, retry_interval, func, value = True)
    

def WaitUntilPasses(
    timeout, 
    retry_interval, 
    func, 
    exceptions = (Exception),
    *args):

    """Wait until ``func(*args)`` does not raise one of the exceptions in 
       exceptions
    
     * **timeout**  how long the function will try the function
     * **retry_interval**  how long to wait between retries
     * **func** the function that will be executed
     * **exceptions**  list of exceptions to test against (default: Exception)
     * **args** optional arguments to be passed to func when called
     
     Returns the return value of the function
     If the operation times out then the original exception raised is in
     the 'original_exception' attribute of the raised exception.
     
     e.g. ::
     
      try:
         # wait a maximum of 10.5 seconds for the 
         # window to be found in increments of .5 of a second.
         # P.int a message and re-raise the original exception if never found.
         WaitUntilPasses(10.5, .5, self.Exists, (WindowNotFoundError))
      except TimeoutError, e:
         print "timed out"
         raise e.
     
    """
    
    start = time.time()
    waited = 0

    # keep trying until the timeout is passed
    while True:
        try:
            # Call the function with any arguments
            func_val = func(*args)
            
            # if this did not raise an exception -then we are finised
            break
        
        # An exception was raised - so wait and try again
        except exceptions as e:
        
            # find out how much of the time is left
            time_left = timeout - ( time.time() - start)
        
            # if we have to wait some more        
            if time_left > 0:
                # wait either the retry_interval or else the amount of
                # time until the timeout expires (whichever is less)
                time.sleep(min(retry_interval, time_left))

            else:
                # Raise a TimeoutError - and put the original exception
                # inside it
                err = TimeoutError()
                err.original_exception = e
                raise err
    
    # return the function value
    return func_val


#
#
#
#def Defaults():
#    _current_timing = __default_timing.copy()
#
#
#def Slow():
#    for setting in __default_timing:
#        if "_timeout" in setting:
#            _current_timing[setting] = _default_timing[setting] * 10
#
#        if "_wait" in setting:
#            _current_timing[setting] = _default_timing[setting] * 3
#
#        elif setting.endswith("_retry"):
#            _current_timing[setting] = _default_timing[setting] * 3
#
#
#
#def SetTiming(**kwargs):
#    ""
#
#    for setting, time in kwargs.items():
#        if setting in __default_timing:
#            _current_timing[setting] = time
#        else:
#            raise KeyError(
#                "Unknown timing setting: %s" % setting)
#
#def Get(setting):
#    if setting in __default_timing:
#        return _current_timing[setting]
#    else:
#        raise KeyError(
#            "Unknown timing setting: %s" % setting)
