![Resume Analyser CI](https://github.com/xl402/ResumeAnalyser/actions/workflows/resume_analyser.yaml/badge.svg?branch=main)

# ResumeAnalyser
## Usage
```python
import fitz

from resume_analyser import ResumeAnalyser

resume = fitz.open('~/example_resume.pdf')
analyser = ResumeAnalyser(category='builder')
result = analyser.run(resume)

print(result.text_analysis)
print(result.score)
result.output_pdf.save('analysed_resume_output.pdf')
```
