import csv
import os
from flask import Flask, jsonify

app = Flask(__name__)

# --- 1. KONFIGURACJA ŚCIEŻEK ---

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# --- 2. MODELE DANYCH ---
class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


# --- 3. INTELIGENTNE WCZYTYWANIE DANYCH ---
def load_data(filename, class_model):

    full_path = os.path.join(BASE_DIR, filename)

    # SPRAWDZENIE CZY PLIK ISTNIEJE
    if not os.path.exists(full_path):
        print(f"[BŁĄD] Nie widzę pliku pod adresem: {full_path}")
        return [{"ERROR": f"Brakuje pliku! Szukam go tutaj: {full_path}. Sprawdź folder."}]

    data_list = []
    try:
        with open(full_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            for row in reader:
                if row:
                    try:

                        obj = class_model(*row)
                        data_list.append(obj.__dict__)
                    except TypeError:
                        continue  # Ignorujemy błędne wiersze
                    except Exception as e:
                        continue

    except Exception as e:
        return [{"ERROR": f"Błąd podczas czytania pliku: {str(e)}"}]

    return data_list


# --- 4. ENDPOINTY ---

@app.route('/')
def hello():
    return jsonify({'hello': 'world', 'status': 'Serwer działa poprawnie'})


@app.route('/movies')
def get_movies():
    return jsonify(load_data('movies.csv', Movie))


@app.route('/links')
def get_links():
    return jsonify(load_data('links.csv', Link))


@app.route('/ratings')
def get_ratings():

    data = load_data('ratings.csv', Rating)

    if len(data) > 0 and "ERROR" in data[0]:
        return jsonify(data)
    return jsonify(data[:100])


@app.route('/tags')
def get_tags():
    return jsonify(load_data('tags.csv', Tag))


# --- 5. START SERWERA ---
if __name__ == '__main__':
    print(f"--- SERWER STARTUJE ---")
    print(f"Szukam plików w folderze: {BASE_DIR}")
    print(f"Upewnij się, że są tam pliki: movies.csv, links.csv, ratings.csv, tags.csv")
    app.run(debug=True, port=5000)