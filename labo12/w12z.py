from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

# pobieramy wszystkie elementy typu <a> gdzie przodkiem jest <H2> oraz elementem nadrzędnym element o
# klasie "geekcentral_leftcol"2
xpath = '//div[@id="results_1"]//a/href()'

# iterowanie przez odnalezione elementy i wyświetlenie nazw i wartości atrybutów
foundElements = page.xpath(xpath)
print(foundElements)