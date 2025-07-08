import spacy

# Load the small English spaCy model
nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = {
    "Python", "Django", "SQL", "HTML", "CSS", "HTML & CSS",
    "Machine Learning", "Git", "GitHub", "Git & GitHub", "Communication",
    "PostgreSQL", "Flask", "NumPy", "Pandas", "TensorFlow", "Java", "C++"
}

def extract_skills(text):
    doc = nlp(text)
    detected_skills = set()

    for token in doc:
        for skill in COMMON_SKILLS:
            if skill.lower() == token.text.lower():
                detected_skills.add(skill)

    # Check for full text matches (multi-word skills like "Machine Learning")
    for skill in COMMON_SKILLS:
        if skill.lower() in text.lower():
            detected_skills.add(skill)

    return sorted(detected_skills)
