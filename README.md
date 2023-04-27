# IMDB Director Movie Recommender

This Python script is designed to scrape data from the IMDB website and recommend other movies from the same director based on a user's input. The script uses the requests and BeautifulSoup libraries for web scraping.

## How it works:
1. The script asks the user to enter a movie title from the IMDB top 250 movies.
2. It retrieves the top 250 movies from IMDB.
3. It selects the movie the user entered and gets its release year and URL to get the director's name.
4. It retrieves the director's name and URL to get their directed movies.
5. It retrieves movies directed by the same director and recommends them to the user.

The script sends a GET request to the IMDB website to retrieve data. It also sets the user-agent header to avoid getting a 403 error.

Note: This script is for educational purposes only. Web scraping may not be legal in all circumstances, so use it at your own risk.