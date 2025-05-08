# 🏡 California Housing Price Predictor

An interactive full-stack machine learning app that predicts median house values in California based on user-input housing features. Built and designed by **Mahir Ahmed**, this project demonstrates how to deploy real ML models through a beautiful web UI using modern tools.

---

## 🚀 Features

- 🔮 Predicts house prices in real-time using a trained Random Forest model
- 🎨 Clean UI built with React + Vite + Tailwind CSS
- ⚙️ Backend powered by FastAPI, Pydantic, and scikit-learn
- 🔗 Frontend and backend connected via a robust API
- 📄 Downloadable research summary included (PDF)

---

## 🧠 Tech Stack

| Layer        | Tools Used                                     |
|--------------|------------------------------------------------|
| Frontend     | React, TypeScript, TailwindCSS, Vite           |
| Backend      | FastAPI, Pydantic, scikit-learn, joblib        |
| ML Model     | RandomForestRegressor, GridSearchCV, pandas    |
| Deployment   | Vercel (frontend), Render (backend)            |

---

## 📁 Project Structure

```
CaliforniaHousingPredictor/
├── backend/                 # FastAPI backend with prediction route
│   └── app/                 # API + ML loading logic
├── frontend/                # React + Tailwind frontend
├── housing.csv              # Raw dataset (optional)
├── california_housing.ipynb # Model training + EDA
├── requirements.txt         # Backend dependencies
├── .gitignore               # Git exclusions
├── .gitattributes           # LFS tracking for .pkl
└── README.md                # This file
```

---

## 🔧 Getting Started Locally

### 📦 Backend (FastAPI)
```bash
cd backend
uvicorn app.main:app --reload
```

### 💻 Frontend (Vite + React)
```bash
cd frontend
npm install
npm run dev
```

> Make sure your `.pkl` model is in `backend/ml_model/` and matches your training format.

---

## 🧪 Model Details

- Features used:
  - `longitude`, `latitude`, `housing_median_age`, `total_rooms`,
  - `total_bedrooms`, `population`, `households`, `median_income`
- Target: `median_house_value`
- Trained using RandomForest + GridSearchCV
- Pickle model saved with joblib

---

## 🌐 Deployment

- **Frontend** hosted on Vercel  
  `https://your-frontend-url.vercel.app`

- **Backend** hosted on Render  
  `https://your-backend-api.onrender.com/api/v1/predict`

To switch environments, change the API endpoint in `frontend/src/services/housingService.ts`.

---

## 📄 Credits

Created by **Mahir Ahmed**  
Trained on the California housing dataset (originally from StatLib)

---

## 📬 Contact

For questions, collaborations, or feedback:  
📧 nafismahir@icloud.com
🌐 https://www.linkedin.com/in/shahriyar-ahmed-mahir-b585ba2b6/



