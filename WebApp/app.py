from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from resume_parser import extract_text_from_file
from ai_model import get_resume_score_and_skills

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'backend/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def upload_files():
    jd_file = request.files['job_description']
    resumes = request.files.getlist('resumes')

    jd_path = os.path.join(UPLOAD_FOLDER, jd_file.filename)
    jd_file.save(jd_path)
    jd_text = extract_text_from_file(jd_path)

    results = []
    for resume in resumes:
        resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
        resume.save(resume_path)
        resume_text = extract_text_from_file(resume_path)

        match_score, skills, suggestions = get_resume_score_and_skills(jd_text, resume_text)

        results.append({
            'filename': resume.filename,
            'match_score': round(match_score, 2),
            'skills': skills,
            'suggestions': suggestions
        })

    return jsonify({'results': results})



if __name__ == '__main__':
    app.run(debug=True)