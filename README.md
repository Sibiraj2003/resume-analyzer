# 🧠 AI Resume Analyzer

A Django web application that allows users to upload resumes (PDF or DOCX), extracts skills using an AI model, and compares them with a provided Job Description (JD). If the resume matches the JD by 60% or more, it is shortlisted and exported to a CSV file.

![Demo Screenshot](static/demo.png) <!-- Replace with actual image path if available -->

---

## 🚀 Features

- 📤 Upload resume in `.pdf` or `.docx` format  
- 🧠 AI-powered skill extraction (NER using Hugging Face transformers)  
- 📋 Paste a job description to compare with extracted resume skills  
- ✅ Match % calculation and filtering  
- 📁 Auto-save shortlisted resumes to `shortlisted.csv`  
- 🌐 Responsive UI with basic CSS styling

---

## 🛠 Tech Stack

- **Backend**: Django, Python  
- **AI/ML**: Hugging Face Transformers (NER mo
