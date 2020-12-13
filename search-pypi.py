#! python3
# searchpypi.py - Opens several search results at pypi.org

import requests, sys, webbrowser, base64

print("Searching...")
res = requests.get("https://google.com/search?q=" "https://pypi.org/search/?q=" + "".join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.package-snippet')

num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = "https://pypi.org" + link_elems[i].get('href')
    print('Openeing', url_to_open)
    webbrowser.open(url_to_open)
