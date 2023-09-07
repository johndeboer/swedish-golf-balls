import requests
from bs4 import BeautifulSoup

r = requests.get("https://topgolf.com/us/locations-by-state/")
soup = BeautifulSoup(r.text, 'lxml')

index = soup.find('li')
while index.string != 'Birmingham':
    index = index.find_next('li')

while True:
    link = index.find('a')
    print(index.string)  #City Name
    # print(link.get('href')) #Relative link to city page
    newUrl = 'https://topgolf.com' + link.get('href')
    r2 = requests.get(newUrl)
    soup2 = BeautifulSoup(r2.text, 'lxml')

    for index2 in soup2.find_all('span'):
        if(index2.get('itemprop') == 'streetAddress' or index2.get('itemprop') == 'addressLocality' or index2.get('itemprop') == 'addressRegion'):
            print(index2.string)

    print('')

    index = index.find_next('li')
    if index.string == 'Essex (Chigwell)':
        break

