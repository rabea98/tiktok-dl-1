# tiktok-dl 
[![N|Solid](https://vashukarn.github.io/top-logo.png)](https://vashukarn.github.io/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/vashukarn/tiktok-dl)

## General Information
It is a python automated script that downloads all videos of a particular TikTok user at once.
As we know that web scraping doesn't work with BeautifulSoup for Dynamic pages in which that code go on updating.
So, I used the selenium web browser to scrape videos from TikTok.

## Prerequisites
These should run without any error: <br>
- Selenium Module should be installed <br>
- Chrome webdriver should be installed <br>
- Path of Chrome Browser should be set <br>


```sh
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
```


## Methods we use:
#### Being a dynamic site we have to let load all the data present on the site so we have to scroll to bottom to load all the videos on the page of that particular user
```sh
def scroll(SCROLL_PAUSE_TIME, WAIT):
    print('Started Scrolling..')
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    sleep(WAIT)
    print('Reached to the end of page')
```

#### We download videos using urllib library
```sh
def download_video(url, num_vid):
    urllib.request.urlretrieve(url, 'media' + str(num_vid) + '.mp4')
    print('Media' + str(num_vid) + '.mp4 downloaded.')
```
#### As TikTok provides the video link in the source code of the webpage when we hover the cursor over each post so we use
```sh
def hover(element):
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()
```
#### If you want to go headless just uncomment these two lines
```sh
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
```

## License:
#### MIT
**Free Software, Hell Yeah!**
