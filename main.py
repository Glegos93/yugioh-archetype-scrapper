from bs4 import BeautifulSoup
import urllib.parse
from archetype import scrape_archetype
from series import scrape_series
from google_sheets import get_google_sheets_data  # Import the Google Sheets function

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def read_current_file(filename):
    with open(filename, 'r') as file:
        return set(line.strip().lower() for line in file)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Define the URLs
# Do not change the following URLs
archetype_url = 'https://yugipedia.com/wiki/Category:TCG_and_OCG_archetypes'
series_url = 'https://yugipedia.com/wiki/Category:TCG_and_OCG_archetypes'
current_file = 'current.txt'
series_url_anime_manga = 'https://yugipedia.com/wiki/Category:Anime_and_manga_only_series'
series_url_rush_duel = 'https://yugipedia.com/wiki/Category:Rush_Duel_series'
archetype_url_anime_manga = 'https://yugipedia.com/wiki/Category:Anime_and_manga_only_archetypes'

def display_menu():
    print("Please choose an option:")
    print("1. Archetype (write to file)")
    print("2. Series (write to file)")
    print("3. Both (write to file)")
    print("4. Import data from Google Sheets")
    print("5. Archetype (print to console)")
    print("6. Series (print to console)")
    print("7. Both (print to console)")
    print("8. Archetype minus current.txt (print to console)")
    print("9. Series minus current.txt (print to console)")
    print("10. Both minus current.txt (print to console)")
    print("11. Unique to current.txt (print to console)")
    print("12. Exit")

print("Starting the program...")

while True:
    display_menu()
    choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, or 12): ")

    if choice == '1':
        print("Scraping archetype data...")
        archetype_titles = scrape_archetype(archetype_url)
        anime_manga_archetype_titles = scrape_archetype(archetype_url_anime_manga)
        filtered_titles = [title for title in archetype_titles if "(anime)" not in title.lower() and title.lower() not in (title.lower() for title in anime_manga_archetype_titles)]
        sorted_titles = sorted(set(title.lower() for title in filtered_titles))
        write_to_file('archetype.txt', sorted_titles)
        print("Archetype data written to archetype.txt")
    elif choice == '2':
        print("Scraping series data...")
        series_titles = scrape_series(series_url)
        anime_manga_titles = scrape_series(series_url_anime_manga)
        rush_duel_titles = scrape_series(series_url_rush_duel)
        filtered_titles = [title for title in series_titles if "(rush duel)" not in title.lower() and "(dm series)" not in title.lower()]
        filtered_titles = [title for title in filtered_titles if title.lower() not in (title.lower() for title in anime_manga_titles)]
        filtered_titles = [title for title in filtered_titles if title.lower() not in (title.lower() for title in rush_duel_titles)]
        sorted_titles = sorted(set(title.lower() for title in filtered_titles))
        write_to_file('series.txt', sorted_titles)
        print("Series data written to series.txt")
    elif choice == '3':
        print("Combining both archetype and series data from files...")
        archetype_titles = read_from_file('archetype.txt')
        series_titles = read_from_file('series.txt')
        combined_titles = set(archetype_titles + series_titles)
        sorted_titles = sorted(combined_titles)
        write_to_file('both.txt', sorted_titles)
        print("Combined data written to both.txt")
    elif choice == '4':
        print("Importing data from Google Sheets...")
        spreadsheet_name = 'Archetype Draft'
        sheet_name = 'Data'
        range_name = 'A2:A455'  # Adjust the range as needed
        data = get_google_sheets_data(spreadsheet_name, sheet_name, range_name)
        values_array = [row[0].lower() for row in data if row and row[0].strip()]  # Filter out empty rows and cells and convert to lowercase
        write_to_file(current_file, values_array)  # Write the values to current.txt
        for value in values_array:
            print(value)
        print(f"Total count: {len(values_array)}")
    elif choice == '5':
        print("Reading archetype data from file...")
        archetype_titles = read_from_file('archetype.txt')
        sorted_titles = sorted(set(archetype_titles))
        for title in sorted_titles:
            print(title)
        print(f"Total count: {len(sorted_titles)}")
    elif choice == '6':
        print("Reading series data from file...")
        series_titles = read_from_file('series.txt')
        sorted_titles = sorted(set(series_titles))
        for title in sorted_titles:
            print(title)
        print(f"Total count: {len(sorted_titles)}")
    elif choice == '7':
        print("Reading both archetype and series data from files...")
        archetype_titles = read_from_file('archetype.txt')
        series_titles = read_from_file('series.txt')
        combined_titles = set(archetype_titles + series_titles)
        sorted_titles = sorted(combined_titles)
        for title in sorted_titles:
            print(title)
        print(f"Total count: {len(sorted_titles)}")
    elif choice == '8':
        print("Reading archetype data from file and comparing with current.txt...")
        archetype_titles = read_from_file('archetype.txt')
        current_titles = read_current_file(current_file)
        remaining_titles = sorted(set(title.lower() for title in archetype_titles) - current_titles)
        for title in remaining_titles:
            print(title)
        print(f"Total count: {len(remaining_titles)}")
    elif choice == '9':
        print("Reading series data from file and comparing with current.txt...")
        series_titles = read_from_file('series.txt')
        current_titles = read_current_file(current_file)
        remaining_titles = sorted(set(title.lower() for title in series_titles) - current_titles)
        for title in remaining_titles:
            print(title)
        print(f"Total count: {len(remaining_titles)}")
    elif choice == '10':
        print("Reading both archetype and series data from files and comparing with current.txt...")
        archetype_titles = read_from_file('archetype.txt')
        series_titles = read_from_file('series.txt')
        combined_titles = set(title.lower() for title in archetype_titles + series_titles)
        current_titles = read_current_file(current_file)
        remaining_titles = sorted(combined_titles - current_titles)
        for title in remaining_titles:
            print(title)
        print(f"Total count: {len(remaining_titles)}")
    elif choice == '11':
        print("Reading both archetype and series data from files and finding unique titles in current.txt...")
        archetype_titles = read_from_file('archetype.txt')
        series_titles = read_from_file('series.txt')
        combined_titles = set(title.lower() for title in archetype_titles + series_titles)
        current_titles = read_current_file(current_file)
        unique_titles = sorted(current_titles - combined_titles)
        for title in unique_titles:
            print(title)
        print(f"Total count: {len(unique_titles)}")
    elif choice == '12':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
    
    # Print three empty lines
    print("\n\n\n")
