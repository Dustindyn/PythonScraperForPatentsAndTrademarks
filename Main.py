import csv
import re
import sys

from selenium.webdriver.firefox.options import Options
from selenium import webdriver

class StartUp:
    def __init__(self, name, domain, category_list, category_group_list, uid):
        self.name = name
        self.domain = domain
        self.category_list = category_list
        self.category_group_list = category_group_list
        self.uid = uid

class errorLog:
    def __init__(self, name, url, exception):
        self.name = name
        self.url = url
        self.exception = exception

startUps = []

with open('data/New Sample_Companies_19h30.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
       startUps.append(StartUp(row[0], row[1], row[2], row[3], row[4]))

del startUps[0]



entries = []
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\User\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
fails = []


for startUp in startUps:
    print('Beginne Bearbeitung für ' + startUp.name)
    searchUrl = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&p=1&f=S&l=50&Query=AN%2F\"" + startUp.name.replace(" ", "+") + "\"&d=PTXT"
    regex = re.compile("http://patft.*" + startUp.name)
    try:
        driver.get(searchUrl)
    except:
        error = errorLog(startUp.name, searchUrl, sys.exc_info()[0])
        fails.append(error)
    elems = driver.find_elements_by_xpath("//a[@href]")

    for elem in elems:
        if regex.fullmatch(elem.get_attribute("href")):
            entry = {
                'Company': startUp.name,
                'Patent Url': elem.get_attribute("href")
            }
            entries.append(entry)

keys = entries[0].keys()
driver.quit()
with open('firstResult(NoFails).csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(entries)
keys = fails[0].keys()
with open('fails.csv', 'w') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(fails)

