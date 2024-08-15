import urllib.request
from bs4 import BeautifulSoup
from flask import app

# url used for data scraping
url = 'https://en.wikipedia.org/wiki/Mercedes-Benz_Group'  # You can change this to any other webpage with sufficient data

response = urllib.request.urlopen(url)
webContent = response.read()

# Parseing and extracting the content using BeautifulSoup
soup = BeautifulSoup(webContent, 'html.parser')

text = soup.get_text()

cleaned_text = ' '.join(text.split())

# Save the cleaned text to a file
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print("Data scraping complete. Text saved to 'scraped_data.txt'.")



if __name__ == "__main__":
    app.run(debug=True, port=5001) 
