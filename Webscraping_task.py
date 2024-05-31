import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_page(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('title').text
    first_paragraph = soup.find('p').text
    
    external_links = []
    references = soup.find_all('a', class_='external text')
    for ref in references:
        external_links.append(ref['href'])
    
    images_info = []
    image_tags = soup.find_all('img')
    for img in image_tags:
        image_url = img.get('src')
        alt_text = img.get('alt')
        images_info.append({'url': image_url, 'alt_text': alt_text})
    
    return {
        'title': title,
        'first_paragraph': first_paragraph,
        'external_links': external_links,
        'images_info': images_info
    }

url = "https://en.wikipedia.org/wiki/Automotive_industry"
result = scrape_wikipedia_page(url)

print("Title:", result['title'])
print("\nFirst Paragraph:", result['first_paragraph'])
print("\nExternal Links:", result['external_links'])
print("\nImages:")
for info in result['images_info']:
    print("URL:", info['url'])
    print("Alt Text:", info['alt_text'])
    print()
