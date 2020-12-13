#! python3
# downloadXkcd.py - Downloads every single XKCD comic. 
import requests, os, bs4
from pathlib import Path

# ANSI COLORS:
RED = "\033[0;31m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"

url = 'https://xkcd.com'
os.makedirs('xkcd_comics', exist_ok=True)

while not url.endswith('#'):
    # Dowload current page
    print(CYAN + "Downloading page {}".format(url) + LIGHT_GRAY)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Now find the url of the comic image
    comic_elem = soup.select('#comic img')
    
    if comic_elem == []:
        print(RED + "Couldn't find any comics")
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        #Now download the image
        print('Downloading image {}'.format(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

        image_file = open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)

        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prev_link.get('href')        

    print(GREEN + "Done!" + LIGHT_GRAY)