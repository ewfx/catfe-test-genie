#!/bin/sh
echo "Setting up environment..."

# Detect OS and set appropriate activation command
if [ "$(uname)" = "Darwin" ] || [ "$(uname)" = "Linux" ]; then
    # macOS/Linux
    python3 -m venv venv
    . venv/bin/activate
elif [ "$(uname -s | cut -c 1-5)" = "MINGW" ] || [ "$(uname -s | cut -c 1-5)" = "CYGWI" ]; then
    # Windows (Git Bash)
    python -m venv venv
    . venv/Scripts/activate
else
    echo "Unsupported OS. On Windows, use PowerShell and run 'src/setup.ps1' instead."
    echo "On macOS/Linux, ensure you have a Bash-compatible shell."
    exit 1
fi

# Install dependencies
pip install -r code/requirements.txt

# Authenticate to Google Cloud
echo "Authenticating to Google Cloud..."
gcloud auth application-default login

echo "Setup complete! You can now run 'python code/src/app.py'."