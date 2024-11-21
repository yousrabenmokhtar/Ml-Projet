from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/train")
def train():
  return {"message": "Hello Youssra"}