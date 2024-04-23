from flask import Flask, request, render_template
import joblib

app = Flask(__name__, static_url_path='/static')

# Load the model and the label encoder
pipeline = joblib.load('music_genre_classifier.pkl')
label_encoder = joblib.load('music_genre_label_encoder.pkl')

@app.route('/', methods=['GET', 'POST'])  # Allowing both GET and POST methods
def index():
    if request.method == 'POST':
        # Get lyrics from the form
        lyrics = request.form['lyrics']
        # Use the model to predict the genre
        genre = predict_genre(lyrics)
        return render_template('index.html', genre=genre)
    else:
        # No form submission, show the form
        return render_template('index.html', genre=None)

def predict_genre(lyrics):
    lyrics = [lyrics.lower()]  # Our model expects a list of items
    lyrics_transformed = pipeline['tfidf'].transform(lyrics)
    genre_code = pipeline['clf'].predict(lyrics_transformed)
    genre = label_encoder.inverse_transform(genre_code)
    return genre[0]

if __name__ == '__main__':
    app.run(debug=True)
