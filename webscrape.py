# Import the libraries we need:
# - requests: to download web pages
# - BeautifulSoup: to extract useful information from HTML
# - csv: to save our data into a CSV file
# - sys: to handle command-line arguments (like giving the program a URL)
import requests
from bs4 import BeautifulSoup
import csv
import sys

def fetch_html(url: str) -> bytes:
    """
    Download the HTML code from a web page.
    Returns the page content if successful, or None if something goes wrong.
    """
    try:
        # Send a GET request (like typing a URL into your browser)
        response = requests.get(url, timeout=10)

        # This will throw an error if the status code is not 200 (OK)
        response.raise_for_status()

        # Return the page content (HTML)
        return response.content

    except requests.RequestException as e:
        # If anything goes wrong (like network issues or invalid URL), print an error
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def parse_links(html: bytes):
    """
    Look inside the HTML and find:
    - The first <h1> heading (main title of the page)
    - All the <a> links on the page
    Returns both the heading and a list of links.
    """
    # Create a BeautifulSoup object so we can search the HTML easily
    soup = BeautifulSoup(html, "html.parser")

    # Find the first <h1> heading on the page (if it exists)
    heading = soup.find("h1").text.strip() if soup.find("h1") else "No heading found"

    # Find all <a> tags (links) on the page
    # For each link, get the visible text and the URL (href attribute)
    links = [(a.text.strip(), a.get("href")) for a in soup.find_all("a")]

    return heading, links

def save_links_to_csv(links, filename="links.csv"):
    """
    Save all the links into a CSV file so we can use them later.
    Each row will have:
    - The text of the link
    - The URL (href)
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Write the header row first
        writer.writerow(["Link Text", "URL"])

        # Write each link as a new row
        writer.writerows(links)

    print(f"✅ Saved {len(links)} links to {filename}")

def main():
    """
    Main function that runs when you start the program.
    1. Chooses which URL to scrape
    2. Downloads the HTML
    3. Finds the heading and links
    4. Prints a preview
    5. Saves everything to a CSV file
    """

    # Default website (the one in your example)
    url = "https://www.timeanddate.com/weather/"

    # If the user gives us a URL in the terminal, use that instead
    # Example: py scraper.py https://www.python.org
    if len(sys.argv) > 1:
        url = sys.argv[1]

    print(f"🔎 Fetching data from: {url}")

    # Step 1: Download the page
    html = fetch_html(url)
    if not html:
        return  # Stop if download failed

    # Step 2: Extract heading and links
    heading, links = parse_links(html)

    # Step 3: Show a preview in the terminal
    print(f"\n📌 Page heading: {heading}")
    print(f"🔗 Found {len(links)} links\n")

    # Show the first 10 links so we don’t flood the screen
    for text, href in links[:10]:
        print(f"- {text} ({href})")

    # Step 4: Save all links to a CSV file
    save_links_to_csv(links)

# This makes sure main() only runs if we start this file directly
# (not if we import it into another program)
if __name__ == "__main__":
    main()