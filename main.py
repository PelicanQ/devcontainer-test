from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def main():
  return {"Hello": "Nuts"}

@app.get("/route")
def route():
  raise HTTPException(500)
  