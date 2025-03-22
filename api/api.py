from fastapi import FastAPI

# Utilizarei api futuramente...um app esta por vir??? ;)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Futura implementação....!"}

