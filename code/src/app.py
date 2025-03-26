import yaml
import re
import os
from flask import Flask, request, render_template, jsonify, send_file
from io import BytesIO
from cloud_service import GeminiClient, get_project_id
from prompt_handler import get_system_prompt, get_example_prompt

# Explicitly set the template folder
app = Flask(__name__, template_folder="../templates")

# Debug: Print the template folder path
print(f"Template folder: {app.template_folder}")

def load_config(config_path="code/config/config.yaml"):
    """Load configuration from YAML file."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def sanitize_filename(text):
    """Convert text into a safe filename by removing invalid characters."""
    return re.sub(r'[<>:"/\\|?*]', '_', text.strip())

# Load config and initialize client once at startup
config = load_config()
project_id = get_project_id(config)
gemini_client = GeminiClient(config)
system_prompt = get_system_prompt(config)
example_prompt = get_example_prompt(config)
full_system_prompt = system_prompt + "\n" + example_prompt

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('Received form data:', request.form)  # Debug log
        title = request.form.get('title', '').strip()
        jira_id = request.form.get('jira_id', '').strip()
        description = request.form.get('description', '').strip()
        acceptance_criteria = request.form.get('acceptance_criteria', '').strip()
        
        if not all([title, jira_id, description, acceptance_criteria]):
            return jsonify({
                'success': False,
                'error': "All fields (Title, ID, Description, Acceptance Criteria) are required."
            })

        # Combine Description and Acceptance Criteria for the model
        user_input = f"Description: {description}\nAcceptance Criteria:\n{acceptance_criteria}"

        # Generate test cases
        test_cases = gemini_client.generate_test_cases(full_system_prompt, user_input)

        # Check if the response indicates an error
        if test_cases.startswith("Error:"):
            return jsonify({
                'success': False,
                'error': test_cases
            })

        # Create the .feature file content with feature details in JIRA format
        feature_content = f"""
Feature: {title}
  Jira ID: {jira_id}

  Description: {description}

  Acceptance Criteria:
  {acceptance_criteria}

{test_cases.strip()}
"""

        # Use Jira ID for filename and store it temporarily
        filename = f"{sanitize_filename(jira_id)}.feature"
        file_path = os.path.join(app.root_path, 'downloads', filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(feature_content)

        return jsonify({
            'success': True,
            'file_url': f"/download/{filename}"
        })

    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(app.root_path, 'downloads', filename)
    if os.path.exists(file_path):
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='text/plain'
        )
    return "File not found", 404

if __name__ == "__main__":
    print(f"Using project: {project_id}")
    app.run(debug=True, host='0.0.0.0', port=5000)