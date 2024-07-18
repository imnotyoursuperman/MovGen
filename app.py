from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

genres = [
    'Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance',
    'Thriller', 'Adventure', 'Animation', 'Documentary', 'Fantasy',
    'Musical', 'Mystery', 'Western', 'Biography', 'Crime', 'Family', 
    'History', 'Sport', 'War'
]
years = list(range(2000, 2024))  # From 2000 to 2023
languages = [
    'English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese',
    'Korean', 'Hindi', 'Italian', 'Russian', 'Portuguese', 'Arabic',
    'Turkish', 'Dutch', 'Greek', 'Polish', 'Swedish', 'Norwegian',
    'Finnish', 'Danish'
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/random/<category>')
def random_choice(category):
    if category == 'genre':
        choice = random.choice(genres)
    elif category == 'year':
        choice = random.choice(years)
    elif category == 'language':
        choice = random.choice(languages)
    else:
        return jsonify({'error': 'Invalid category'})
    
    return jsonify({'choice': choice})

if __name__ == '__main__':
    app.run(debug=True)
