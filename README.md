## Simple Web Scraper
This Python script retrieves the HTML content of a web page, extracts all links using the Beautiful Soup library, and saves the links to a CSV file.

## Prerequisites
To run the script, you need to have Python 3 and the following libraries installed:

**requests**  **beautifulsoup4**
You can install these libraries using pip. Open your terminal or command prompt and type:

**pip install requests beautifulsoup4**

## Installing
Download or clone this repository to your local machine.
Open your terminal or command prompt and navigate to the project directory.
Run the script by typing the following command:

**python webscrape.py**

## Usage
By default, the script extracts all links from the URL 'https://www.timeanddate.com/weather/' and saves them to a CSV file named 'links.csv'. If you want to scrape a different URL or save the links to a different file name, modify the url and with open('links.csv', 'w') as file lines in the script accordingly.
# Web-Scraper
