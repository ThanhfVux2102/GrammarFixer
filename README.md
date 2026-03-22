# 🧠 GrammarFixer – AI Grammar Correction System

GrammarFixer is an AI-powered web application that automatically detects and corrects grammatical errors in English sentences using a Machine Learning model integrated with a modern web stack.

---

## 🚀 Tech Stack

### 🔹 Frontend
- React (Vite / CRA)
- Fetch API / Axios

### 🔹 Backend
- FastAPI
- Uvicorn

### 🔹 AI / ML
- Transformers / PyTorch
- Custom-trained Grammar Error Correction (GEC) model

### 🔹 Deployment
- Frontend: Vercel / Netlify
- Backend: Render / Railway
- Docker (optional)

---

## 📂 Project Structure
GrammarFixer/

├── api/ # FastAPI backend

├── app.py # Main API entrypoint

├── routes/ # API routes

├── services/ # Business logic (model inference)

└── schemas/ # Pydantic models

├── frontend/ # React frontend

    ├── src/
    └── package.json
├── ml/ # Model + training + notebooks

    ├── notebooks/

    └── models/

├── docker/ # Docker configs

├── requirements.txt

├── Dockerfile

└── README.md

---

## ⚙️ Features

- ✅ Grammar correction using AI model
- ✅ Fast API response with optimized inference
- ✅ Clean React UI for user interaction
- ✅ Scalable backend architecture
- ✅ Ready for cloud deployment

---

## 🔌 API Contract

### POST `/api/correct`

#### Request
```json
{
  "text": "She go to school yesterday."
}
