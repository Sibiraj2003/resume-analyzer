import fitz
import docx
import csv
import os
from django.shortcuts import render
from analyzer.forms import ResumeUploadForm
from analyzer.skill_extractor import extract_skills  # AI Skill extractor

def extract_text_from_pdf(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def upload_resume(request):
    extracted_text = ""
    extracted_skills = []
    matched_skills = []
    match_score = 0

    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        jd_text = request.POST.get('jd_text', '')  # 👈 Get JD from textarea

        if form.is_valid():
            file = form.cleaned_data['resume']
            filename = file.name.lower()

            if filename.endswith('.pdf'):
                extracted_text = extract_text_from_pdf(file)
            elif filename.endswith('.docx'):
                extracted_text = extract_text_from_docx(file)
            else:
                extracted_text = "Unsupported file format. Please upload PDF or DOCX."

            # Extract skills from resume and JD
            extracted_skills = extract_skills(extracted_text)
            jd_skills = extract_skills(jd_text)

            # Compare and calculate match
            matched_skills = list(set(extracted_skills) & set(jd_skills))
            total = len(jd_skills)
            match_score = int(len(matched_skills) / total * 100) if total else 0
            # CSV export if match is high enough
            if match_score >= 60:
                csv_path = os.path.join("shortlisted.csv")

                with open(csv_path, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)

                    # Write header only if file is new
                    if file.tell() == 0:
                        writer.writerow(["Resume File", "Extracted Skills", "Matched Skills", "Match %"])

                    writer.writerow([
                        filename,
                        ", ".join(extracted_skills),
                        ", ".join(matched_skills),
                        match_score
                    ])
    else:
        form = ResumeUploadForm()

    return render(request, 'upload.html', {
        'form': form,
        'extracted_text': extracted_text,
        'extracted_skills': extracted_skills,
        'matched_skills': matched_skills,
        'match_score': match_score,
    })
