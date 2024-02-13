![Resume Analyser CI](https://github.com/xl402/ResumeAnalyser/actions/workflows/resume_analyser.yaml/badge.svg?branch=main)

# ResumeAnalyser

**Goal**: Algorithmically determine resume quality to reduce bias

**Method**: Get an analyser to
1. Score a given resume
2. Output text-based analysis
3. Output the original resume with highlited areas for sanity checking

**Verification:**
Must be able to backtest with known good / bad resumes

## Usage
Add the repo to your path
```sh
PYTHONPATH="$PATH_TO_REPO/ResumeAnalyser/src:$PYTHONPATH"
```

```python
import fitz

from resume_analyser import ResumeAnalyser

resume = fitz.open('example_resume.pdf')

analyser = ResumeAnalyser()
result = analyser.run(resume)

print(result.text_analysis)
print(result.score)
result.output_pdf.save('analysed_resume_output.pdf')
```

## Backtest
```python
from resume_analyser import ResumeAnalyser
from resume_backtester import BackTester

analyser = ResumeAnalyser()
backtester = BackTester('labelled_resumes_data_dir')
result = backtester.run(analyser, regret_threshold=7.0)

print(result.catastrophic_loss)
print(result.score)
```

## Sending Request To Server

```python
import requests
import fitz

URL = # Server URL

files = {'file': ('example_resume.pdf', open(example_resume_path, 'rb'), 'application/pdf')}

response = requests.post(f'{URL}/analyse-resume', files=payload)
data = response.json()

pdf_content = base64.b64decode(data['output_pdf'])
doc = fitz.open(stream=pdf_content, filetype='pdf')
```
