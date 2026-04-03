from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("https://www.google.com")   # updated site
time.sleep(2)
search = browser.find_element(By.ID,"APjFqb")
time.sleep(2)
search.send_keys("Nikku Naksha Vala")
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(2)


input("Press Enter to close...")