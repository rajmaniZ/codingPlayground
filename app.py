from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import subprocess

app = Flask(__name__)

# Set up absolute path to DB file
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'codes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Editor page
@app.route('/', methods=['GET', 'POST'])
def editor():
    if request.method == 'POST':
        action = request.form.get('action')
        code = request.form.get('code', '')

        if action == 'save':
            # Saving the new code to the database
            name = f"Version {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"
            new_code = Code(name=name, code=code)
            db.session.add(new_code)
            db.session.commit()
            return redirect('/versions')

        elif action == 'run':
            # Writing the user code to a temp file
            with open('temp_code.py', 'w') as f:
                f.write(code)
            
            try:
                # Running the code using subprocess and capturing output
                result = subprocess.run(
                    ['python', 'temp_code.py'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=5
                )
                output = result.stdout + result.stderr
            except subprocess.TimeoutExpired:
                output = "⏱️ Code execution timed out!"
            except Exception as e:
                output = f"❌ Error: {e}"

            return render_template('editor.html', old_code=code, output=output)

    return render_template('editor.html', old_code=None)


# Save code
@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']  # Get the filename
    code_content = request.form['code']  # Get the code content
    new_code = Code(name=name, code=code_content)  # Create a new Code object
    db.session.add(new_code)  # Add the new code to the database
    db.session.commit()  # Commit the transaction
    return redirect('/versions')  # Redirect to the versions page


@app.route('/versions')
def versions():
    all_codes = Code.query.order_by(Code.timestamp.desc()).all()
    return render_template('versions.html', codes=all_codes)

# Load a saved version
@app.route('/load/<int:id>')
def load(id):
    code_item = Code.query.get_or_404(id)
    return render_template('editor.html', old_code=code_item.code)

# Delete a saved version
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    code_item = Code.query.get_or_404(id)
    db.session.delete(code_item)
    db.session.commit()
    return redirect('/versions')

# Entry point — create DB file and run app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create table if not exists
    app.run(debug=True)

