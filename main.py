from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def main():
  return {"Hello": "Test"}

@app.get("/route")
def route():
  raise HTTPException(500)
  