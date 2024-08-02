# Avocado_AI
Avocado AI is a comprehensive machine learning project designed to extract, analyze, and generate insights from articles on menstrual health or contraception. The project involves scraping content, performing NLP tasks, and providing an API for text analysis.

## Tables of content
1. Introduction
2. Features
3. Installation
4. Usage
5. Project Structure
6. Contributing
7. License

## Introduction
Avocado AI aims to provide a robust solution for extracting, analyzing, and generating insights from articles related to menstrual health or contraception. The project includes a web scraper, named entity recognition, key phrase extraction, and an API endpoint for text analysis.

## Features
1. Content Extraction: Scrape articles from the Flo app's blog.
2. Named Entity Recognition (NER): Identify medical terms, conditions, and treatments.
3. Key Phrase Extraction: Highlight main topics and claims in the articles.
4. API Development: FastAPI endpoint for text analysis.

## Installation
To set up project locally, follow these steps: 
1. Clone the repository.
```
git clone https://github.com/Khushi-12/Avocado_AI.git
cd Avocado_AI
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
To run the project, use the following commands:
1. To scrape the articles.
```
python data.py
```
2. Start the FastAPI server:
```
uvicorn main:app --port 5000
```
3. Open 'index.html' file to enter the article content.


