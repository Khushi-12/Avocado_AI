from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
import json
import os
import logging

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# FastAPI app
app = FastAPI()

#Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Request model
class ArticleRequest(BaseModel):
    text: str

# Function to extract key phrases
def extract_key_phrases(text):
    doc = nlp(text.lower())
    candidate_phrases = []
    for chunk in doc.noun_chunks:
        if chunk.root.text.lower() not in STOP_WORDS and chunk.root.text not in punctuation:
            candidate_phrases.append(chunk.text)
    return candidate_phrases

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Avocado AI FastAPI application. Use /articles to fetch articles and /process_article to process article text."}

# Endpoint to process article text
@app.post("/process_article")
async def process_article(article: ArticleRequest):
    logger.info("Received request to process article")
    content = article.text
    
    # Perform NER
    logger.info("Starting Named Entity Recognition")
    doc = nlp(content)
    named_entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DISEASE', 'SYMPTOM', 'TREATMENT', 'MEDICATION', 'HORMONE']]
    logger.info(f"Named entities found: {named_entities}")
    
    # Extract key phrases
    logger.info("Starting key phrase extraction")
    key_phrases = extract_key_phrases(content)
    most_common_phrases = Counter(key_phrases).most_common(10)
    logger.info(f"Key phrases found: {most_common_phrases}")
    
    return {
        "named_entities": named_entities,
        "key_phrases": most_common_phrases
    }

# Endpoint to serve articles.json
@app.get("/articles")
async def get_articles():
    if not os.path.exists("articles.json"):
        raise HTTPException(status_code=404, detail="File not found")

    with open("articles.json", "r") as f:
        articles = json.load(f)
    print(articles)
    return articles

# Run the app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port = 5000)
