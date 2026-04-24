# SIS-3 — ML System with Streamlit Frontend & MLflow

## Project Structure
```
sis3/
├── train.py            # Train model + MLflow experiment tracking + model registry
├── main.py             # FastAPI application
├── streamlit_app.py    # Streamlit frontend
├── model.joblib        # Generated after running train.py
├── requirements.txt    # Dependencies
├── Dockerfile          # FastAPI container
├── docker-compose.yml  # Full stack: API + Streamlit + MLflow
└── README.md
```

---

## Run Locally

### 1. Install & train
```bash
pip install -r requirements.txt
python train.py
```
MLflow will log: parameters, accuracy, f1_score, model artifact, and register model as `IrisClassifier`.

### 2. Start FastAPI
```bash
uvicorn main:app --reload
```
→ http://localhost:8000

### 3. Start Streamlit frontend
```bash
streamlit run streamlit_app.py
```
→ http://localhost:8501

### 4. Start MLflow UI
```bash
mlflow ui
```
→ http://localhost:5000

---

## Run with Docker (Full Stack)
```bash
docker-compose up --build
```

| Service   | URL                        |
|-----------|----------------------------|
| FastAPI   | http://localhost:8000      |
| Swagger   | http://localhost:8000/docs |
| Streamlit | http://localhost:8501      |
| MLflow    | http://localhost:5000      |

---

## MLflow Details
- **Experiment name:** `iris-classification`
- **Logged params:** `n_estimators`, `max_depth`, `random_state`
- **Logged metrics:** `accuracy`, `f1_score`
- **Model Registry name:** `IrisClassifier`

- <img width="1514" height="873" alt="Снимок экрана 2026-04-24 232556" src="https://github.com/user-attachments/assets/2d73814d-d74c-4d12-948b-9e6832d715ff" />
<img width="1482" height="1025" alt="Снимок экрана 2026-04-24 232610" src="https://github.com/user-attachments/assets/ac8f46c0-a4a3-4db0-9cd1-170dccc6ab10" />
<img width="1542" height="1098" alt="Снимок экрана 2026-04-24 232618" src="https://github.com/user-attachments/assets/882882d7-15bf-4258-a097-551421341eca" />





