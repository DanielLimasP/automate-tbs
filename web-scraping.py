import webbrowser
import requests
import bs4
from selenium import webdriver

# Romeo and Juliet
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))
status_code = res.status_code == requests.codes.ok
print(status_code)
print(len(res.text))
print(res.text[:250])

def everything_else():
    res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))

    res = requests.get('https://nostarch.com')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(type(noStarchSoup))

    example_file = open('example.html')
    example_soup = bs4.BeautifulSoup(example_file.read(), 'html.parser')
    elems = example_soup.select('#author')
    # Oddly enough, elems is not a list, but I suppose
    # that it has some properties akin to them
    print(type(elems))
    print(len(elems))
    print(type(elems[0]))

    for e in elems:
        print(e.getText())
        print(e.attrs)

    # To get attrs from html elements
    soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
    spanElem = soup.select('span')[0]
    print(str(spanElem))
    print(spanElem.attrs)

    # Selenium module
    browser = webdriver.Firefox()
    print(type(browser))
    # Should open a new browser window
    browser.get('https://inventwithpython.com')

    # Clicking with selenium
    browser = webdriver.Firefox()
    browser.get('https://inventwithpython.com')
    linkElem = browser.find_element_by_link_text('Read Online for Free')
    print(type(linkElem))
    linkElem.click() # follows the "Read Online for Free" link

    # submitting forms
    browser = webdriver.Firefox()
    browser.get('https://login.metafilter.com')
    userElem = browser.find_element_by_id('user_name')
    userElem.send_keys('your_real_username_here')
    passwordElem = browser.find_element_by_id('user_pass')
    passwordElem.send_keys('your_real_password_here')
    passwordElem.submit()

def download_img():
    res = requests.get('https://www.freecodecamp.org/news/content/images/size/w2000/2020/06/SVMs.png')
    res.raise_for_status()
    playFile = open('svm.png', 'wb')
    for chunk in res.iter_content(100000):
            playFile.write(chunk)
    playFile.close()

if __name__ == "__main__":
    download_img()
