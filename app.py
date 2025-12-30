import cv2, os, uuid, requests, numpy as np
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import RedirectResponse
from ultralytics import YOLO

app = FastAPI(title="Projekt - Wykrywanie Ludzi")
zadania = {}
model = YOLO("yolov8m.pt")

def wykonaj_zadanie(tid, img, nazwa):
    wyniki = model.predict(img, classes=[0], conf=0.25)
    ile = sum(len(r.boxes) for r in wyniki)
    for r in wyniki:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imwrite(nazwa, img)
    zadania[tid] = {"status": "gotowe", "osoby": ile, "foto": nazwa}

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

@app.get("/detect-local")
def z_dysku(bt: BackgroundTasks, plik: str = "foto.jpg"):
    if not os.path.exists(plik): return {"blad": "Brak pliku"}
    tid = str(uuid.uuid4())
    zadania[tid] = {"status": "pracuję"}
    bt.add_task(wykonaj_zadanie, tid, cv2.imread(plik), f"wynik_{tid}.jpg")
    return {"task_id": tid}

@app.get("/detect-url")
def z_internetu(bt: BackgroundTasks, link: str):
    tid = str(uuid.uuid4())
    try:
        res = requests.get(link, timeout=10)
        img = cv2.imdecode(np.frombuffer(res.content, np.uint8), cv2.IMREAD_COLOR)
        zadania[tid] = {"status": "pracuję"}
        bt.add_task(wykonaj_zadanie, tid, img, f"wynik_{tid}.jpg")
        return {"task_id": tid}
    except:
        return {"blad": "Nie udało się pobrać zdjęcia"}

@app.get("/sprawdz/{tid}")
def status(tid: str):
    return zadania.get(tid, {"info": "Nie ma takiego ID"})
