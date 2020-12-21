   #! python3
   # add-logo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

   import os
   from pathlib import Path
   from PIL import Image

   SQUARE_FIT_SIZE = 300
   LOGO_FILENAME = Path.cwd / 'img' / 'logo.jpg'

   logo_img = Image.open(LOGO_FILENAME)
   logo_w, logo_h = logo_img.size

   # Loop through dir to find images
   for filename in os.listdir(Path.cwd() / 'img'):
       if not (filename.endswith('.png') or filename.endswith('.jpg') or filename == LOGO_FILENAME):
           continue

        img_file = Image.open(filename)
        w, h = img_file.size

        if w > SQUARE_FIT_SIZE and h > SQUARE_FIT_SIZE:
            if w > h:
                h = int((SQUARE_FIT_SIZE / w) * h)
                w = SQUARE_FIT_SIZE
            else:
                w = int((SQUARE_FIT_SIZE / w) * h)
        
        print('Resizing {}'.format(filename))
        img_file = img_file.resize((w, h))

        print('Adding logo to {}'.format(filename))
        img_file.paste()