import requests

# Send a Request to the Website To retrieve the HTML content of a web page, you need to send an HTTP request to its URL using the requests library. 

url = 'https://www.timeanddate.com/weather/'
response = requests.get(url)

# In the above code, we send a GET request to the URL 'https://www.example.com' using the requests.get() method. 

if response.status_code == 200:
    html_content = response.content
else:
    print(f'Request failed with status code {response.status_code}')

# If the request is successful (i.e., status code 200), we store the HTML content in the html_content variable.

# Parse the HTML Content Next, we need to parse the HTML content to extract the data we want. We can do this using the BeautifulSoup library.
 
# Here's an example:

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html_content, 'html.parser')

 # Find all links on the page: 

links = soup.find_all('a') 

# Find the text of the first heading on the page:

heading = soup.find('h1').text 

# In the above code, we create a BeautifulSoup object from the HTML content using the 'html.parser' parser.

# We can then use the soup.find_all() method to find all the links on the page, or the soup.find() method to find the first occurrence of a particular HTML element (in this case, the first h1 heading).

# Extract the Data you want once you have the HTML elements containing the data you want, you can extract the data itself. 

# Here's an example:

# Get the href attribute of the first link on the page

first_link = links[0].get('href') 

# Print the text of all the links on the page:

for link in links: 
   print(link.text) 

# In the above code, we use the get() method to extract the href attribute of the first link on the page. 

# We also use a for loop to print the text of all the links on the page.

# Finally save the Data, you can save the data you've scraped to a file or database. 

# Here's an example:

import csv 

# Save the links to a CSV file:

with open('links.csv', 'w') as file: 
   writer = csv.writer(file) 
   for link in links:
    writer.writerow([link.text, link.get('href')]) 

# In the above code, we use the csv module to save the links to a CSV file. 

# We open the file in write mode using a with statement, create a csv.writer object, and use a for loop to write each link's text and href attribute to a new row in the file.