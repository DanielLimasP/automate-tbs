from PIL import Image

catIm = Image.open(cwd / 'zophie.png')
catIm.size
width, height = catIm.size
width
height
catIm.filename
catIm.format
catIm.format_description
catIm.save(cwd / 'zophie.jpg')

# Cropping images
catIm = Image.open(cwd / 'zophie.png')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')

# Resize
catIm = Image.open(cwd / 'zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# Rotating
catIm = Image.open(cwd / 'zophie.png')
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')