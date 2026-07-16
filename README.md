# AI Resume Screening System

An AI-powered resume screening system that uses Large Language Models to analyze resumes and compare them against HR requirements.

The system extracts information from PDF and DOCX resumes, performs ATS-style matching, and evaluates whether a candidate is suitable for a given role.

---

## Features

- Resume Parsing
  - PDF support
  - DOCX support

- Candidate Information Extraction
  - Name
  - Skills
  - Projects
  - Experience

- ATS Matching

- Percentage Scoring
  - Skills match
  - Experience match
  - Project match

- Candidate Eligibility Analysis

- Structured JSON Output using Pydantic

- LLM powered analysis using Groq API

---

## Tech Stack

- Python
- Groq API
- GPT-OSS-120B
- Pydantic
- PyMuPDF
- Python-DOCX
- dotenv

---

## Project Workflow

1. Upload a resume.
2. Extract resume text.
3. Define HR requirements.
4. Send the data to the LLM.
5. Extract structured information.
6. Compare candidate skills with company requirements.
7. Calculate matching percentages.
8. Determine eligibility.

---

## Example HR Requirements

```python
{
    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "FastAPI"
    ],
    "experience": [
        "6 months internship"
    ],
    "projects": [
        "AI Project"
    ]
}
```

---

## Example Output

```json
{
    "name":"Roshan Kumar",

    "skills":[
        "Python",
        "SQL",
        "FastAPI"
    ],

    "projects":[
        "Resume Screening System"
    ],

    "experience":[
        "Backend Internship"
    ],

    "matching_percentage":{
        "skills":75,
        "experience":100,
        "projects":80
    },

    "eligible":true
}
```

---

## Installation

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-System.git

cd AI-Resume-Screening-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file:

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
python main.py
```

---

## Future Improvements

- Web Interface using FastAPI
- Resume Upload API
- ATS Score out of 100
- Multiple Job Description Support
- Semantic Skill Matching
- Resume Suggestions
- Missing Skills Recommendation
- Docker Deployment

---

## License

MIT License
