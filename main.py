from fastapi import FastAPI, UploadFile, File
from ai_agent import analyze_resume

app = FastAPI()

@app.get("/")
def home():
    return {"message": "VidyaGuide AI Backend Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    result = analyze_resume(text)

    return {"analysis": result}