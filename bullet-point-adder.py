#! python3
# bullet-point-adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip as clip

text = clip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)

clip.copy(text)
