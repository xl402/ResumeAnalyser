import base64

import fitz
from fastapi import FastAPI, File, UploadFile

from resume_analyser.analyser import ResumeAnalyser

app = FastAPI()


@app.post("/analyse-resume")
async def analyse_resume(file: UploadFile = File(...)):
    content = await file.read()

    analyser = ResumeAnalyser()
    resume = _decode_content_to_pdf(content)
    analysis_result = analyser.run(resume)

    output_pdf = analysis_result.output_pdf.tobytes()
    output_pdf_base64 = base64.b64encode(output_pdf).decode('utf-8')
    return {
        "text_analysis": analysis_result.text_analysis,
        "score": analysis_result.score,
        "output_pdf": output_pdf_base64,
    }


def _decode_content_to_pdf(content_bytes):
    pdf_document = fitz.open(stream=content_bytes, filetype="pdf")
    return pdf_document
