import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://www.nike.com/t/pegasus-40-mens-road-running-shoes-mVJdmS/FQ8723-010").content

soup = BeautifulSoup(r, 'html.parser')

span = soup.find("h1", {"class":"headline-2 css-16cqcdq"})

title = span.text

span = soup.find("div", {"class":"mb3-sm"})

price = span.text

print("The item %s has price %s " % (title, price))