from flask import Flask, request, render_template
import os
from extract import extract_resume_data  # Import your parsing functions

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded.'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file.'
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # Call backend parsing function here
        parsed_data = extract_resume_data(filepath)
        return render_template('result.html', data=parsed_data)

if __name__ == "__main__":
    app.run(debug=True)
