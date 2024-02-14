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
    'https://yugipedia.com/index.php?title=Category:Archetypes&pagefrom=Fabled#mw-pages',
    'https://yugipedia.com/index.php?title=Category:Archetypes&pagefrom=Nekroz#mw-pages',
    'https://yugipedia.com/index.php?title=Category:Archetypes&pagefrom=T.G.#mw-pages'
]

# Use the function for each URL
titles_set = set()
for url in urls:
    titles = scrape_wikia(url)
    for title in titles:
        titles_set.add(title)

# Convert the set to a list and sort it
titles_list = sorted(list(titles_set))

# Print the titles
for title in titles_list:
    print(title)

# Print the total count
print(f'Total count: {len(titles_list)}')