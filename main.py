from fastapi import FastAPI, Request, Form, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import shutil
import os

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

response = model.generate_content("The opposite of hot is")
print(response.text)

app = FastAPI()

# Serve the static files for the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

"""
@app.get("/")
def read_root():
    return{"text": "An API for generating data"}

@app.post("/generate")
def generate_data():
    return {"text": "data generated successfully"}
"""

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_data(prompt: str = Form(...), file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
    
    # Save the uploaded file to the data directory
    file_location = f"data/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Read the CSV file and prepare the prompt
    df = pd.read_csv(file_location)
    reviews = df['review'].tolist()  # Assuming the CSV has a column named 'review'
    prompt_with_data = f"{prompt} {reviews}"

    # Generate content using the Gemini AI API
    response = model.generate_content(prompt_with_data)
    
    # Clean up the data directory
    os.remove(file_location)
    
    return {"text": response.text}