from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# function to return name of latest file added after clicking on download,so we can close the webdriver
def latest_download_file():
      path = r"C:\\Users\\AJAY_KANDPAL\\Desktop\\microsoft"
      os.chdir(path)
      files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
      newest = files[-1]

      return newest

# URL of website from where to download
website_url = "https://dsssb.delhi.gov.in/dsssb/latest-updates"

# Path to the directory where we want to save the PDF file
download_directory = "C:\\Users\\AJAY_KANDPAL\\Desktop\\microsoft"

# WebDriver for Chrome
chrome_options = webdriver.ChromeOptions()

prefs = { # needed as not to open pdf in browser, but to download instead
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}

chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=chrome_options)

try:
    # Opening the website
    driver.get(website_url)
    time.sleep(5)  # Waiting for page to load

    # Finding the link to the latest PDF and clicking it
    latest_pdf_link = driver.find_element("xpath", "//a[contains(@href, '.pdf')]") # xpath to be passed as argument now
    latest_pdf_link.click()

    # Waiting for the download to complete
    fileends = "crdownload"
    while fileends == "crdownload":
        time.sleep(2)
        newest_file = latest_download_file()
        if "crdownload" in newest_file:
            print(newest_file)
            fileends = "crdownload"
        else:
            fileends = "none"  
finally:
    # Closing the WebDriver
    driver.quit()
