from fastapi import FastAPI, UploadFile, File
from pdf_reader import extract_text_from_pdf
import shutil
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag import get_answer

app = FastAPI()

# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Financial Document Summarizer API is running"}


@app.post("/ask")
def ask_question(data: Question):
    print("Received question:", data.question)

    answer = get_answer(data.question)

    print("Answer generated successfully!")

    return {
        "question": data.question,
        "answer": answer
    }
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    with open("uploaded.pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extract_text_from_pdf("uploaded.pdf")

    return {
        "message": "PDF uploaded and processed successfully",
        "filename": file.filename
    }