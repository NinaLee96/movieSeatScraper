# Movie Seat Scraper
Python script file uses Selenium to open up Chrome browser and navigate to URL. Then downloads the HTML and parses, extracting the movie title and time. 

Uses the title and set times to extract the movie ID and time ID from the website, generating a new URL which will open to the seat selection. Once here, all the available seats will be extracted from all the set times and returned.

*If site changes web layout and html, script will not work*
