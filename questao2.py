from bs4 import BeautifulSoup
import requests

#html = requests.get('http://www.fraiburgo.ifc.edu.br/').content ---- Utilizei como exemplo
html = requests.get('https://stackoverflow.com/').content

bs = BeautifulSoup(html, 'html.parser')
print(bs.find_all('h1'))

h1 = bs.find('span', class_='fl-heading-text')
print(h1)

if not 'h1':
    print('Sem tag h1')
