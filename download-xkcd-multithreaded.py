#! python3
# downloadXkcd.py - Downloads every single XKCD comic. 
import requests, os, bs4
from pathlib import Path
import threading 

# ANSI COLORS:
RED = "\033[0;31m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"

URL = 'https://xkcd.com/'
os.makedirs('xkcd_comics', exist_ok=True)

def download_comics(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        print(CYAN + "Downloading page {}/{}/".format(URL, url_number) + LIGHT_GRAY)
       
        # Dowload current page
        download_url = URL + str(url_number)
        res = requests.get(download_url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
       
        # Now find the URL of the comic image
        comic_elem = soup.select('#comic img')

        if comic_elem == []:
            print(RED + "Couldn't find any comics")
        else:
            comic_url = 'https:' + comic_elem[0].get('src')
            #Now download the image
            print('Downloading image {}'.format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image. Remember that wb = write binary
            image_file = open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)

        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prev_link.get('href')        

    print(GREEN + "Done!" + LIGHT_GRAY)

if __name__ == "__main__":
    download_threads = []

    for i in range(0, 140, 10):
        start = i
        end = i + 9

        if start == 0:
            start = 1

        download_thread = threading .Thread(target=download_comics, args=(start, end))
        download_threads.append(download_thread)
        download_thread.start()

        # Wait for download threads to stop
        for download_thread in download_threads:
            download_thread.join()

        print(GREEN + 'Done' + LIGHT_GRAY)

