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


import markdown
from weasyprint import HTML


def markdown_to_pdf(markdown_text: str, output_pdf_path: str):
    """Converts Markdown text to a PDF file."""
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_text)

    # Create a full HTML document (optional but good for styling)
    full_html = f"""
    <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: #333;
                }}
                p {{
                    margin: 10px 0;
                }}
                ul, ol {{
                    margin: 10px 20px;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
    </html>
    """

    # Convert the HTML to a PDF
    HTML(string=full_html).write_pdf(output_pdf_path)
    return True
    # print(f"PDF created successfully at: {output_pdf_path}")

if "__main__"==__name__:
    markdown_text = """
                    # Jobify

**Jobify** is your friendly AI-powered resume assistant. It helps you improve your resume so you land more interviews, and even suggests jobs that match your skills. With Jobify, you can easily upload your current resume and let intelligent tools analyze it. Think of it as having a personal career coach that checks your resume for you and gives practical tips to stand out.

---

## ✨ Key Features

- **📄 Upload Your Resume:**  
  Quickly upload your resume (PDF, Word, etc.) to Jobify. Your resume is saved securely in your account so you can access it anytime.

- **🤖 ATS-Friendly Suggestions:**  
  Jobify’s AI analyzes your resume and gives smart suggestions to make it **ATS-friendly**. These may include:
  - Adding important keywords
  - Improving formatting
  - Clarifying sections for automated resume scanners

- **🛠️ One-Click Improvements:**  
  View suggestions in an easy-to-read list. You can apply changes automatically with just one click — no need to manually edit your resume.

- **💼 Smart Job Matches:**  
  Based on your resume content, Jobify finds job openings that match your skills and experience. Browse personalized job recommendations directly in the app.

- **🎯 Tailor Your Resume to Jobs:**  
  Provide a job description, and Jobify will suggest how to customize your resume for that specific role. Tailoring includes:
  - Highlighting relevant skills
  - Adjusting your summary
  - Using keywords from the job posting

---

## 🚀 How It Works

1. **Sign In & Upload:**  
   Create a free account and upload your latest resume.

2. **Review AI Suggestions:**  
   Let Jobify analyze your resume and present easy-to-understand improvement tips.

3. **Apply Changes:**  
   Accept the suggestions you like and Jobify will update your resume for you.

4. **Find Jobs That Fit You:**  
   Explore curated job listings matched to your profile.

5. **Tailor for Specific Applications:**  
   Paste a job description and get a tailored resume version ready to send.

---

Jobify takes the guesswork out of job hunting. Whether you're updating your resume or applying to your dream job, Jobify's smart tools make the process easier, faster, and more effective.

> 🙌 Build a better resume. Apply smarter. Land more interviews — with **Jobify**.

                    """
    html_content = markdown.markdown(markdown_text)
    print(html_content)
