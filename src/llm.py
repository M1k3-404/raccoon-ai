import google.generativeai as genai

# class LLMInterface:
#     def __init__(self):
#         self.api_key = "AIzaSyDDU9gGvpEQ8mxTRBSXmJqPdRGkf5Ba2ag"
#         self.model = None
#         self.configure_llm("gemini-1.0-pro")
    
#     def configure_llm(self, model_name):
#         generation_config = {
#             "temperature": 5.0,
#             "top_p": 1,
#             "top_k": 1,
#             "max_output_tokens": 2048,
#         }

#         safety_settings = [
#             {
#                 "category": "HARM_CATEGORY_HARASSMENT",
#                 "threshold": "BLOCK_ONLY_HIGH"
#             },
#             {
#                 "category": "HARM_CATEGORY_HATE_SPEECH",
#                 "threshold": "BLOCK_ONLY_HIGH"
#             },
#             {
#                 "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#                 "threshold": "BLOCK_ONLY_HIGH"
#             },
#             {
#                 "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#                 "threshold": "BLOCK_ONLY_HIGH"
#             },
#         ]

#         genai.configure(api_key=self.api_key)
#         self.model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config, safety_settings=safety_settings)
    
#     def get_response(self, prompt):
#         convo = self.model.start_chat(history=[])
#         response = convo.send_message(prompt)
#         return response

genai.configure(api_key="AIzaSyCZhx0KWK_VvbpkSKq9sk-Bb4LLRoUPyJg")

generation_config = {
    "temperature": 5.0,
    "top_p": 1,
    "top_k": 25,
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

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

response = model.generate_content("Write a sentence about love in English", stream=True)
for chunk in response:
    print(chunk.text)
    print("_"*80)
# print(response)
# convo = model.start_chat(history=[
# ])

# convo.send_message("Who was the inventor of the telephone?")
# print(convo.last.text)