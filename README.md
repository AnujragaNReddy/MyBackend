# MyBackend FastAPI Project

## Folder Structure

```
MyBackend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routers/
│       ├── __init__.py
│       └── root.py
│
├── README.md
```

## How to Run

From the MyBackend directory, run:

D:/NAG/Code/Python/.venv/Scripts/python.exe -m uvicorn app.main:app --reload

This will start the server at http://127.0.0.1:8000

Visit http://127.0.0.1:8000/docs for the interactive API docs.
