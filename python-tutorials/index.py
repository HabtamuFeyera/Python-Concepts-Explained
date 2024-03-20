# index.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tutorial.html', tutorial_title='Welcome', tutorial_content='<p>Select a tutorial from the navigation bar</p>')

@app.route('/<tutorial>')
def show_tutorial(tutorial):
    try:
        with open(f'tutorials/{tutorial}.md', 'r') as f:
            tutorial_content = f.read()
            return render_template('tutorial.html', tutorial_title=tutorial.replace('_', ' ').title(), tutorial_content=tutorial_content)
    except FileNotFoundError:
        return render_template('tutorial.html', tutorial_title='Error', tutorial_content='<p>Tutorial not found</p>')

if __name__ == '__main__':
    app.run(debug=True)
