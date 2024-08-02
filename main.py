from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
import json
import os
import logging
# import spacy
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")

pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple", device = 0)

nlp = spacy.load("en_core_web_sm")
# Configure CORS
def extract_key_phrases(text):
    doc = nlp(text.lower())
    candidate_phrases = []
    for chunk in doc.noun_chunks:
        if chunk.root.text.lower() not in STOP_WORDS and chunk.root.text not in punctuation:
            candidate_phrases.append(chunk.text)
    return candidate_phrases

def analyze_text(text):
    # Perform NER
    doc = pipe(text)
    entities = [(ent['word'], ent['entity_group']) for ent in doc]
    
    # Extract key phrases
    key_phrases = extract_key_phrases(text)
    most_common_phrases = Counter(key_phrases).most_common(10)
    
    return entities, most_common_phrases

class Article(BaseModel):
    text: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Avocado AI FastAPI application. Use /articles to fetch articles and /process_article to process article text."}
@app.on_event('startup')
async def load_articles():
    global articles_data
    with open('articles.json', 'r') as f:
        articles_data = json.load(f)

@app.post("/analyze_articles")
async def process_article_endpoint(article:Article):
    text = article.text
    # text = data.get("text", "")
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")
    
    entities, most_common_phrases = analyze_text(text)
    
    return {
        'named_entities': entities,
        'key_phrases': most_common_phrases
    }


# Endpoint to get all articles
@app.get("/articles")
async def get_articles():
    return articles_data



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)