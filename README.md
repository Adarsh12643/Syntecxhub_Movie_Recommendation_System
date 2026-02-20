# 🎬 CINEWORLD: AI-Powered Movie Recommendation System

CINEWORLD is a high-performance, content-based recommendation engine. It utilizes Natural Language Processing (NLP) to analyze cinematic plot signatures and provide users with contextually relevant movie suggestions.

---

## 🚀 Key Features

* **Exact Match Logic**: Unlike traditional systems that skip the query, CINEWORLD identifies and highlights the searched movie as a "Your Match" result before presenting AI suggestions.
* **NLP Engine**: Powered by **TF-IDF Vectorization** and **Cosine Similarity** to understand the semantic relationship between movie overviews.
* **Modern UI/UX**: A sleek, responsive interface built with **Tailwind CSS**, featuring glassmorphism effects, smooth transitions, and a dark-mode-first aesthetic.
* **Live Search**: Asynchronous (AJAX) search handling using Python Flask and JavaScript Fetch API, providing results without page reloads.
* **Dynamic Response**: Optimized to handle both the real TMDB 5,000 movie dataset and lightweight mock data for testing.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.x, Flask
* **Machine Learning**: Scikit-learn (TfidfVectorizer, Cosine Similarity)
* **Data Handling**: Pandas, NumPy
* **Frontend**: HTML5, Tailwind CSS, JavaScript (ES6+)
* **Icons/Fonts**: Material Symbols, Plus Jakarta Sans

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/Adarsh12643/cineworld-recommender.git
cd cineworld-recommender

```


2. **Install Dependencies**
```bash
pip install flask pandas scikit-learn

```


3. **Data Setup**
Ensure your `tmdb_5000_movies.csv` file is placed in the root directory. If the file is missing, the system will automatically initialize a mock dataset for demonstration.
4. **Run the Application**
```bash
python app.py

```


Navigate to `http://127.0.0.1:5000` in your browser.

---

## 🧠 How It Works

1. **Vectorization**: The system cleans movie plot summaries and converts them into a high-dimensional vector space using the **Term Frequency-Inverse Document Frequency (TF-IDF)** algorithm.
2. **Similarity Scoring**: When a user searches for a movie, the system calculates the **Cosine Similarity** (the cosine of the angle between two vectors) between the searched movie and all other entries in the database.
3. **Filtering**: The engine sorts the results based on the highest similarity scores, filters out noise, and returns the top 5 closest matches.

---

## 📈 Future Outcomes & Roadmap

CINEWORLD is designed with scalability in mind. Reliable future outcomes for this project include:

* [ ] **Hybrid Filtering Implementation**: Combining content-based filtering with **Collaborative Filtering** (User-to-User) to suggest movies based on community ratings.
* [ ] **Cloud Deployment**: Deploying the application to **Render**, **Heroku**, or **AWS** to make it accessible to global users.
* [ ] **Live API Integration**: Replacing static CSV data with the **TMDB API** to fetch real-time posters, trailers, and cast information.
* [ ] **Personalized User Accounts**: Implementing a database (PostgreSQL/Firebase) to allow users to save their "Watchlist" across devices.
* [ ] **Deep Learning Migration**: Utilizing **BERT** or **Word2Vec** embeddings for even more nuanced plot understanding.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork** the Project.
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the Branch (`git push origin feature/AmazingFeature`).
5. **Open** a Pull Request.
