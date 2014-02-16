import os, sys, tempfile
#import SendKeys
#print SendKeys
from SendKeysCtypes import SendKeys
import time

try:
    True
except NameError:
    True,False = 1,0

if __name__ == '__main__':

    # create file game will be saved to
    filename = tempfile.mktemp('.txt')
    print >> sys.stdout, "saving tic-tac-toe game to `%s`" % filename
    f = open(filename,'w')
    f.write('')
    f.close()

    # open notepad
    print "openeing notepad"
    SendKeys("""{LWIN}r{PAUSE 1}Notepad.exe{SPACE}"%(filename)s"{ENTER}{PAUSE 1}"""
        % {'filename': filename.replace('~','{~}')}, 0.05, with_spaces=True,)

    time.sleep(1)
    # draw board
    SendKeys("""\
   |   |  
---+---+---
   |   |  
---+---+---
   |   |  """.replace('+','{+}'),0.05, with_spaces=True, with_newlines=True)

   # play the game
    SendKeys("""\
    ^o{PAUSE 4}
    
    ^{HOME}
    {DOWN 2}{RIGHT 5}+{RIGHT}{PAUSE 1}x
    {LEFT 4}+{LEFT}+o
    {UP 2}{RIGHT 3}+{RIGHT}x
    {DOWN 4}+{LEFT}+(o)
    {LEFT 4}+{LEFT}x
    {RIGHT 7}{UP 4}+{RIGHT}O
    {DOWN 4}+{LEFT}x
    {UP 4}{LEFT 8}+{LEFT}+O
    {RIGHT 7}{DOWN 2}+{RIGHT 1}x
    ^s
    """, 0.5)

    # read game saved from notepad
    f = open(filename)
    output = f.read()
    f.close()

    assert output == """\
 O | x | O
---+---+---
 O | x | x
---+---+---
 x | O | x"""
    print 'Bad news: cat got the game'
    print "Good news: that's what we expected, so the test passed"
