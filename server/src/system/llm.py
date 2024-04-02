import google.generativeai as genai

class LLMInterface:
    def __init__(self):
        self.api_key = "AIzaSyCZhx0KWK_VvbpkSKq9sk-Bb4LLRoUPyJg"
        self.model = None
        self.configure_llm("gemini-1.0-pro")

    def configure_llm(self, model_name):
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH"
            },
        ]

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config, safety_settings=safety_settings)

    def generate_response(self, prompt):
        convo = self.model.start_chat(history=[])
        convo.send_message(prompt)
        return convo.last.text
        # print(convo.last.text)