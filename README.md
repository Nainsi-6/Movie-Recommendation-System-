🎬 Movie Recommendation System

A hybrid movie recommendation system that provides personalized movie suggestions using a combination of **content-based filtering** and **similarity-based collaborative techniques**.  
The project focuses on recommendation relevance, explainability, and a clean, reproducible ML pipeline with an optional Streamlit interface.

 🚀 Project Overview

This system recommends movies by analyzing:
- Similarities between movie content such as genres, overview, and keywords
- Relationships inferred through similarity metrics

A hybrid approach is used to improve recommendation quality and reduce limitations of using a single method.

🧠 Recommendation Approach

🔹 Content-Based Filtering
- Uses movie metadata (genres, descriptions, keywords)
- Applies TF-IDF vectorization to convert text into numerical features
- Computes cosine similarity to find related movies

🔹 Similarity-Based Recommendation
- Uses similarity matrices to identify closely related movies
- Ensures recommendations align with user preferences

🔹 Hybrid Strategy
- Combines outputs from multiple similarity techniques
- Produces more relevant and balanced recommendations

🖥️ Streamlit Application

The Streamlit app allows users to:
- Select a movie
- Instantly receive recommended movies
- Interact with a simple and intuitive UI

All deployment-related files are located in the `Streamlit Deployment/` directory.

 ⚙️ Technologies Used

- Python
- Pandas
- Scikit-learn
- NLTK
- Streamlit
- Jupyter Notebook

---

▶️ How to Run Locally

1️⃣ Clone the repository

git clone https://github.com/Nainsi-6/Movie-Recommendation-System-.git
cd Movie-Recommendation-System-

📁 Project Structure

Movie-Recommendation-System/
│
├── Streamlit Deployment/ # Streamlit app and deployment files
├── model/ # Model generation logic (no artifacts committed)
├── movie_recommender.ipynb # Core notebook for preprocessing & recommendations
├── tmdb_5000_movies.csv # Movie metadata dataset
├── tmdb_5000_credits.csv # Cast and crew dataset
├── requirements.txt # Project dependencies
└── README.md

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Generate recommendation models

Run the notebook:

movie_recommender.ipynb


This will generate similarity matrices and required data locally.

4️⃣ Run the Streamlit app
streamlit run Streamlit\ Deployment/app.py


