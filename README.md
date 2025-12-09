
# Grammatical Error Correction (GEC) Web Application

The **Grammatical Error Correction (GEC)** web application uses a **fine-tuned transformer** model from **Hugging Face** to detect and correct grammar errors in text. The application supports **real-time corrections** via **WebSocket** and **FastAPI**, with the frontend built using **Streamlit**. AI models are deployed and monitored through **Docker** and **MLflow**, with the model trained on the **The BEA-2019 Shared Task** dataset.

##  Run the Application

### 1. **Environment Setup**
First, you need to install the necessary libraries for this application. Below are the installation steps.

#### **Requirements:**
- Python 3.7 or higher
- pip (Python package manager)
- Docker (for MLOps and containerized environment)
- Node.js and npm (for frontend with Streamlit)

#### **Install Backend:**
1. Clone the repo to your machine:
   ```bash
   git clone https://github.com/your-username/grammatical-error-correction.git
   cd grammatical-error-correction
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

#### **Install Frontend:**
1. Navigate to the **frontend** directory:
   ```bash
   cd frontend
   ```

2. Install the required packages:
   ```bash
   npm install
   ```

### 2. **Environment Configuration**
- Modifying the model configuration in **`backend/app.py`** if you want to use a different model (BERT, T5, etc.).
- Ensure that you have downloaded the GEC model from **Hugging Face** (or a different fine-tuned model).

### 3. **Run Backend**
Run the FastAPI backend using Uvicorn:
```bash
uvicorn backend.app:app --reload
```

- After the server is running, your API will be available at [http://localhost:8000](http://localhost:8000).

### 4. **Run Frontend**
Navigate to the **frontend** directory and run the application:
```bash
streamlit run app.py
```
- After the frontend server is running, the application will be available at [http://localhost:8501](http://localhost:8501).

### 5. **Using the Application**
1. Access the application in your browser at **http://localhost:8501**.
2. Enter the text you want to check in the input field.
3. Click the **"Correct Grammar"** button to get the corrected text from the system.
4. The corrected result will be displayed immediately.

### 6. **WebSocket Configuration**
The application uses **WebSocket** to process grammar correction requests in real-time. When the user sends the text, the backend receives the data via WebSocket and returns the result immediately.



---

##  **AI Model**

The application uses a **fine-tuned transformer** model for the **Grammatical Error Correction (GEC)** task. This model can be **BERT**, **T5**, or other models from **Hugging Face**.

- **Hugging Face Model**: [BERT for GEC](https://huggingface.co/bert-base-uncased) .

This model is fine-tuned to detect and correct grammar errors in text, including errors like:
- Spelling mistakes
- Sentence structure errors
- Punctuation errors

##  **Training Data**

The GEC model uses the **The BEA-2019 Shared Task** training dataset.

- **BEA-2019 dataset** consists of text that has been annotated for errors and human-made corrections. It is a standard dataset for training GEC models.
  
  You can download the dataset from: [The BEA-2019 Shared Task](https://www.clips.uantwerpen.be/BEA2019/).

## 🛠 **Tech Stack**

### 1. **Frontend**
- **Streamlit**: A Python framework for building user interfaces quickly, suitable for data science and machine learning applications.
  
### 2. **Backend**
- **FastAPI**: A Python framework to build APIs quickly and efficiently. FastAPI helps handle both RESTful requests and WebSocket connections.
- **WebSocket**: Allows real-time data transmission between frontend and backend.

### 3. **MLOps**
- **Docker**: Packages the backend FastAPI application and the AI model into a container for easy and consistent deployment.
- **MLflow**: Tracks, manages, and deploys AI models. It helps monitor experiments, store models, and deploy them to production.

### 4. **Deployment**
- **Render**: A cloud service for easily deploying the FastAPI backend.

---

##  **Docker and MLflow (MLOps)**

### 1. **Using Docker**:
Docker helps you package the FastAPI backend and AI model training environment into a single container, making deployment easier across different environments.

To run the application in Docker, you can use the **Dockerfile** available in this repo.

- **Docker Build**:
```bash
docker build -t grammatical-error-correction .
```

- **Docker Run**:
```bash
docker run -p 8000:8000 grammatical-error-correction
```

### 2. **Using MLflow**:
MLflow helps monitor the model training process, track parameters, and deploy models in production environments.

- Install MLflow:
```bash
pip install mlflow
```

- After training the model, you can use **MLflow** to log and track the model:
```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("param1", value)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.pytorch.log_model(model, "model")
```

---

##  **Improvements and Upcoming Features**
- **Model Improvements**: Integrate better models for GEC.
- **Personalization**: Provide customization options for users (e.g., select preferred models, feedback).
- **Language Translation Integration**: Add translation features and grammar correction for multiple languages.

---

## **Tech Stack Summary**:

- **Frontend**: Streamlit (Quick UI development)
- **Backend**: FastAPI + WebSocket (Fast and efficient API handling)
- **MLOps**: Docker + MLflow (Model deployment and monitoring)
- **Deployment**: Render (Easy backend deployment)
- **Dataset**: The BEA-2019 Shared Task (Data for GEC)
- **Model**: Fine-tuned models from Hugging Face (BERT/T5)