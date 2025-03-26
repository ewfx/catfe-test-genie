import vertexai
from vertexai.generative_models import GenerativeModel, HarmCategory, HarmBlockThreshold

class GeminiClient:
    def __init__(self, config):
        self.project_id = config["google_cloud"]["project_id"]
        self.region = config["google_cloud"]["region"]
        self.model_id = config["google_cloud"]["model_id"]
        
        # Initialize Vertex AI with project and location
        vertexai.init(project=self.project_id, location=self.region)
        
        # Initialize the Gemini model
        self.model = GenerativeModel(self.model_id)
        
        # Load safety settings from config
        safety_settings_config = config.get("safety_settings", [])
        self.safety_settings = {}
        for setting in safety_settings_config:
            category = getattr(HarmCategory, setting["category"])
            threshold = getattr(HarmBlockThreshold, setting["threshold"])
            self.safety_settings[category] = threshold
        
        # Load generation config
        generation_config = config.get("generation_config", {})
        self.generation_config = {
            "temperature": generation_config.get("temperature", 0.7),
            "top_p": generation_config.get("top_p", 0.9),
            "top_k": generation_config.get("top_k", 40),
        }

    def generate_test_cases(self, system_prompt, user_input):
        try:
            # Combine system prompt and user input
            prompt = f"{system_prompt}\n\n{user_input}"
            
            # Send the prompt to the Gemini model using generate_content
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config,
                safety_settings=self.safety_settings
            )
            
            # Extract the generated text from the response
            return response.text
        except Exception as e:
            return f"Error generating test cases: {str(e)}"

def get_project_id(config):
    return config["google_cloud"]["project_id"]