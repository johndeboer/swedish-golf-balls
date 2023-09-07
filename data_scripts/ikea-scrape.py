import requests
from bs4 import BeautifulSoup

listingReq = requests.get('https://www.ikea.com/us/en/stores/')
listing = BeautifulSoup(listingReq.text, 'lxml')

link = listing.find('a')
while link.string != 'AZ, Tempe':
    link = link.find_next('a')

while True:
    newUrl = link.get('href')

    r = requests.get(newUrl)
    soup = BeautifulSoup(r.text, 'lxml')

    index = soup.find('h2')
    while index.string != 'Address':
        index = index.find_next('h2')

    index = index.find_next_sibling('p')
    print(index.prettify())

    if link.string == 'WI, Oak Creek':
        break
    link = link.find_next('a')