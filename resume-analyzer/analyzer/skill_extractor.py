from transformers import pipeline

nlp_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

COMMON_SKILLS = {
    "Python", "Django", "SQL", "HTML", "CSS", "HTML & CSS",
    "Machine Learning", "Git", "GitHub", "Git & GitHub", "Communication",
    "PostgreSQL", "Flask", "NumPy", "Pandas", "TensorFlow", "Java", "C++"
}

def extract_skills(text):
    results = nlp_pipeline(text)
    raw_tokens = [entity["word"].strip("##") for entity in results]

    # Also scan the full text for known skills
    detected_skills = set()

    for skill in COMMON_SKILLS:
        if skill.lower() in text.lower():
            detected_skills.add(skill)

    # Also add any AI-model-detected tokens that match known skills
    for token in raw_tokens:
        if token in COMMON_SKILLS:
            detected_skills.add(token)

    return sorted(detected_skills)
