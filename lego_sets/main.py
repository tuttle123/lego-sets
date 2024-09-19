import requests
from bs4 import BeautifulSoup
import random

def scrape_the_list(url, set_count=2):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Webpage request failed: {response.status_code}")
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all elements with the specific attribute 'data-test="article-text"'
        sets = soup.find_all(attrs={"data-test": "article-text"})
        
        # Extract the text from these elements and filter out the introduction paragraph
        set_texts = [set.text.strip() for set in sets if "LEGO®" in set.text]
        
        # We know that the actual LEGO sets start after the first one, so we skip the first item
        lego_sets = set_texts[1:12]  # Selecting sets 1 to 11
        
        # Return a random sample of the sets
        return random.sample(lego_sets, min(set_count, len(lego_sets)))
    
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []

def main():
    url = "https://www.lego.com/en-us/categories/adults-welcome/article/challenging-lego-sets-to-build-for-adults"

    sets = scrape_the_list(url)
    
    # Printing the two random sets selected from the list
    for i, set in enumerate(sets, 1):
        print(f"{i}: {set}")

# Boilerplate to run the main() function
if __name__ == "__main__":
    main()
