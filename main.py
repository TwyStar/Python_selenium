from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)

current_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


PATH = "C:\Program Files (x86)\chromedriver.exe"
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

print(current_dateTime + " Test end")


