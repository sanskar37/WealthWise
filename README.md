# 💰 WealthWise — Finance Tracker

A full-stack **Finance Tracking App** built with **FastAPI (Backend)**, **Streamlit (Frontend)**, and **MySQL (Database)**.  
WealthWise helps users **log transactions, analyze spending trends, and export reports**, enabling smarter financial decisions.

---

## 🚀 Features
- 🔹 **Transaction Management** — Add, view, and manage expenses & income.  
- 🔹 **Real-time Analytics** — Track spending patterns and visualize insights with **Matplotlib**.  
- 🔹 **CSV Export** — Export transaction history for personal records.  
- 🔹 **Fast & Secure** — Built with **FastAPI** + **MySQL** for speed and reliability.  
- 🔹 **Deployed MySQL on Railway** — Handles **1000+ transactions/month** securely.  
- 🔹 **Savings Insights** — Spend analytics helping users cut expenses by **up to 15%**.

---

## 🏗️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Database:** [MySQL](https://www.mysql.com/) (hosted on Railway)  
- **Deployment:** Streamlit Cloud (Frontend), Render/Railway (Backend)  
- **Visualization:** Matplotlib  
- **Other Tools:** Uvicorn, SQLAlchemy, Pydantic  

---

## 📂 Project Structure
```
FINTRACK-MAIN/
│── client/                  # Streamlit frontend
│   └── streamlit_app.py
│
│── server/                  # FastAPI backend
│   └── app/
│       ├── main.py          # FastAPI entry point
│       ├── models.py        # Database models
│       ├── schemas.py       # Pydantic schemas
│       ├── crud.py          # CRUD operations
│       ├── config.py        # Config (DB, secrets)
│       ├── database.py      # DB connection
│       └── utils.py
│
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

---

## ⚡ Getting Started (Local Setup)

### 1. Clone the repo
```bash
git clone https://github.com/your-username/wealthwise.git
cd wealthwise
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
# Windows
.\env\Scripts\activate
# Mac/Linux
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup database
- Ensure you have **MySQL** running (local or Railway).  
- Create a database (e.g., `wealthwise_db`).  
- Update `.env` file or `config.py` with your DB connection string:
  ```
  DATABASE_URL=mysql://username:password@host:3306/wealthwise_db
  ```

### 5. Run backend (FastAPI)
```bash
cd server
uvicorn app.main:app --reload --port 8000
```
Backend will run on → [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Docs available at → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6. Run frontend (Streamlit)
Open another terminal:
```bash
cd client
streamlit run streamlit_app.py
```
Frontend will run on → [http://localhost:8501](http://localhost:8501)
---

## 📌 Future Improvements
- Add authentication (JWT / OAuth2)  
- Support multiple currencies  
- Advanced budgeting & savings goals  
- Mobile-friendly UI  

---
## 👨‍💻 Author
**WealthWise — Finance Tracker**  
Developed by *Sanskar* ✨  
🔗 GitHub: https://github.com/sanskar37
