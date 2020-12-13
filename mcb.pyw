#! python3
# Updatable Multi-Clipboard
# mcb.pyw - saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip as pyclip, sys

mcb_shelve = shelve.open('shelve/mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelve[sys.argv[2]] = pyclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyclip.copy(str(list(mcb_shelve.keys())))
    elif sys.argv[1] in mcb_shelve:
        pyclip.copy(mcb_shelve[sys.argv[1]])

mcb_shelve.close()
