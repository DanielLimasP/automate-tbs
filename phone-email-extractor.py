#! python3

import re
import pyperclip as clip

def pe_extractor():
    phone_regex = re.compile(
        r'''(
            (\d{3}|\(\d{3}\))?                # area code
            (\s|-|\.)?                        # separator
            (\d{3})                           # first 3 digits
            (\s|-|\.)                         # separator
            (\d{4})                           # last 4 digits
            (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', re.VERBOSE)

    email_regex = re.compile(
        r'''(
            [a-zA-Z0-9._%+-]+      # username
            @                      # at symbol
            [a-zA-Z0-9.-]+         # domain name
            (\.[a-zA-Z]{2,4})      # dot-something
        )''', re.VERBOSE)


    clipboard_text = str(clip.paste())

    matches = [] 

    for groups in phone_regex.findall(clipboard_text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != "":
            phone_num += 'x' + groups[8]
        matches.append(phone_num)
    for groups in email_regex.findall(clipboard_text):
        matches.append(groups[0])

    if len(matches) > 0:
        clip.copy('\n'.join(matches))
        print('Copied the results to the clipboard')
        print('\n'.join(matches))
    else:
        print('No matches emails or phones were found')

if __name__ == "__main__":
    pe_extractor()