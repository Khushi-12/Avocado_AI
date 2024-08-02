import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
links = []
url = 'https://flo.health/menstrual-cycle'
base_url = 'https://flo.health'
driver.get(url)
time.sleep(3)  # Allow time for the page to load

soup = BeautifulSoup(driver.page_source, 'html.parser')
articles_section = soup.find_all('div', {'class': 'flo-categories__articles'})

# print(articles_section)
# Iterate through each div in the ResultSet
for section in articles_section:
    # Find all 'a' tags within the current section
    a_tags = section.find_all('a')
    # Extract the href attribute from each 'a' tag and add it to the links list
    for tag in a_tags:
        links.append(base_url+tag['href'])
# print(links)
def extract_text(element):
    """Recursively extract text from relevant elements, maintaining the order."""
    text_content = []
    for child in element.descendants:
        if child.name in ['p', 'li', 'h2', 'h3', 'h4', 'h5', 'h6']:
            text_content.append(child.get_text(strip=True))
    return text_content
article_list = []   

for l in links:
    response = requests.get(l)
    soup = BeautifulSoup(response.content, 'html.parser')
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