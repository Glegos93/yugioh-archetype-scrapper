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

# Define the URLs
urls = [
    'https://yugipedia.com/wiki/Category:Archetypes',
    'https://yugipedia.com/index.php?title=Category:Archetypes&pagefrom=Fire+Fist#mw-pages',
    'https://yugipedia.com/index.php?title=Category:Archetypes&pagefrom=Nekroz#mw-pages',
    'https://yugipedia.com/index.php?title=Category:Archetypes&pagefrom=T.G.#mw-pages'
]

# Use the function for each URL
total_count = 0
for url in urls:
    titles = scrape_wikia(url)
    for title in titles:
        print(title)
        total_count += 1

# Print the total count
print(f'Total count: {total_count}')