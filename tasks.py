from uuid import uuid4

# słownik na zadania
# klucz: id zadania
# wartość: status i wynik
tasks = {}


def create_task():
    task_id = str(uuid4())

    tasks[task_id] = {
        "status": "pending",   # zadanie jeszcze się wykonuje
        "result": None
    }

    return task_id


def finish_task(task_id, result):
    tasks[task_id]["status"] = "done"
    tasks[task_id]["result"] = result
