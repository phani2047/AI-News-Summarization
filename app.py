from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import requests
from newspaper import Article

app = FastAPI()

# Load AI Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class NewsRequest(BaseModel):
    url: str

def fetch_news_content(url):
    """Extract news content from the given URL."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {"title": article.title, "content": article.text}
    except Exception as e:
        return {"error": str(e)}

@app.post("/summarize")
async def summarize_news(news_request: NewsRequest):
    news = fetch_news_content(news_request.url)
    
    if "error" in news:
        return news
    
    summary = summarizer(news["content"], max_length=150, min_length=50, do_sample=False)
    
    return {
        "title": news["title"],
        "summary": summary[0]['summary_text']
    }

# Run the server: uvicorn app:app --reload
