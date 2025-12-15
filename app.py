import csv
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# --- 1. KONFIGURACJA ---
app = Flask(__name__)

# Ustalanie ścieżki do bazy danych
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'movies.db')

# Konfiguracja SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# --- 2. MODELE DANYCH ---

class Movie(db.Model):
    __tablename__ = 'movies'
    movieId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genres = db.Column(db.String)

    def to_json(self):
        return {
            "movieId": self.movieId,
            "title": self.title,
            "genres": self.genres
        }


class Link(db.Model):
    __tablename__ = 'links'
    movieId = db.Column(db.Integer, primary_key=True)
    imdbId = db.Column(db.String)
    tmdbId = db.Column(db.String)

    def to_json(self):
        return {
            "movieId": self.movieId,
            "imdbId": self.imdbId,
            "tmdbId": self.tmdbId
        }


class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    movieId = db.Column(db.Integer)
    rating = db.Column(db.Float)
    timestamp = db.Column(db.String)

    def to_json(self):
        return {
            "userId": self.userId,
            "movieId": self.movieId,
            "rating": self.rating,
            "timestamp": self.timestamp
        }


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    movieId = db.Column(db.Integer)
    tag = db.Column(db.String)
    timestamp = db.Column(db.String)

    def to_json(self):
        return {
            "userId": self.userId,
            "movieId": self.movieId,
            "tag": self.tag,
            "timestamp": self.timestamp
        }


# --- 3. FUNKCJA DO ŁADOWANIA DANYCH ---
def import_data():
    print("--- Sprawdzam pliki CSV i bazę danych... ---")

    # Filmy
    if Movie.query.first() is None:
        print("Wczytuje movies.csv...")
        try:
            path = os.path.join(basedir, 'movies.csv')
            with open(path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    movie = Movie(movieId=int(row['movieId']), title=row['title'], genres=row['genres'])
                    db.session.add(movie)
                db.session.commit()
        except Exception as e:
            print(f"Blad movies: {e}")
    else:
        print("Filmy OK.")

    # Linki
    if Link.query.first() is None:
        print("Wczytuje links.csv...")
        try:
            path = os.path.join(basedir, 'links.csv')
            with open(path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    link = Link(movieId=int(row['movieId']), imdbId=row['imdbId'], tmdbId=row['tmdbId'])
                    db.session.add(link)
                db.session.commit()
        except Exception as e:
            print(f"Blad links: {e}")
    else:
        print("Linki OK.")

    # Tagi
    if Tag.query.first() is None:
        print("Wczytuje tags.csv...")
        try:
            path = os.path.join(basedir, 'tags.csv')
            with open(path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tag = Tag(userId=int(row['userId']), movieId=int(row['movieId']), tag=row['tag'],
                              timestamp=row['timestamp'])
                    db.session.add(tag)
                db.session.commit()
        except Exception as e:
            print(f"Blad tags: {e}")
    else:
        print("Tagi OK.")

    # Oceny
    if Rating.query.first() is None:
        print("Wczytuje ratings.csv (czekaj)...")
        try:
            path = os.path.join(basedir, 'ratings.csv')
            with open(path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                licznik = 0
                for row in reader:
                    rating = Rating(userId=int(row['userId']), movieId=int(row['movieId']), rating=float(row['rating']),
                                    timestamp=row['timestamp'])
                    db.session.add(rating)
                    licznik += 1
                    if licznik % 1000 == 0:
                        db.session.commit()
                db.session.commit()
        except Exception as e:
            print(f"Blad ratings: {e}")
    else:
        print("Oceny OK.")


# --- 4. ENDPOINTY ---

@app.route('/')
def home():
    return jsonify({'hello': 'world'})


@app.route('/movies')
def get_movies():
    return jsonify([m.to_json() for m in Movie.query.all()])


@app.route('/links')
def get_links():
    return jsonify([l.to_json() for l in Link.query.all()])


@app.route('/tags')
def get_tags():
    return jsonify([t.to_json() for t in Tag.query.all()])


@app.route('/ratings')
def get_ratings():
    return jsonify([r.to_json() for r in Rating.query.limit(100).all()])


# --- 5. START SERWERA ---

with app.app_context():
    db.create_all()
    import_data()

print("=" * 40)
print("SERWER DZIAŁA! Kliknij w linki poniżej:")
print("http://127.0.0.1:5000/movies")
print("http://127.0.0.1:5000/links")    # Dopisane
print("http://127.0.0.1:5000/tags")     # Dopisane
print("http://127.0.0.1:5000/ratings")
print("=" * 40)

app.run(debug=True, port=5000)