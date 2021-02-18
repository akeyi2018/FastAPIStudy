import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/name/{name}")
async def showname(name):
    return {"name": name}

if __name__ == "__app__":
    uvicorn.run(app, host="0.0.0.0", port=8000)