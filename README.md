# 🚀 TestGenie

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Future Roadmap](#future-roadmap)
- [Team](#team)s

---

## 🎯 Introduction
Welcome to **TestGenie**, an innovative AI-powered tool designed to revolutionize functional test case creation for banking systems. Built for the hackathon challenge *"Streamline software testing in regulated industries like banking by leveraging AI to reduce manual effort and improve accuracy."* TestGenie transforms Jira feature details into precise Gherkin test cases with zero-cost AI magic. By automating repetitive tasks, it saves time, enhances test coverage, and ensures compliance with banking standards—making testing faster, smarter, and more reliable.

## 🎥 Demo
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:
![Screenshot 1](link-to-image)

## 💡 Inspiration
In banking, software testing is a critical yet time-consuming process. Testers often spend hours manually crafting test cases, only for them to become obsolete with new regulations, emerging fraud tactics, or system updates. We’ve witnessed teams racing against deadlines, missing edge cases, delaying releases, and risking compliance failures. This inspired us: what if AI could instantly generate accurate, banking-specific test cases from feature descriptions? TestGenie was born to free testers from grunt work, letting them focus on strategy and innovation—ultimately making banking software safer and more efficient.

## ⚙️ What It Does
- **Dynamic Test Case Generation**: Converts Jira feature details (Title, ID, Description, Acceptance Criteria) into Gherkin-syntax test cases (Given, When, Then).
- **Banking Context Awareness**: Tailored for banking domains like payments (SWIFT ISO), fraud detection, loans, chatbots, and compliance (KYC, AML).
- **Web Interface**: A sleek form for inputting Jira details, with a "Generate" button that produces a downloadable `.feature` file named after the Jira ID.
- **Real-World Ready**: Simulates modern banking scenarios for practical, actionable tests.
- **User Feedback**: Displays a "Test case generation in progress" overlay during processing, enhancing the app-like experience.

## 🛠️ How We Built It
We tapped into Google Cloud Platform’s AI prowess, leveraging their $300 free trial to keep costs at zero. Here’s the recipe:
- **Experimental AI Model**: Used an experimental setup within Vertex AI to generate test cases without incurring charges, optimizing for hackathon constraints.
- **Python & Flask**: Python powers the backend logic, while Flask serves a lightweight, responsive web frontend.
- **Google Cloud Integration**: Vertex AI handles AI-driven test case generation, authenticated via Google Cloud SDK.
- **Modular Design**: Separated cloud services, prompt engineering, and execution for maintainability.
- **File Handling**: Generates and serves .feature files dynamically, stored temporarily for download.

## 🚧 Challenges We Faced
- **Cost Management**: Keeping costs at zero required creative use of an experimental model, limiting us to basic features but proving feasibility.
- **Prompt Engineering**: Tuning the AI to produce consistent, banking-specific Gherkin syntax across diverse use cases was a trial-and-error journey.

## 🏆 Accomplishments We're Proud Of
- **Zero-Cost AI**: Successfully leveraged an experimental model to deliver results without spending a dime.
- **Banking Relevance**: Built a tool that understands banking nuances, from fraud detection to compliance.
- **Hackathon Speed**: Went from concept to functional prototype in record time, with a polished UI to boot.
- **User Experience**: Added a loading overlay that makes the tool feel like a professional app, not just a script.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/catfe-test-genie.git
   ```
2. Change directory to git project folder `cd catfe-test-genie`
3. Install dependencies  
   Run the appropriate setup script based on your operating system:
  **Windows (PowerShell)**:
  ```powershell
  .\code\src\setup.ps1
  ```
  **macOS/Linux**:
  ```sh
  bash code/src/setup.sh
  ```
   - Sets up a virtual environment, installs dependencies, and authenticates with Google Cloud.
   - Follow the browser prompt to log in with your Google account.
4. Configure
   Update code/config/config.yaml with your Google Cloud project_id:
   ```yaml
   google_cloud:
      project_id: "your-project-id"
   ```
5. Enable Vertex AI API
   Before proceeding, ensure the Vertex AI API is enabled in your Google Cloud project.
   - Go to https://console.cloud.google.com/apis/library/vertexai.googleapis.com
   - Select your project and click 'Enable' if not already enabled.
6. Launch the App
**Windows (PowerShell)**: `python .\code\src\app.py`
**macOS/Linux**: `python ./code/src/app.py`
   - Visit http://localhost:5000 in your browser. There will be a external URL mentioned in Flask log as well which can be used.
   - Enter Jira details (Title, ID, Description, Acceptance Criteria), click "Generate," and download the .feature file.

## 🏗️ Tech Stack
- 🔹 Frontend: Flask (HTML, CSS, JavaScript)
- 🔹 Backend: Python
- 🔹 Cloud: Google Cloud Vertex AI (Experimental Model)
- 🔹 Libraries: google-cloud-aiplatform, pyyaml, flask
- 🔹 Other: Google Cloud SDK for authentication

## 🔮 Future Roadmap
- **Advanced AI**: Integrate a production-grade model for richer test cases (e.g., edge cases, negative scenarios).
- **Jira API Integration**: Pull feature details directly from Jira with authentication.
- **Multi-File Output**: Support zip files for multiple test cases per feature.
- **Customization**: Allow users to tweak Gherkin templates or add banking-specific rules.
- **Cloud Deployment**: Host on GCP for public access, with scalability in mind.

## 👥 Team
- **Amiya Kumar Sahu** - [GitHub](#) | [LinkedIn](#)
- **Prameela Tulugu** - [GitHub](#) | [LinkedIn](#)
- **Snehanjali Rowlo** - [GitHub](#) | [LinkedIn](#)
- **Sudeepa R** - [GitHub](#) | [LinkedIn](#)
- **Tejaswini K** - [GitHub](#) | [LinkedIn](#)
