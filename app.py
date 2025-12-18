import cv2
import os
import uuid
import requests
import numpy as np
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import RedirectResponse
from ultralytics import YOLO

app = FastAPI(title="Projekt - Wykrywanie Ludzi")

# To jest Twoja "kolejka" i magazyn wyników
zadania = {}

# Model YOLO - wykryje każdego, nawet na zdjęciu reprezentacji
model = YOLO('yolov8m.pt')


@app.get("/")
def strona_glowna():
    # To naprawia Twój błąd 404 - od razu przenosi do panelu docs
    return RedirectResponse(url="/docs")


def wykonaj_zadanie(id_zadania, obrazek, nazwa_pliku):
    # Wykrywanie osób (klasa 0 to 'person')
    wyniki = model.predict(obrazek, classes=[0], conf=0.25)

    ile_osob = 0
    for r in wyniki:
        ile_osob += len(r.boxes)
        # Rysowanie ramek [cite: 17]
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(obrazek, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite(nazwa_pliku, obrazek)

    # Zapisujemy wynik, żeby można było go sprawdzić później
    zadania[id_zadania] = {"status": "gotowe", "osoby": ile_osob, "foto": nazwa_pliku}


@app.get("/detect-local")
def z_dysku(background_tasks: BackgroundTasks, plik: str = "foto.jpg"):
    if not os.path.exists(plik):
        return {"blad": "Brak pliku foto.jpg"}

    id_zadania = str(uuid.uuid4())
    zadania[id_zadania] = {"status": "pracuję"}

    obrazek = cv2.imread(plik)
    # Wrzucenie na kolejkę (asynchronicznie)
    background_tasks.add_task(wykonaj_zadanie, id_zadania, obrazek, f"wynik_{id_zadania}.jpg")

    return {"task_id": id_zadania}  # Zwracamy ID


@app.get("/detect-url")
def z_internetu(background_tasks: BackgroundTasks, link: str):
    id_zadania = str(uuid.uuid4())
    zadania[id_zadania] = {"status": "pracuję"}

    try:
        odp = requests.get(link, timeout=10)
        bity = np.frombuffer(odp.content, np.uint8)
        obrazek = cv2.imdecode(bity, cv2.IMREAD_COLOR)

        # Wrzucenie na kolejkę
        background_tasks.add_task(wykonaj_zadanie, id_zadania, obrazek, f"wynik_{id_zadania}.jpg")
        return {"task_id": id_zadania}
    except:
        return {"blad": "Nie udało się pobrać zdjęcia"}


@app.get("/sprawdz/{task_id}")
def status(task_id: str):
    # Sprawdzanie wyniku zadania
    wynik = zadania.get(task_id)
    if not wynik:
        return {"info": "Nie ma takiego ID"}
    return wynik