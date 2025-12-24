# import re

# SKILLS = [
#     "Python", "Django", "Flask",
#     "Java", "Spring Boot",
#     "React", "React Js", "JavaScript",
#     "AWS", "SQL", "MySQL",
#     "REST API", "Microservices"
# ]


# def clean_text(text):
#     text = re.sub(r'\s+', ' ', text)
#     return text.strip()

# def extract_skills(text):
#     return [skill for skill in SKILLS if skill.lower() in text.lower()]

import json
import re

with open("skills.json", "r") as f:
    SKILL_DB = json.load(f)

ALL_SKILLS = set(
    skill.lower()
    for category in SKILL_DB.values()
    for skill in category
)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

def extract_skills(text):
    text = clean_text(text)
    found_skills = []

    for skill in ALL_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill.title())

    return sorted(set(found_skills))
