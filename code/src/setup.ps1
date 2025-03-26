Write-Host "Setting up environment..."

# Create virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..."
pip install -r code\requirements.txt

# Authenticate to Google Cloud
Write-Host "Authenticating to Google Cloud..."
gcloud auth application-default login

Write-Host "Setup complete! You can now run 'python code/src/app.py'."