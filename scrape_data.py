from selenium import webdriver
import os
from time import sleep

if(not os.path.isdir("CSV_FILES")):                                                     # create directory for csv files if one does not exits
    os.mkdir("CSV_FILES")
else:
    os.system("rm CSV_FILES/*")                                                         # if it exists then rm all files

if(not os.path.isdir("PDF_FILES")):                                                     # create directory for pdf files if one does not exits
    os.mkdir("PDF_FILES")

tn_url = "https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html"         # default url
driver_path = os.getcwd() + "/chromedriver"                                             # path to chrome driver
download_path = os.getcwd() + "/CSV_FILES"                                              # path to download directory


chromeOptions = webdriver.ChromeOptions()                                               # configure chrome
chromeOptions.headless = True
prefs = {"download.default_directory" : download_path}                                  # set download path
chromeOptions.add_experimental_option("prefs",prefs)                                      
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chromeOptions)    # initialize chrome driver

driver.get(tn_url)                                                                      # go to website
xlsx_links = driver.find_elements_by_css_selector("a[href*='XLSX']")                    # get all spreadsheet links
for link in xlsx_links:                                                                 # download everything
    link.click()

sleep(30)                                                                               # wait for downloads to complete
driver.quit()                                                                           # close the browser