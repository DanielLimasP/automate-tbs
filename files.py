# Chapter 9: Automate the boring stuff
from pathlib import Path
import my_cats
import pprint
import shelve
import os

if __name__ == "__main__": 
    print(str(Path('bacon', 'eggs', 'bread')))
    
    my_files = ['todo.txt', 'gay.docx', 'homeworkpp.pptx']
    
    for filename in my_files:
        # Raw string
        print(Path(r'C:\Users\danyl', filename))

    # The slash joins paths!
    Path('spam') / 'bacon' / 'eggs'
    Path('spam') / Path('bacon/eggs')  
    homeFolder = Path('C:/Users/Al')
    subFolder = Path('spam')
    homeFolder / subFolder
    print(str(homeFolder / subFolder))
    print(Path.cwd())
    print(Path.home())

    # Creating new dirs with pathlib
    #Path(r'C:\Users\danyl\bitch').mkdir()

    # Absolute and relative paths
    print((Path.cwd().is_absolute()))
    print(os.path.abspath('.'))
    print(Path.home() / Path('my/relative/path'))
    os.path.isabs(os.path.abspath('.'))
    # relpath takes two args. First is the cwd and the second is target rel dir
    os.path.relpath('C:\\Windows', 'C:\\')
    p = Path.cwd()
    # Paths have different parts
    print(p.anchor)
    print(p.parent)
    print(p.name)
    print(p.stem)
    print(p.suffix)
    print(p.drive)

    calc_file_path = 'C:\\Windows\\System32\\calc.exe'
    print(os.path.basename(calc_file_path))
    print(os.path.dirname(calc_file_path))
    print(os.path.split(calc_file_path))
    print(calc_file_path.split(os.sep))

    # Finding File Sizes and Folder Contents
    os.path.getsize('C:\\Windows\\System32\\')
    os.listdir('C:\\Windows')

    p = Path('C:/Users/danyl/Documents')
    # * stands for any char
    p.glob('*')
    print(list(p.glob('*')))
    # Glob returns a generator object that
    # contains the paths of files or dirs 
    # within cwd
    # glob uses some sort of regexp. 
    # This line gets us a list of txt files within docs
    print(list(p.glob('*.txt')))
    # The ? stands for a single char
    print(list(p.glob('project?.docx')))
    # To list any txt or exe file within docs
    print(list(p.glob('*.?x?')))

    # Checking Path Validity
    print(p.exists())
    print(p.is_dir())
    print(p.is_file())

    # Handling files
    p = Path('files/spam.txt')
    p.write_text("This is just spam text")
    print(p.read_text())

    _spam = Path.open(Path.cwd() / 'files' / '_spam.txt')
    print(_spam.read()) 
    
    #print(_spam.readlines())
    for line in _spam.readlines():
        print(line)

    _spam.close()

    bacon_file = open('files/bacon_file.txt', 'w')
    bacon_file.write('Hello bacon\n')
    bacon_file.close()
    bacon_file = open('files/bacon_file.txt', 'a')
    bacon_file.write('Bacon is not a vegetable')
    bacon_file.close()
    bacon_file = open('files/bacon_file.txt')
    content = bacon_file.read()
    bacon_file.close()
    print(content)

    # Saving Variables with the shelve Module
    shelf_file = shelve.open('shelve/mydata')
    cats = ['Cat1', 'Anni', 'Maki', 'Toto']
    shelf_file['cats'] = cats 
    shelf_file.close()

    shelf_file = shelve.open('shelve/mydata')
    print(list(shelf_file.keys()))
    print(list(shelf_file.values()))
    shelf_file.close()

    # Saving variables with the pprint.pformat() function
    pprint.pformat(cats)
    file_obj = open('files/my_cats.py', 'w')
    file_obj.write('cats = ' + pprint.pformat(cats) + '\n')
    file_obj.close()

    file_obj = open('files/my_cats.py', 'r')
    print(file_obj.read())

    print(my_cats.cats)











