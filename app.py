import cv2, os, uuid, requests, numpy as np
from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from fastapi.responses import RedirectResponse
from ultralytics import YOLO

app = FastAPI(title="Projekt - Wykrywanie Ludzi")
zadania = {}
model = YOLO("yolov8m.pt")

os.makedirs("wyniki", exist_ok=True)


def wykonaj_zadanie(tid, img, nazwa_pliku):
    if img is None:
        zadania[tid] = {"status": "błąd", "info": "Nie udało się wczytać obrazu"}
        return

    wyniki = model.predict(img, classes=[0], conf=0.25)
    ile = sum(len(r.boxes) for r in wyniki)

    for r in wyniki:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    sciezka_wynikowa = os.path.join("wyniki", nazwa_pliku)
    cv2.imwrite(sciezka_wynikowa, img)

    zadania[tid] = {
        "status": "gotowe",
        "osoby": ile,
        "foto_url": sciezka_wynikowa
    }


@app.get("/")
def home():
    return RedirectResponse(url="/docs")


@app.get("/detect-local")
def z_dysku(bt: BackgroundTasks, plik: str = "foto.jpg"):
    if not os.path.exists(plik): return {"blad": "Brak pliku na serwerze"}
    tid = str(uuid.uuid4())
    zadania[tid] = {"status": "pracuję"}
    bt.add_task(wykonaj_zadanie, tid, cv2.imread(plik), f"local_{tid}.jpg")
    return {"task_id": tid}


@app.get("/detect-url")
def z_internetu(bt: BackgroundTasks, link: str):
    tid = str(uuid.uuid4())
    try:
        res = requests.get(link, timeout=10)
        res.raise_for_status()
        img_array = np.frombuffer(res.content, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        zadania[tid] = {"status": "pracuję"}
        bt.add_task(wykonaj_zadanie, tid, img, f"url_{tid}.jpg")
        return {"task_id": tid}
    except Exception as e:
        return {"blad": f"Nie udało się pobrać zdjęcia: {str(e)}"}


@app.post("/detect-upload")
async def z_uploadu(bt: BackgroundTasks, file: UploadFile = File(...)):
    tid = str(uuid.uuid4())

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    zadania[tid] = {"status": "pracuję"}
    bt.add_task(wykonaj_zadanie, tid, img, f"upload_{tid}.jpg")

    return {"task_id": tid}


@app.get("/sprawdz/{tid}")
def status(tid: str):
    return zadania.get(tid, {"info": "Nie znaleziono zadania o takim ID"})