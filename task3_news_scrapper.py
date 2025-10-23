import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Fetch the HTML content
response = requests.get(url)

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines
headlines = []
for h in soup.find_all(['h1', 'h2', 'h3'], limit=15):
    text = h.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)

# Save the headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, headline in enumerate(headlines, 1):
        f.write(f"{i}. {headline}\n")

print("✅ Headlines scraped successfully and saved to 'headlines.txt'")
