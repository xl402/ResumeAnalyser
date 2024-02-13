import os

import fitz
import pytest

from resume_analyser import ResumeAnalyser


def test_resume_analyser_end_to_end(example_resume_path):
    analyser = ResumeAnalyser()
    resume = fitz.open(example_resume_path)
    result = analyser.run(resume)

    assert isinstance(result.text_analysis, str)
    assert isinstance(result.output_pdf, fitz.Document)
    assert isinstance(result.score, float)
