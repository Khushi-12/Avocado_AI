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


# Project Summary
## Approach
The Avocado AI project is designed to extract and analyze articles on menstrual health or contraception from the Flo app's blog.

The key components of the approach are:

1. Content Extraction: Implemented a Python script to scrape articles from the Flo app's blog. The script extracts text content and metadata (title, URL, publication date) and stores it in JSON format.
2. Named Entity Recognition (NER): Utilized the Hugging Face model 'd4data/biomedical-ner-all' for NER. This setup allows for identifying medical terms, conditions, and treatments in the extracted content.
3. Key Phrase Extraction: Employed NLP techniques to extract key phrases, highlighting main topics and claims in the articles.
4. API Development: Developed a FastAPI endpoint that accepts article text as input and returns NER and key phrase extraction results.
## Challenges Faced
1. Setting Up FastAPI: Integrating FastAPI for the first time presented a learning curve. Ensuring smooth interaction between the FastAPI server and the NLP model required careful configuration and debugging.
2. Merging NER and Key Phrases into HTML Content: Combining the NER and key phrase extraction results into a cohesive HTML output was complex. It involved synchronizing the extracted entities and phrases with the original article text to maintain context and readability.
## Ideas for Scaling
1. Automated URL Integration: Enhance the system by connecting the website URL directly to the FastAPI endpoint. This will automate the process, allowing users to feed URLs instead of raw text, streamlining content extraction and analysis.
2. Custom Tuning of NER Pipeline: The current NER output is functional but can be improved. Fine-tuning the NER model to recognize only the desired tags will enhance accuracy. Customizing the pipeline to suit the specific needs of the project will yield more precise and relevant results.
