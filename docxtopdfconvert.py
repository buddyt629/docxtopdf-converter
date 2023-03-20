from fastapi import FastAPI, UploadFile, File
import aspose.words as aw
from io import BytesIO

app = FastAPI()

@app.post("/convert_to_pdf")
async def convert_to_pdf(file: UploadFile = File(...)):
    # Read the uploaded file as binary data
    contents = await file.read()

    # Load word document from binary data
    stream = BytesIO(contents)
    doc = aw.Document(stream)

    # Save as PDF
    doc.save("PDF.pdf")

    return {"message": "File converted successfully!"}
##main.py