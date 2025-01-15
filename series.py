import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_series(url):
    titles = []
    while url:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for group in soup.find_all(class_='mw-category-group'):
            for title in group.find_all('a'):
                titles.append(title.get_text())
        
        next_link = soup.find('a', text='next page')
        if next_link:
            url = 'https://yugipedia.com' + next_link['href']
        else:
            url = None
    
    return titles

if __name__ == "__main__":
    url = 'https://yugipedia.com/wiki/Category:Series'
    titles_set = set()
    for _ in range(4):
        titles = scrape_series(url)
        for title in titles:
            titles_set.add(title)
        
        # Generate the next URL based on the second to last title
        if len(titles) >= 2:
            entry = titles[-2]
            url = f'https://yugipedia.com/index.php?title=Category:Series&pagefrom={urllib.parse.quote(entry)}#mw-pages'

    # Convert the set to a list and sort it
    titles_list = sorted(list(titles_set))

    print("it scrapped series data")
    # # Print the titles
    # for title in titles_list:
    #     print(title)

    # # Print the total count
    # print(f'Total count: {len(titles_list)}')