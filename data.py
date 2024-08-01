import requests
from bs4 import BeautifulSoup
import json
import time


links = []
url = 'https://flo.health/menstrual-cycle'
base_url = 'https://flo.health'
response = requests.get(url)
time.sleep(3)  # Allow time for the page to load

soup = BeautifulSoup(response.content, 'html.parser')
articles_section = soup.find_all('div', {'class': 'flo-categories__articles'})
# Iterate through each div in the ResultSet
for section in articles_section:
    # Find all 'a' tags within the current section
    a_tags = section.find_all('a')
    # Extract the href attribute from each 'a' tag and add it to the links list
    for tag in a_tags:
        links.append(base_url+tag['href'])


def extract_text(element):
    """Recursively extract text from relevant elements, maintaining the order."""
    text_content = []
    for child in element.descendants:
        if child.name in ['p', 'li', 'h2', 'h3', 'h4', 'h5', 'h6']:
            text_content.append(child.get_text(strip=True))
    return text_content
article_list = []   

for l in links:
    driver.get(l)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #TITLE
    title = soup.find('h1').text.strip()
    #URL
    url = l
    #Publication date
    date = soup.find('div',{'class': 'flo-article-banner-bottom__info-panel-date--item'})
    date = date.text.replace('Published','').replace('  ','').replace('\n','')

    sections = soup.find_all('section', {'class': 'flo-article-text'})
    #Article Content
    content = []
    for section in sections:
        content.extend(extract_text(section))

    article_content = " ".join(content)

    article_list.append({
                'title': title,
                'url': url,
                'publication_date': date,
                'content': article_content
            })
    
with open('articles.json', 'w') as json_file:
    json.dump(article_list, json_file, indent=4)