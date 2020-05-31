from lxml import html
import requests
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)
# tabela z grami wszechczasów (tylko pierwsza strona !), pobrana za pomocą XPath
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
# można pobierać elementy dokumentu również poprzez funkcje pakietu lxml po id lub klasie
table_div = page.get_element_by_id('collection')

# w dowolnym momencie na elemencie ponownie możemy pobrać elementy przez XPath, najważniejsza jest wiedza o drzewie DOM dokumentu w celu określenia odpowiedniej ścieżki względnej lub bezwzględnej 
# należy pamiętać (lub sprawdzić) to, że zostanie zwrócona lista odnalezionych elementów dokumentu, stąd index [0] aby zwrócić bezpośrednio ten element a nie całą listę
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]

print(table)

# kolejna informacja jest taka, że większość (ale nie wszystkie) nagłówków jest w formie łącza (znacznik <a>), trzeba więc wyłuskać z niego tekst
headers = [label for label in table.xpath('.//th')]
reszta = [label for label in table.xpath('//tr/td')]
del(headers[1])
labels = []
resztas = []
for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
        labels.append(anchor[0].strip())
    else:
        # trzeba pozbyć się znaków niedrukowalnych
        labels.append(header.text.strip())

for element in reszta:
    anchor = element.xpath('.//a/text()')
    if len(anchor) > 0:
        # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
        resztas.append(anchor[0].strip())
    else:
        # trzeba pozbyć się znaków niedrukowalnych
        resztas.append(element.text.strip())
s = np.array(resztas)
x = np.reshape(s, (100,7))
s = np.delete(x, 1, 1)
s = np.delete(s, 5, 1)
c = np.array(labels)
c = np.delete(c, 5)


for x in range(0, np.size(s, 0)):
    anchor = element.xpath('//a/@name')
    s[x][0] = anchor[x]

df = pd.DataFrame(s, columns=c)
df = df.astype({'Num Voters': int})
sortowane = df.sort_values(by='Num Voters', ascending=False)
print(sortowane[0:10])

dane = sortowane[0:10]
wykres = dane['Num Voters'].plot.bar()
wykres.set_xticklabels(dane['Title'])
plt.show()