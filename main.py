import requests
from bs4 import BeautifulSoup

def scrape_wikia(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = []
    for group in soup.find_all(class_='mw-category-group'):
        for title in group.find_all('a'):
            titles.append(title.get_text())
    
    return titles

# Use the function
url = 'https://yugipedia.com/wiki/Category:Archetypes'
titles = scrape_wikia(url)
for title in titles:
    print(title)