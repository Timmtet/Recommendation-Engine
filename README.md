🎬 # Movie Recommendation Engine
Deploying a Content-Based Movie Recommendation System with Streamlit & TMDB API

📌 Overview
This project is focused on building and deploying a content-based movie recommendation engine using Python and streamlit respectively. The system recommends movies based on textual features like title, genres, keywords, and overview. A Streamlit web app was developed to make the system interactive, allowing users to select a movie and receive recommendations with posters fetched via the TMDB API.

🛠 Tech Stack
•	Python (Pandas, NumPy, Scikit-learn, NLTK)
•	Natural Language Processing (NLP) (Porter Stemmer, CountVectorizer)
•	Machine Learning (Cosine Similarity, Nearest Neighbors)
•	Streamlit (For Web App Deployment)
•	TMDB API (For Movie Posters)

📂 Project Structure
📂 Recommendation Engine
│── 📁 venv                      # Python Virtual Environment  
│── 📜 app.py                    # Streamlit web app  
│── 📊 cleaned_movies3.xlsx       # Preprocessed dataset  
│── 📊 keywords.xlsx              # Movie keywords dataset  
│── 📊 movies_metadata.xlsx       # Original metadata  
│── 📜 movie_list.pkl             # Serialized movie list  
│── 📜 vectorized_sparse.pkl      # Sparse matrix for similarity  
│── 📜 rec_engine.ipynb           # Jupyter Notebook for training  
│── 📜 requirements.txt           # Project dependencies  


📈 Data Pipeline
1.	Data Collection: Movie metadata from Kaggle: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data

2.	Data Cleaning: Removed duplicates, missing values, and incorrect formats
3.	Feature Engineering: Extracted text-based features (title, genres, keywords, overview)
4.	Text Processing: Lowercasing, stemming (Porter Stemmer), and vectorization (CountVectorizer)
5.	Building the Model: Nearest Neighbors with Cosine Similarity
6.	Web App Deployment: Interactive movie selection with Streamlit

🚀 How to Run
1️ Clone the Repository
git clonehttps://github.com/Timmtet/Recommendation-Engine.git
cd movie-recommendation-engine
2️ Activate the Virtual Environment
If you're using Windows:
venv\Scripts\activate
If you're using Mac/Linux:
source venv/bin/activate
3️  Install Dependencies
Inside the virtual environment, install the necessary packages:
pip install -r requirements.txt
4️ Run the App
streamlit run app.py

🏆 Key Features
✅Select a movie from a dropdown menu
✅Get 10 recommended movies based on similarity
✅View movie posters retrieved from TMDB API
✅Fast & lightweight deployment with Streamlit

🛠 Challenges Faced
•	Memory Limitations: Original dataset was too large (45,000+ movies). 
o	Solution: Filtered dataset to include movies released after 2015.

🎯 Future Improvements
•	Implement hybrid recommendations (content-based + collaborative filtering)
•	Improve model efficiency using TF-IDF or Deep Learning

💡 Acknowledgments
•	Kaggle: Movie dataset
•	TMDB API: Movie posters
