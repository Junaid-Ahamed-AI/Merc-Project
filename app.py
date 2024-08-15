import urllib.request
from bs4 import BeautifulSoup
from flask import app

# Define the URL of the webpage to scrape
url = 'https://en.wikipedia.org/wiki/Mercedes-Benz_Group'  # You can change this to any other webpage with sufficient data

# Open the URL and fetch the content
response = urllib.request.urlopen(url)
webContent = response.read()

# Parse the content using BeautifulSoup
soup = BeautifulSoup(webContent, 'html.parser')

# Extract text from the webpage
text = soup.get_text()

# Optional: Clean the text (e.g., remove extra whitespace)
cleaned_text = ' '.join(text.split())

# Save the cleaned text to a file (for training later)
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print("Data scraping complete. Text saved to 'scraped_data.txt'.")



if __name__ == "__main__":
    app.run(debug=True, port=5001) 
