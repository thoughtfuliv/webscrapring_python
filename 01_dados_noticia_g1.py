import requests
from bs4 import BeautifulSoup

#realizando a requisição
response = requests.get('https://g1.globo.com/')

content = response.content

#convertendo para objeto BeautifulSoup

site = BeautifulSoup(content,'html.parser')

# print(site.prettify())

#indicando os parâmetros da pesquisa 

noticia = site.find('div', attrs={'class': 'feed-post-body'})

#indicando os parâmetros do título da notícia
titulo = noticia.find('a',attrs={'class':'feed-post-link'})

#seção da notícia
secao = noticia.find('span',attrs={'class':'feed-post-metadata-section'})

# .text pega apenas o texto daquele trecho de HTML
print('O título desta notícia é:',titulo.text)
print('A seção desta notícia é:',secao.text)
