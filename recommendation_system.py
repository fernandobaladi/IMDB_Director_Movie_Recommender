#Let's make some basic imports to scrape
import requests
from bs4 import BeautifulSoup

#We ask the user to write a movie from the IMDB top 250 movies 
user_movie_name = input('Enter a movie that you like: ')

#Let's retrieve the 250 movies from the IMDB top
res = requests.get('https://www.imdb.com/chart/top/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')

#Now we select the rows to find the movie name that we are looking for
#Remember that we are looking for the movie name that the user entered
tr_tags = soup.select('tbody.lister-list tr')
for tr in tr_tags:
    td = tr.find('td', {'class': 'titleColumn'})
    movie_name = td.a.string
    if(movie_name == user_movie_name):
        #Once we found the movie, we get the year and the url to get the movie director
        movie_year = td.span.string
        movie_url = f"https://www.imdb.com{td.a['href']}"
        break

#Here we instance the payload and the header because if we don't send it to IMDB's page
#It returns a 403 error
payload = {}
headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
          }

#Here we retrieve the movie page
response = requests.request("GET", movie_url, headers=headers, data=payload)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#Now we select the director's name and its IMDB page
li = soup.select('[data-testid="title-pc-principal-credit"] li a')
director_name = li[0].string
director_page = f"https://www.imdb.com{li[0]['href']}"

#Now we scrape the director's page
response = requests.request("GET", director_page, headers=headers, data=payload)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#Finally here we get some movies directed from the same director
#And we print the movie recomendations
titles_list = soup.find_all('a', {'class': 'ipc-primary-image-list-card__title'})
print(f"It was released in {movie_year.strip('(').strip(')')}")
print(f"The movie director's name is {director_name}")
print(f"Some other movies of the same director that you might like are {', '.join([a.string for a in titles_list])}")
