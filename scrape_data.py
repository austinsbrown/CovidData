#%% import libraries
from selenium import webdriver
from requests import get
import os

#%% get data  !!!(fix closing before download)
tn_url = "https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html"         # default url
driver_path = os.getcwd() + "/chromedriver"                                             # path to chrome driver
download_path = os.getcwd()                                                             # path to download directory

chromeOptions = webdriver.ChromeOptions()                                               # configure chrome
prefs = {"download.default_directory" : download_path}                                  # set download path
chromeOptions.add_experimental_option("prefs",prefs)                                      
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chromeOptions)    # initialize chrome driver

driver.get(tn_url)                                                                      # go to website
xlsx_links = driver.find_elements_by_css_selector("a[href*='XLSX']")                    # get all spreadsheet links
for link in xlsx_links:                                                                 # download everything
    link.click()

driver.quit()                                                                           # close the browser