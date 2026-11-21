
# 🏛️ SchemeSathi AI
### Government Schemes Made Simple, For Everyone.

SchemeSathi AI is an AI-powered multilingual government schemes assistant designed to help citizens understand Indian government schemes in simple and easy language.

It provides information about scheme eligibility, benefits, required documents, and application procedures in Marathi, Hindi, and English.

---

## 🎯 Problem Statement

Many citizens are unable to access government scheme benefits because:
- Scheme information is complex and difficult to understand.
- Information is scattered across different government websites.
- People face language barriers.
- Citizens are often confused about eligibility and required documents.
- Finding the correct application process takes time.

## 💡 Our Solution

SchemeSathi AI simplifies access to government scheme information through an AI-powered multilingual assistant.

Users can ask questions in their preferred language and receive easy-to-understand answers based on available scheme documents.

---

## ✨ Key Features

- 🌐 Multilingual Support – Marathi, Hindi, and English.
- 🤖 AI-Powered Question Answering using Groq API.
- 📋 Scheme Eligibility Guidance.
- 📄 Required Documents Information.
- 💰 Scheme Benefits and Financial Assistance Details.
- 📝 Step-by-Step Application Process.
- 🔍 Document-Based Information Retrieval.
- 🏛️ Official Government Portal Links.
- 💬 Simple and User-Friendly Interface.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Streamlit | User Interface |
| Groq API | AI Response Generation |
| OpenAI GPT-OSS 20B | Language Model |
| PyPDF | PDF Text Extraction |
| Python Retrieval System | Scheme Information Retrieval |

---

## 🚀 Live Demo

**Try SchemeSathi AI:**

https://schemesathi-ai-prachi.streamlit.app/

---

## 📸 Application Screenshots

### 🏛️ Home Page
![Home Page](screenshots/home.png)

### 🤖 AI Answer in Marathi
![AI Answer](screenshots/answer.png)

### 📋 Eligibility Information
![Eligibility](screenshots/eligibility.png)

### 📄 Required Documents
![Documents](screenshots/documents.png)

### 🔍 Retrieved Information
![Retrieved Information](screenshots/retrieval.png)

---

## 📚 Government Information Sources

SchemeSathi AI provides guidance using available scheme documents and official government portals.

- [myScheme Portal](https://www.myscheme.gov.in/)
- [MahaDBT Portal](https://mahadbt.maharashtra.gov.in/)
- [National Scholarship Portal](https://scholarships.gov.in/)

**Note:** Users should verify the latest scheme rules, eligibility, benefits, and application requirements on official government portals before applying.

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/prachisonone04-ui/SchemeSathi-AI-Repository.git
```

### 2. Open the Project Folder

```bash
cd SchemeSathi-AI-Repository
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment (Windows)

```bash
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 7. Run the Application

```bash
streamlit run app.py
```

---

## 🔐 Security

- Never share API keys publicly.
- Keep `.env` files private.
- Never upload API credentials to GitHub.
- Use environment variables or secure secrets management.

---

## 🌟 Future Improvements

- Add more Indian government schemes.
- Improve retrieval accuracy and answer quality.
- Introduce voice-based question answering.
- Expand support for additional Indian languages.
- Provide more direct links to official application services.
- Improve accessibility for rural citizens.

---

## 👩‍💻 Developed By

**Prachi Sonone**

B.Sc. Student | Full Stack Developer | AI Enthusiast

- GitHub: https://github.com/prachisonone04-ui
- LinkedIn: https://linkedin.com/in/prachi-sonone-b45450399

---

## 🏆 Hackathon Project

Built for **IDEA//FORGE – NxtWave Academy AI & Agents Hackathon**.

---

### 🏛️ SchemeSathi AI
**Making Government Schemes Easy for Everyone!**
