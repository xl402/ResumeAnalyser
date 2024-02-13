import base64
import os

from fastapi.testclient import TestClient
import fitz
import pytest

from resume_analyser.server import app

client = TestClient(app)


def test_resume_analyser_server_end_to_end(payload):
    response = client.post('/analyse-resume', files=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data['text_analysis'], str)
    assert isinstance(data['score'], float)
    assert isinstance(data['output_pdf'], str)


def test_resume_analyser_server_can_decode_output_pdf(payload, tmp_path):
    response = client.post('/analyse-resume', files=payload)
    data = response.json()

    pdf_content = base64.b64decode(data['output_pdf'])
    doc = fitz.open(stream=pdf_content, filetype='pdf')
    assert len(doc) > 0


@pytest.fixture
def payload(example_resume_path):
    files = {'file': ('example_resume.pdf', open(example_resume_path, 'rb'), 'application/pdf')}
    return files
