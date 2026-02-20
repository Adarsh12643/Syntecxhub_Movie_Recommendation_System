from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# --- Data Engine ---
def load_data():
    # Use the credits file which exists
    credits_path = 'tmdb_5000_credits.csv'
    
    if os.path.exists(credits_path):
        df = pd.read_csv(credits_path)
        
        # Clean the data
        df['title'] = df['title'].fillna('')
        df['cast'] = df['cast'].fillna('')
        df['crew'] = df['crew'].fillna('')
        
        # Extract main actor names from cast (first 3 actors)
        def extract_cast(cast_str):
            try:
                if cast_str:
                    cast_list = json.loads(cast_str)
                    actors = [c['name'] for c in cast_list[:3]]
                    return ' '.join(actors)
                return ''
            except:
                return ''
        
        # Extract director from crew
        def extract_director(crew_str):
            try:
                if crew_str:
                    crew_list = json.loads(crew_str)
                    for member in crew_list:
                        if member.get('job') == 'Director':
                            return member.get('name', '')
                return ''
            except:
                return ''
        
        # Create combined features for similarity
        df['cast_names'] = df['cast'].apply(extract_cast)
        df['director'] = df['crew'].apply(extract_director)
        df['combined_features'] = df['title'] + ' ' + df['cast_names'] + ' ' + df['director']
        
        # Use combined features for TF-IDF
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df['combined_features'])
        cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        return df, cos_sim
    else:
        # Fallback dataset for immediate testing
        data = {
            'title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Avengers', 'Iron Man', 'The Prestige'],
            'combined_features': [
                'Leonardo DiCaprio Joseph Gordon-Levitt Christopher Nolan',
                'Christian Bale Heath Ledger Christopher Nolan',
                'Matthew McConaughey Anne Hathaway Christopher Nolan',
                'Robert Downey Jr. Chris Evans Joss Whedon',
                'Robert Downey Jr. Jon Favreau',
                'Christian Bale Hugh Jackman Christopher Nolan'
            ]
        }
        df = pd.DataFrame(data)
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df['combined_features'])
        cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return df, cos_sim

df, cos_sim = load_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.json.get('movie_name', '').strip()
    
    if not movie_name:
        return jsonify({'success': False, 'message': 'Please enter a movie name.'})
    
    # Improved search: First try exact match (case-insensitive), then partial match
    # If multiple exact matches exist, use the first one
    idx_list = df[df['title'].str.lower() == movie_name.lower()].index.tolist()
    
    # If no exact match, try partial match
    if len(idx_list) == 0:
        # Use regex for partial matching with word boundaries for better results
        partial_matches = df[df['title'].str.lower().str.contains(movie_name.lower(), na=False)]
        if not partial_matches.empty:
            idx_list = partial_matches.index.tolist()
    
    if len(idx_list) > 0:
        idx = idx_list[0]
        
        # Get similarity scores for this movie
        sim_scores = list(enumerate(cos_sim[idx]))
        # Sort by similarity score (descending) and exclude the movie itself
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Exclude the searched movie itself and get top 6 recommendations
        sim_scores = [s for s in sim_scores if s[0] != idx][:6]
        
        movie_indices = [i[0] for i in sim_scores]
        
        # Prepare results with title and cast info
        results = []
        for i in movie_indices:
            movie_data = {
                'title': df['title'].iloc[i],
                'cast': df['cast_names'].iloc[i] if 'cast_names' in df.columns else '',
                'director': df['director'].iloc[i] if 'director' in df.columns else ''
            }
            results.append(movie_data)
        
        return jsonify({
            'success': True, 
            'results': results, 
            'searched': df['title'].iloc[idx]
        })
    
    return jsonify({'success': False, 'message': 'Movie not found. Please try another movie name.'})

if __name__ == '__main__':
    app.run(debug=True)
