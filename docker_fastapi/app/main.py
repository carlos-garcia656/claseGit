from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/myname/{name}")
async def myName(name: str):
    return {"message": f"Hello {name} this is my fastapi"}
