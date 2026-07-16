import os;
from groq import Groq; 
from dotenv import load_dotenv;
from pathlib import Path;
from pydantic import BaseModel
import fitz
from docx import Document

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api key is not there!")

Client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"

file_path="resume.docx"

text1=""
text2=""
if file_path.endswith(".pdf"):
    doc1=fitz.open("resume.pdf")
    for page in doc1:
        text+=doc1.get_text()
elif file_path.endswith(".docx"):
    doc2= Document("resume.docx")
    text2="\n".join([p.text for p in doc2.paragraphs])
    


class user_resume(BaseModel):
    name:str
    skills:list
    project:list
    experience:list

class percent(BaseModel):
    skills:int
    experience:int
    projects:int

schema=user_resume.model_json_schema()
schema1=percent.model_json_schema()

hr_requirements = {

"skills":[
"Python",
"SQL",
"Machine Learning",
"FastAPI"
],

"experience":[
"6 months internship"
],

"projects":[
"AI Project"
]

}
response_format={
    "type":"json_object"
}


system_prompt=f"""You have to give the output using {text1} and {text2} and provide the output strictly in the given schema {schema} and in json format and also provide the percentage of the maching of the details in the {text1} or {text2} with {hr_requirements} in the schema {schema1} and also provide the percentage of the eligibility of the user for our company like if the user is applicable for use or not in json format"""

text=f"""I am giving you the requirements for the jobs {hr_requirements} and {text1} and{text2} give me the details and provide me the percentage of skills, experience and projects and if the candidate is fit for the job or not."""

message_system={
    "role":"system",
    "content":system_prompt
}

role="user"
prompt=f"""Give details of the user from {text}"""

message={
    "role":role,
    "content":prompt,
}

messages=[message_system,message]

response=Client.chat.completions.create(model=model,messages=messages,response_format=response_format)

answer=response.choices[0].message.content

print(answer)










