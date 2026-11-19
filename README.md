
# 🏛️ SchemeSathi AI

### Government Schemes Made Simple, For Everyone.

SchemeSathi AI is an AI-powered multilingual assistant that helps citizens understand Indian government schemes, eligibility criteria, required documents, and application procedures in simple language.

## 🎯 Problem Statement

Many citizens struggle to understand government schemes because information is complex, scattered across websites, and often unavailable in their preferred language.

## 💡 Our Solution

SchemeSathi AI aims to make government scheme information accessible through an AI-powered assistant.

## ✨ Key Features

- 🌐 Multilingual support – Marathi, Hindi, and English
- 🤖 AI-powered question answering using Gemini
- 📋 Scheme eligibility guidance
- 📄 Required document information
- 📝 Application process guidance
- 🔗 Official government website references

## 🛠️ Technology Stack

- Python
- Streamlit
- Google Gemini API
- LangChain
- FAISS
- PyPDF

## 🚀 How to Run Locally

1. Clone or download this repository.
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate it on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

6. Start the application:

   ```bash
   streamlit run app.py
   ```

## 🌍 Official Information Sources

- [myScheme](https://www.myscheme.gov.in/)
- [MahaDBT](https://www.mahadbt.maharashtra.gov.in/)
- [National Scholarship Portal](https://scholarships.gov.in/)

## 🔐 Security

Never share your Gemini API key publicly. Keep your `.env` file private.

## 👩‍💻 Project

Built for the IDEA//FORGE Online Hackathon.

**SchemeSathi AI – Making Government Schemes Easy for Everyone!**
