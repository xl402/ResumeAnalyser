import base64
import os

from fastapi.testclient import TestClient
import fitz
import pytest

from resume_analyser.server import app

SERVER_URL = "http://127.0.0.1:8000"
client = TestClient(app)


def test_resume_analyser_server_end_to_end(example_resume_path, tmp_path):
    files = {'file': ('example_resume.pdf', open(example_resume_path, 'rb'), 'application/pdf')}
    response = client.post(f'{SERVER_URL}/analyse-resume', files=files)
    
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data['text_analysis'], str)
    assert isinstance(data['score'], float)
    assert isinstance(data['output_pdf'], str)

    pdf_content = base64.b64decode(data['output_pdf'])
    output_pdf_path = tmp_path / "returned_resume.pdf"
    with open(output_pdf_path, 'wb') as f:
        f.write(pdf_content)
    doc = fitz.open(str(output_pdf_path))
    assert len(doc) > 0
