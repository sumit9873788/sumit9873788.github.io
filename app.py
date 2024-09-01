from flask import Flask, request, redirect, url_for
import csv
import os
from git import Repo

app = Flask(__name__)
CSV_FILE_PATH = 'data.csv'
REPO_PATH = '/test_sumit'  # Update this to your local repository path
REPO_BRANCH = 'sumit9873788'  # Update this to your target branch gh repo clone sumit9873788/test_sumit

# Ensure the CSV file exists
if not os.path.exists(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Email'])

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    # Append data to CSV
    with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])

    # Push to GitHub
    repo = Repo(REPO_PATH)
    repo.git.add(CSV_FILE_PATH)
    repo.git.commit(m='Update CSV file with new data')
    repo.git.push('origin', REPO_BRANCH)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
