from bs4 import BeautifulSoup
import requests

# Get the HTML of the page
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_website = response.text

# Parse the page
soup = BeautifulSoup(movies_website, "html.parser")
# Extract the film titles
h3_tags = soup.find_all(name="h3", class_="title")
# Create a list of the top 100 film titles
movie_titles = [movie.getText() for movie in h3_tags]
# Reverse the film order
reversed_movie_list = movie_titles[::-1]

# Write the txt file that will include all of these films
with open("100movies.txt", "a") as file:
    for movie in reversed_movie_list:
        file.write(movie)
        file.write('\n')
