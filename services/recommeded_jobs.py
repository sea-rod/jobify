# Copyright 2025 Seamus.F.Rodrigues
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate

from pydantic import BaseModel
from typing import List


class Skills(BaseModel):
    domain: str
    technical_skills: List[str]
    methodologies: List[str]
    soft_skills: List[str]
    certifications: List[str]
    languages: List[str]
    tools: List[str]
    industry_knowledge: List[str]


def recommend_jobs(resume: str):
    parser = JsonOutputParser(
        pydantic_object=Skills
    )
    example_prompt = PromptTemplate.from_template(
        "Resume:\n{resume}\n\skills:\n{skills}"
    )

    examples = [
        {
            "resume": """John Doe
Software Engineer with 3+ years of experience in full-stack development, cloud infrastructure, and Agile methodologies.
Skills: Python, JavaScript, React, Django, AWS, Docker, Git, Jenkins, MongoDB
Certifications: AWS Certified Solutions Architect - Associate, Scrum Master (CSM)
Soft skills: Teamwork, Problem-solving, Communication""",
            "skills": """{{"domain": "Software Engineering",
  "technical_skills": ["Python", "JavaScript", "React", "Django", "MongoDB", "Docker", "Git", "Jenkins"],
  "methodologies": ["Agile", "Scrum"],
  "soft_skills": ["Teamwork", "Problem-solving", "Communication"],
  "certifications": ["AWS Certified Solutions Architect - Associate", "Scrum Master Certification (CSM)"],
  "languages": [],
  "tools": [],
  "industry_knowledge": []
}}""",
        },
        {
            "resume": """Jane Smith
Marketing Manager with 5+ years in digital strategy, content marketing, and SEO.
Skills: SEO, Google Ads, Google Analytics, HubSpot, Copywriting, Social Media
Certifications: HubSpot Inbound Marketing, Google Ads Certification
Languages: English, Spanish
Soft Skills: Creativity, Collaboration, Leadership""",
            "skills": """{{
  "domain": "Marketing",
  "technical_skills": ["SEO", "Google Ads", "Google Analytics", "Copywriting"],
  "methodologies": ["Digital Strategy", "Content Marketing"],
  "soft_skills": ["Creativity", "Collaboration", "Leadership"],
  "certifications": ["HubSpot Inbound Marketing", "Google Ads Certification"],
  "languages": ["English", "Spanish"],
  "tools": ["HubSpot", "Google Ads", "Google Analytics"],
  "industry_knowledge": ["Lead Generation", "Digital Marketing"]
}}""",
        },
        {
            "resume": """Alex White
Cybersecurity Analyst with experience in penetration testing, SIEM tools, and incident response.
Tools: Wireshark, Nessus, Splunk, Kali Linux
Certifications: CompTIA Security+, CEH
Soft Skills: Critical thinking, Problem-solving, Attention to detail""",
            "skills": """{{
  "domain": "Cybersecurity",
  "technical_skills": ["Penetration Testing", "Incident Response"],
  "methodologies": ["SIEM", "Vulnerability Assessment"],
  "soft_skills": ["Critical thinking", "Problem-solving", "Attention to detail"],
  "certifications": ["CompTIA Security+", "Certified Ethical Hacker (CEH)"],
  "languages": [],
  "tools": ["Wireshark", "Nessus", "Splunk", "Kali Linux"],
  "industry_knowledge": ["Cybersecurity", "Network Security"]
}}""",
        },
        {
            "resume": """Priya Mehta
Financial Analyst with expertise in financial modeling, budgeting, and reporting.
Tools: Excel, Power BI, SAP
Certifications: CFA Level 1, CPA (India)
Soft Skills: Analytical thinking, Accuracy, Time management
Languages: English, Hindi""",
            "skills": """{{
  "domain": "Finance",
  "technical_skills": ["Financial Modeling", "Budgeting", "Forecasting", "Reporting"],
  "methodologies": ["Financial Analysis", "Variance Analysis"],
  "soft_skills": ["Analytical thinking", "Accuracy", "Time management"],
  "certifications": ["CFA Level 1", "CPA (India)"],
  "languages": ["English", "Hindi"],
  "tools": ["Excel", "Power BI", "SAP"],
  "industry_knowledge": ["Corporate Finance", "Accounting Standards"]
}}""",
        },
    ]

    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="""
        You are an intelligent resume parser. Extract structured skill information from the following resumes. Follow the format 
        given below and ONLY return the json format
        NOTE:DO NOT ADD CONCLUSION OR INTRODUCTION ONLY STRICTLY JSON FORMAT """,
        suffix="Resume:\n{resume}",
        input_variables=["resume"],
        example_separator="\n\n---\n\n",
    )
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=1)

    chain = few_shot_prompt | model | parser
    
    res = chain.invoke({"resume":resume})

    print(res)


if __name__ == "__main__":
    resume = """John Doe
    📍 San Francisco, CA | 📞 (123) 456-7890 | ✉️ john.doe@email.com | 🌐 linkedin.com/in/johndoe

    Professional Summary
    Highly motivated and detail-oriented professional with experience in software development, team collaboration, and project management. Strong passion for technology and innovation. Seeking opportunities to contribute to high-performing engineering teams.

    Work Experience
    Software Engineer
    ABC Tech Solutions, San Francisco, CA
    Jan 2021 - Present

    Developed internal tools using Python and Flask, improving process efficiency by 25%.

    Collaborated with cross-functional teams to launch 3 key features on the main product.

    Wrote unit and integration tests resulting in 30% fewer bugs during QA.

    Junior Developer
    CodeWave Inc., Remote
    Jun 2019 - Dec 2020

    Maintained and upgraded legacy applications in PHP and JavaScript.

    Participated in code reviews and agile sprints.

    Worked on client-facing features under tight deadlines.

    Education
    Bachelor of Science in Computer Science
    University of California, Davis
    2015 - 2019

    Skills
    Programming: Python, JavaScript, HTML, CSS, SQL

    Frameworks: Flask, React

    Tools: Git, Docker, Jira, Postman

    Soft Skills: Communication, Problem-solving, Teamwork"""

    recommend_jobs(resume)
