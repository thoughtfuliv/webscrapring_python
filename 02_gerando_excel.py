import requests
from bs4 import BeautifulSoup
import pandas as pd


#realizando a requisição
response = requests.get('https://g1.globo.com/')

content = response.content

#convertendo para objeto BeautifulSoup

site = BeautifulSoup(content,'html.parser')

# print(site.prettify())

#indicando os parâmetros da pesquisa

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
  #indicando os parâmetros do título da notícia
  titulo = noticia.find('a',attrs={'class':'feed-post-link'})

  #subtitulo da notícia
  subtitulo = noticia.find('a',attrs={'class':'feed-post-body-title'})

  # .text pega apenas o texto daquele trecho de HTML
  # print(titulo.text)
  # print(titulo['href']) #atributo da notícia

if (subtitulo):
    #print(subtitulo.text)
    lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
else:
    lista_noticias.append([titulo.text,'',titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título','Subtítulo', 'Link'])

news.to_excel('noticas.xlsx', index=False)

#print(news)
