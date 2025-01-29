from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service
import json, time

WEBDRIVER_SAFARI_PATH = "/usr/bin/safaridriver"
WEBDRIVER_SETUP_SLEEP_TIME = 5
WEBDRIVER_PAGE_LOAD_SLEEP_TIME = 5


def getData():
    print("Initializing webdriver...")
    browser = webdriver.Safari(service=Service(executable_path=WEBDRIVER_SAFARI_PATH))
    # browser = webdriver.Safari() # same error
    time.sleep(WEBDRIVER_SETUP_SLEEP_TIME)
    # load cookies
    print("Loading cookies...")
    with open("cookies.json", "r") as f:
        cookies = json.load(fp=f)
        for cookie in cookies:
            print(f"Adding cookie \"{cookie['name']}\":\"{cookie['value']}\"")
            browser.add_cookie(cookie_dict=cookie)
    time.sleep(WEBDRIVER_SETUP_SLEEP_TIME)
    browser.get("https://google.com")
    # wait for page to load
    time.sleep(WEBDRIVER_PAGE_LOAD_SLEEP_TIME)
    # Wait for page opening
    browser.close()
    browser.quit()

def main():
    getData()

if __name__ == "__main__":
    main()