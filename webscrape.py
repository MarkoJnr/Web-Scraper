import requests

url = 'https://www.timeanddate.com/weather/'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
else:
    print(f'Request failed with status code {response.status_code}')

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html_content, 'html.parser')
 # Find all links on the page 
links = soup.find_all('a') 
# Find the text of the first heading on the page
heading = soup.find('h1').text 

import csv 
# Save the links to a CSV file 
with open('links.csv', 'w') as file: 
   writer = csv.writer(file) 
   for link in links:
    writer.writerow([link.text, link.get('href')]) 

