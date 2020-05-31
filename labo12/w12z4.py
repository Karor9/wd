from bs4 import BeautifulSoup
import urllib3
import pandas as pd


url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page=0    "
http = urllib3.PoolManager()
page = http.request("GET", url)
# wyświetla każdy odczytany bajt
print(page.data)
soup = BeautifulSoup(page.data, 'lxml')

tytul = []
platforma = []
data = []
ocena = []

for a in soup.find_all('a'):
    for h3 in a.find_all('h3'):
        tytul.append(h3.text.strip())

for div in soup.find_all('div', {"class": "clamp-details"}):
    i = 0
    for span in div.find_all('span'):
        if i == 0:
            i = i + 1
            continue
        elif i == 1:
            platforma.append(span.text.strip())
            i = i + 1
        else:
            data.append(span.text.strip())
            i = i + 1
i = 0        
for a in soup.find_all('a', {"class": "metascore_anchor"}):
    i = i + 1
    for div in a.find_all('div', {"class": "metascore_w large game positive"}):
        if i % 2 ==  0:
            ocena.append(div.text.strip())
        else:
            continue    

df = pd.DataFrame(list(zip(tytul, platforma, data, ocena)), columns = ["Tytuł", "Platforma", "Data", "Ocena"])
print(df[df['Platforma']=="PC"][0:10])


