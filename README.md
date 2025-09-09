## Web Scraping Tutorial
This tutorial demonstrates how to scrape links and headers from a website using Python 3 and the BeautifulSoup library.
It is written step by step so beginners can follow along.

##  Prerequisites
You need Python installed, plus these libraries:

**requests** (for fetching web pages)
**beautifulsoup4** (for parsing HTML)

Install them with pip:

pip install requests beautifulsoup4

## Getting Started

Open your preferred text editor or IDE (e.g., VS Code, PyCharm, or IDLE).

Create a new Python file (e.g., webscrape.py).

Copy the code from this tutorial into your file.

Save it with a .py extension.

## How it Works

The script uses **requests** to send a GET request to a website and download its HTML content.

BeautifulSoup parses the HTML and extracts:

The main heading (<h1> tag)
All the links (<a> tags)

The results are:
Printed in the terminal

Saved to a CSV file using the csv module.

## How to Use

Run the script from your terminal:

**python webscrape.py**


By default, the script scrapes from:

https://www.timeanddate.com/weather/

## Scraping a Different Website

You can scrape any other website by doing the following:

Change the url inside the script
Open webscrape.py and edit this line:

url = "https://www.timeanddate.com/weather/"


Without editing the script, you can also provide the URL directly when running:

python webscrape.py https://www.python.org


This will scrape links and headings from the Python homepage instead of the default site.

## Customization

Save to a different file:
Edit this line in the script:

with open('links.csv', 'w') as file:
Replace 'links.csv' with another filename (e.g., "new_links.csv").

## Notes

This tutorial was written to help beginners learn the basics of web scraping.
The code includes extra comments to explain each step clearly.
The aim is to provide a guide that’s both accessible for beginners and useful for experienced developers.