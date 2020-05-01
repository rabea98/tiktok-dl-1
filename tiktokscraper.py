from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

# Scrolling


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


# Hovering


def hover(element):
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()
    # This hovers the cursor over the element provided

# Downloading


def download_video(url, num_vid):
    urllib.request.urlretrieve(url, 'media' + str(num_vid) + '.mp4')
    print('Media' + str(num_vid) + '.mp4 downloaded.')
    # This saves the video with the name media1.mp4 and so on.


def main():
    driver.maximize_window()
    driver.get('https://www.tiktok.com/@' + username)
    sleep(2)
    i = start
    # Enter the time taken to scroll I prefer to add 1 second for 7 videos
    scroll(1, diff)
    while i < end+1:
        element_to_hover = driver.find_element_by_xpath(
            '//*[@id = "main"]/div[2]/div/div[1]/div/main/div[2]/div[' + str(i) + ']/div/div/div/a/div/div/div')
        hover(element_to_hover)
        sleep(1)
        link = driver.find_element_by_tag_name('video')
        post = link.get_attribute('src')
        download_video(post, i)
        sleep(1)
        i = i + 1


# Changed the chrome options to DuckDuckBot or you can also use GoogleBot so that tiktok allows you to stay within it's territory and lets you scrape data
chrome_options = Options()
chrome_options.add_argument('--user-agent=DuckDuckBot')

# Uncomment two lines down if you don't want chrome window to popup and go headless
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.minimize_window()
# Enter tiktok username here
username = str(input('Enter tiktok username : '))
# Enter the number of video here
start = int(input('Enter no of first video : '))
end = int(input('Enter no of last video : '))
diff = start - end
main()
print(str(diff) + ' videos of ' + username + ' downloaded successfully. ')
