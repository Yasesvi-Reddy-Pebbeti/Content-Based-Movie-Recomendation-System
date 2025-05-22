# 🎬 Content-Based Movie Recommendation System

A full-stack Python application that allows users to register/login and receive intelligent movie recommendations using content-based filtering. Built with a Tkinter GUI, PostgreSQL backend, and scikit-learn for natural language-based similarity. Includes bulk SQL data ingestion and dynamic movie metadata retrieval.

---

## 🚀 Features

- 🔐 User Registration and Login (PostgreSQL)
- 🧠 Content-Based Recommendation using TF-IDF + Cosine Similarity
- 📂 Reads movie metadata from `movie_dataset.csv`
- 🧾 “About Movie” details fetched live from SQL database
- 🛠️ `.env` for secure credential management
- 📤 Custom script for automatic SQL table population from CSV

---

## 🧰 Tech Stack

- `Python 3`
- `Tkinter` – GUI
- `pandas`, `scikit-learn` – Data analysis & NLP
- `psycopg2` – PostgreSQL adapter
- `dotenv` – Secure credential loading
- `PostgreSQL` – Database
- `Git` – Version control

---

## 📁 Folder Structure

```
Content-Based-Movie-Recommendation-System/
│
├── data/
│   └── movie_dataset.csv
│
├── src/
│   ├── loginSignup.py        # GUI + logic
│   ├── registration.py       # Register/Login SQL operations
│   ├── movielistdata.py      # Fetch metadata from DB
│   └── movielist.py          # Bulk upload from CSV to SQL
│
├── requirements.txt
├── .env                      # (Not included in GitHub)
└── README.md
```

---

## 🖥️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Yasesvi-Reddy-Pebbeti/Content-Based-Movie-Recommendation-System.git
```

2. Navigate to the folder:
```bash
cd Content-Based-Movie-Recommendation-System
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

5. Load the dataset into PostgreSQL:
```bash
python src/movielist.py
```

6. Run the application:
```bash
python src/loginSignup.py
```

---

## 🧠 Recommendation Logic

This app uses a **CountVectorizer** over combined metadata features (cast, director, genre, keywords) to compute **cosine similarity** between movies and suggest the most similar ones based on the input title.

---

## 📸 Screenshots

> Add your screenshots here for:
> - Login/Register Window
> - Recommendation results
> - About Movie popup

---

## 🙋‍♂️ Author

Made with ❤️ by [Yash (Yasesvi Reddy Pebbeti)](https://github.com/Yasesvi-Reddy-Pebbeti)

---

## 🪪 License

This project is licensed under the MIT License.