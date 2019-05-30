from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import bs4
from bs4 import BeautifulSoup

########################################################

# Helper functions to download page and save
def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html.encode('utf-8'))
        
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

def parse_html(html, arr):
    for extract in html:
        arr.append(extract.text.strip('\n '))

# Prompts user to pick a movie, returns chosen movie
def menu(title_showtime):
    list_of_movies = []

    print("Select Movie to Watch:")
    for index, movie_title in enumerate(title_showtime):
        print(index, movie_title)
        list_of_movies.append(movie_title)

    print()
    choice = input("Enter a number from choices above:")
    chosen_movie = list_of_movies[int(choice)]
    return chosen_movie

# Get time of today's date
now = datetime.datetime.now()
print(now.date())

# scrape the movies/showtime 
# driver = webdriver.Chrome()
# driver.get('https://www.movietickets.com/theaters/detail/id/ti-10358/name/sierra-vista-cinemas-16?date='+ str(now))

# Save the data into file
# html = driver.page_source
# save_html(html, 'sierra-vista-movies.html')

# Pretty print file retrieved
html = open_html('sierra-vista-movies.html')
soup = BeautifulSoup(html, 'html.parser')
# save_html(soup.prettify(), 'pretty-sierra.html')

############### Extract Movies and Set Times #######################
title_showtime = {}
movies = soup.find_all('div', class_='small-12 column theater-detail-movie-darken')

for movie_title in movies:
    if not isinstance(movie_title.next_sibling, bs4.Tag):
        title = movie_title.find('h4', class_='theater-detail-movie-title').text
        title = title.strip('\n  ')

        # Grabs all time per movie
        time = movie_title.find_all('a', class_='button showtime mtc-showtimes')
        # print(time)

        # Strips html tag from movie and appends to list
        movie_times = []
        for movie_time in time:
            bsTime = movie_time.text.strip()
            # print(bsTime)    
            movie_times.append(bsTime)
        
        # makes dictionary with movie title/time
        title_showtime[title] = movie_times

        # title_showtime[title] = time

# print(title_showtime)
chosen_movie = menu(title_showtime)
print("Getting available seats for all available set times:")
print(title_showtime.get(chosen_movie))



############# Generate URL ##################

# Performance = showtimeID
# Movie = Movie-id

# https://www.movietickets.com/purchase/performance/1029612095?theater-id=10358&movie-id=257059&step=initial
# https://www.movietickets.com/purchase/performance/1029612040?theater-id=10358&movie-id=257059&step=initial
# https://www.movietickets.com/purchase/performance/1029612031?theater-id=10358&movie-id=272082&step=initial

# showtime_ID = 1029612095
# movie_ID = 257059
# driver = webdriver.Chrome()
# driver.get('https://www.movietickets.com/purchase/performance/'+ str(showtime_ID) + '?theater-id=10358&movie-id=' + str(movie_ID) +'&step=seatselection')

# driver.find_element_by_class_name("ticket-selection").click()

# <input class="button" id="add-ticketss" type="submit" name="Add Tickets" onclick="showPurchaseProgressArea();" value="Add Tickets">


