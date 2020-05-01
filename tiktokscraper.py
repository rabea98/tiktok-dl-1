from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

# Changed the chrome options to DuckDuckBot or you can also use GoogleBot so that tiktok allows you to stay within it's territory and lets you scrape data
chrome_options = Options()
chrome_options.add_argument('--user-agent=DuckDuckBot')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
start = 1
end = True
# Enter tiktok username here
username = str(input(Enter tiktok username:))
# Enter the number of video here
start = int(input(Enter start:))
end = int(input(Enter end:))
diff = start - end
driver.get('https://www.tiktok.com/@', username)
sleep(2)
videos = []
i = start
# For scrolling to Bottom
SCROLL_PAUSE_TIME = 1  # Pause time after each scroll
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Enter the time taken to scroll I prefer to add 1 second for 7 videos
sleep(diff * 0.7)
while i < end:
    element_to_hover_over = driver.find_element_by_xpath(
        '//*[@id = "main"]/div[2]/div/div[1]/div/main/div[2]/div[' + str(i) + ']/div/div/div/a/div/div/div')
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    sleep(1)
    link = driver.find_element_by_tag_name('video')
    post = link.get_attribute('src')
    urllib.request.urlretrieve(post, 'media' + str(i) + '.mp4')
    sleep(1)
    videos.append(post)
    i = i + 1
