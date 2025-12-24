import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain import PromptTemplate


load_dotenv()   # 👈 THIS IS REQUIRED

class ColdEmailChain:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),  # ✅ correct
            model_name="llama-3.1-8b-instant"

        )

        self.prompt = PromptTemplate(
            input_variables=["job", "projects"],
            template="""
You are a software developer applying for a job.

Job Description:
{job}

Relevant Portfolio:
{projects}

Write a professional cold email.
"""
        )

    def generate(self, job_desc, portfolio):
        return self.llm.invoke(
            self.prompt.format(job=job_desc, projects=portfolio)
        ).content
