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
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()


def get_resume_feedback(resume):

    parser = JsonOutputParser(
        # pydantic_object={
        #     "type": "object",
        #     "properties": {
        #         "feedback": {"type": "array", "items": {"type": "string"}},
        #     },
        #     "required": ["feedback"],
        # }
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a professional career coach and ATS expert. Analyze the following resume text and provide only critical, constructive feedback to improve the resume for job applications.
                If you feel there is no need to update the resume then say so.
                Return only the feedback as a JSON object in the following format:
                    {{"feedback": ["<point 1>", "<point 2>", "..."]}}

                Do not include any introductions, conclusions, explanations, or additional fields—only the JSON object.
                NOTE:ONLY GIVE THE FEEDBACK. DO NOT GIVE UNECESSARY FEEDBACK. DO NOT ADD CONCLUSION OR INTRODUCTION ONLY STRICTLY JSON FORMAT

                Resume Text:{resume}""",
            ),
        ]
    )

    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=1)

    chain = prompt | model | parser

    response = chain.invoke({"resume": resume})

    return response.get("feedback",[])


def apply_feedback(resume: str, feedback: list):
    parser = JsonOutputParser(
        pydantic_object={
            "type": "Object",
            "properties": {
                "updated_resume": {"type": "string"},
            },
            "required": ["updated_resume"],
        }
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a professional resume writer and AI assistant. Based on the feedback below, rewrite the given resume in Markdown format and
                return the entire resume that follows a professional format.

                - Do not fabricate or assume information. If you do not have the required information refrain from applying the feedback
                - Keep the formatting clean and ATS-friendly.
                - Do not include any explanations, headings, or markdown code fences like ```json or ```markdown.


                Input:
                Feedback: {feedback}
                Resume: {resume}

                Respond with a JSON object in the following format only.
                NOTE:STRICTLY FOLLOW THE FORMAT GIVEN BELOW.IF YOU DO NOT KNOW ANY INFOMATION LEAVE IT BLANK AND DO NOT
                IMPLEMENT THAT FEEDBACK.

                You must respond with a pure JSON object like this:
                OUTPUT FORMAT:
                {{
                "updated_resume": "..."
                }}

                Do not add any text outside the JSON object.
            """,
            )
        ]
    )

    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=1)

    chain = prompt | model | parser

    response = chain.invoke({"resume": resume, "feedback": feedback})
    return response["updated_resume"]


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

    feedback = get_resume_feedback(resume)
    print(feedback, type(feedback))
    # if feedback:
    #     apply_feedback(resume, feedback)
