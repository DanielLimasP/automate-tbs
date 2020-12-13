import re

# Automate the boring stuff with python
# Chapter 7: Regular expression matching
# Basically we import re, which helps a lot when handling regexp

if __name__ == "__main__":
    # re.compile() -> Pass the pattern to match as a raw string. Returns a regexp object
    phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # search method searches regexp inside a string
    matched_objects = phone_number.search('My phone number 614-555-7812')
    # We obtain the found strings with group
    print('Phone number found: ' + matched_objects.group())

    # bat_regex is split into two groups: Bat and man, mobile, copter and bat
    bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo = bat_regex.search('Batmobile lost a wheel')
    mo.group()
    mo.group(1)

    # Optional matching ()?
    bat_regex = re.compile(r'Bat(wo)?man')
    mo1 = bat_regex.search('The Adventures of Batman')
    print(mo1.group())

    mo2 = bat_regex.search('The Adventures of Batwoman')
    print(mo2.group())

    # Matching one or more with plus sign
    bat_regex = re.compile(r'Bat(wo)+man')
    mol = bat_regex.search('The Adventures of Batwoman')
    print(mol.group())

    mo2 = bat_regex.search('The Adventures of Batwowowowoman')
    print(mo2.group())

    mo3 = bat_regex.search('The Adventures of Batman')
    mo3 == None

    # Matching specific repetitions with brackets
    # 3 is the minimum of repetitions and 5 is the maximum
    ha_regex = re.compile(r'(Ha){3,5}')
    mo1 = ha_regex.search('HaHaHaHa')
    print(mo1.group())

    mo2 = ha_regex.search('Ha')
    mo2 == None

    # Greedy and non-greedy matching
    greedy_ha_regex = re.compile(r'(Ha){3,5}')
    mo1 = greedy_ha_regex.search('HaHaHaHaHa')
    print(mo1.group())

    nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
    mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
    print(mo2.group())

    # The findall() method
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
    print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

    # Character classes
    # \d ---> Any numeric digit from 0 to 9.
    # \D ---> Any character that is not a numeric digit from 0 to 9.
    # \w ---> Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
    # \W ---> Any character that is not a letter, numeric digit, or the underscore character.
    # \s ---> Any space, tab, or newline character. (Think of this as matching “space” characters.)
    # \S ---> Any character that is not a space, tab, or newline.

    xmax_regex = re.compile(r'\d+\s\w+')
    print(xmax_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

    # Making our own character classes
    # You can also include ranges of letters or numbers by using a hyphen. For example, 
    # the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.
    vowel_regex = re.compile(r'[aeiouAEIOU]')
    print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

    consonant_regex = re.compile(r'[^aeiouAEIOU]')
    print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

    # The caret and the dollar sign
    begins_with_hello = re.compile(r'^Hello')
    print(begins_with_hello.search("Hello world"))
    
    ends_with_world = re.compile(r'\d$')
    print(ends_with_world.search("42"))

    # The wildcard character
    at_regex = re.compile(r'.at')
    print(at_regex.findall("The cat in the hat sat on the flat mat."))

    # Matching everything with dot-star
    name_regex = re.compile(r'First name: (.*) Last name: (.*)')
    mo = name_regex.search('First name: Al Last name: Sweigart')
    print(mo.group(1))
    print(mo.group(2))

    non_greedy_regex = re.compile(r'<.*?>')
    mo = non_greedy_regex.search('<To serve man> for dinner.>')
    print(mo.group())

    greedy_regex = re.compile(r'<.*>')
    mo = greedy_regex.search('<To serve man> for dinner.>')
    print(mo.group())

    # Passing re.DOTALL as parameter
    new_line_regex = re.compile('.*', re.DOTALL)
    new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

    # Case sensitive matching: re.I = ignore case
    robocop = re.compile(r'robocop', re.I)
    print(robocop.search('RoboCop is part man, part machine, all cop.').group())

   # You can substitute strings with the sub method
    names_regex = re.compile(r'Agent \w+')
    print(names_regex.sub('CENSORED', 'Agent Alice gave the secrets docs to Agent Robert'))

    # How to manage complex regexp. Add the re.VERBOSE flag
    phone_regex = re.compile(
    r'''(
        (\d{3}|\(\d{3}\))?            # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)                     # separator
        \d{4}                         # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', 
    re.VERBOSE)


