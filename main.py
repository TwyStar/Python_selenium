from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

current_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# PATH = "C:\Program Files (x86)\chromedriver.exe"
site = "https://hardverapro.hu/index.html"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.get(site)
driver.maximize_window()

print(current_dateTime + " Test start")
print(current_dateTime + " Testable site \n" + driver.title)

links = driver.find_elements("xpath",
                             "//a[@href]")
for link in links:
    if "icon-videocard" in link.get_attribute("innerHTML"):
        link.click()
        print(current_dateTime + " Click event Done")
        break

search = driver.find_element(By.NAME, "stext")
if search != 0:
    print(current_dateTime + " Element has found")
else:
    print(current_dateTime + " Element has not found")

searchStatement = "RTX 3070"
search.send_keys(searchStatement)
print(current_dateTime + " search done " + searchStatement)
search.send_keys(Keys.ENTER)
print(current_dateTime + " Key ENTER done")

print(current_dateTime + " Test end")
