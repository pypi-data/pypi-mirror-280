import google.generativeai as genai
import json
import os

class CognxCore:
    def __init__(self, api_key, config_file=None):
        # Set up the API key
        genai.configure(api_key=api_key)

        # If no config file is provided, create a default one
        if config_file is None:
            script_dir = os.path.dirname(__file__)
            config_file = os.path.join(script_dir, 'config.json')

            # Create a default config file if it doesn't exist
            if not os.path.exists(config_file):
                default_config = {
                    'model_name': 'gemini-1.5-pro-latest',
                    'generation_config': {
                        "temperature": 1,
                        "top_p": 1,
                        "top_k": 1,
                        # "max_output_tokens": 512,
                    },
                    'system_instruction': 'You are a virtual assistant, your job is to be as informative as possible. Try to be neutral on your answers.',
                    'safety_settings': [
                        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
                    ]
                }
                with open(config_file, 'w') as f:
                    json.dump(default_config, f, indent=4)

        # Load the configuration from the JSON file
        with open(config_file) as f:
            self.config = json.load(f)

        # Create a model
        self.model = genai.GenerativeModel(model_name=self.config['model_name'],
                                           generation_config=self.config['generation_config'],
                                           system_instruction=self.config['system_instruction'],
                                           safety_settings=self.config['safety_settings'])

    def generate_content(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
    
    def upload_to_gemini(self, path, mime_type=None):
        """Uploads the given file to Gemini.

        See https://ai.google.dev/gemini-api/docs/prompting_with_media
        """
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file