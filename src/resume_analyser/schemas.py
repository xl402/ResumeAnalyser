from pydantic import BaseModel
import fitz


class FitzDocument:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, fitz.Document):
            message = f"Expected fitz.Document, received {type(v)}"
            raise ValueError(message)
        return v


class AnalysisResult(BaseModel):
    text_analysis: str
    output_pdf: FitzDocument
    score: float
