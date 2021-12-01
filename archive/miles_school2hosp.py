import csv
from os import replace
from pandas.core.indexes import base
import requests
from bs4 import BeautifulSoup
import urllib

hospital_addresses = []
with open('hospital_addresses.csv') as f:
    csvread =  csv.reader(f, delimiter = ',')
    for row in csvread:
        hospital_addresses.append(row)

print(hospital_addresses)


school_addresses = []
with open('school_addresses.csv') as f:
    csvread = csv.reader(f, delimiter=',')
    for row in csvread:
        school_addresses.append(row)

print(school_addresses)


base_url = 'https://www.mapdevelopers.com/distance_from_to.php?'
for s in school_addresses:
    the_from = '&from=' + s[0].replace(' ', '%20')
    for h in hospital_addresses:
        the_to = '&to=' + h[0].replace(' ', '%20')
        new_url_content = requests.get(base_url + the_from + the_to).text
        # p = BeautifulSoup(new_url.content, 'html.parser')
        # html_content = requests.get(new_url).text
        # print(new_url_content)
        soup = BeautifulSoup(new_url_content, "lxml")
        print('__________')
        print('__________')
        print('__________')
        print('__________')
        print(soup.title.text)

        gdp_table = soup.find("script")
        print(gdp_table)
        break

        # for link in soup.find_all("div"):
        #     print(link)
 




'https://www.mapdevelopers.com/distance_from_to.php?&from=3344%20babcock%20blvd%2015237&to=205%20pinecrest%20dr%2015235'
