# 📰 AI News Summarization API

## 📌 Overview
The **AI News Summarization API** is a FastAPI-based web service that extracts news articles from given URLs and generates **short summaries** using **Natural Language Processing (NLP) models**.

✅ **Tech Stack:**  
- 🐍 FastAPI (Backend)
- 🤖 Hugging Face Transformers (`facebook/bart-large-cnn`)
- 🌐 Newspaper3k & BeautifulSoup (Web Scraping)
- ⚡ Uvicorn (Server)
- 📡 Render (Deployment) *(Optional)*

---

## 🔧 **Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/phani2047/AI-News-Summarization.git
cd AI-News-Summarization


2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
Activate it:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🚀 Run the API Locally
Start the FastAPI server:

bash
Copy code
uvicorn app:app --reload
API will be available at:

Swagger UI: http://127.0.0.1:8000/docs
Redoc UI: http://127.0.0.1:8000/redoc
📌 How to Use the API
1️⃣ Send a POST Request
Use Swagger UI or a tool like Postman:

📡 Endpoint: /summarize
json
Copy code
{
  "url": "https://www.bbc.com/news/articles/cd65pz1p7d9o"
}
2️⃣ Response (Example Output)
json
Copy code
{
  "title": "Putin agrees in Trump call to pause Ukraine energy attacks but no full ceasefire",
  "summary": "The Russian leader declined to sign up to the comprehensive month-long ceasefire that Trump's team recently worked out with Ukrainians in Saudi Arabia."
}


 Project Structure
bash
Copy code
📂 AI-News-Summarization
 ┣ 📜 app.py           # FastAPI Backend Code
 ┣ 📜 requirements.txt  # Dependencies List
 ┣ 📜 README.md        # Project Documentation (You're Reading This!)
 ┣ 📂 venv/            # Virtual Environment (Not Pushed to GitHub)
