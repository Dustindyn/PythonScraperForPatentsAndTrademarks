import csv
import re

from selenium.webdriver.firefox.options import Options
from selenium import webdriver

class StartUp:
    def __init__(self, name, domain, category_list, category_group_list, uid):
        self.name = name
        self.domain = domain
        self.category_list = category_list
        self.category_group_list = category_group_list
        self.uid = uid




listOfStartUps = []

with open('data/New Sample_Companies_19h30.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
       listOfStartUps.append(StartUp(row[0], row[1], row[2], row[3], row[4]))

startUp = listOfStartUps[0]

searchUrl = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&p=1&f=S&l=50&Query=AN%2Fopenx&d=PTXT"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\User\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
driver.get(searchUrl)

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))








