from dataclasses import dataclass

from pydantic import BaseModel

from resume_analyser.schemas import AnalysisResult


class ResumeAnalyser():
    def run(self, resume):
        result = AnalysisResult(
                text_analysis='',
                output_pdf=resume,
                score=0
                )
        return result
