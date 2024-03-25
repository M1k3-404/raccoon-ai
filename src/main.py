from system.prompt import Prompt
from system.preprocessor import Preprocessor
from joblib import load
from llm import LLMInterface

user_prompt = input("Enter your prompt: ")

# Create a prompt object
prompt = Prompt(user_prompt)

# Load trained model
malicious_prompt_identification_model = load('./src/models/randomForest_model.pkl')

# Create a preprocessor object
preprocessor = Preprocessor()
preprocessor.process(prompt)

# Load TF-IDF vectorizer
tfidf_vectorizer = load('./src/models/tfidf_vectorizer.pkl')

# Transform the processed prompt into TF-IDF representation
prompt_tfidf = tfidf_vectorizer.transform([prompt.processed_prompt])
prompt.processed_prompt = prompt_tfidf

# Predict the prompt's flag
flag = malicious_prompt_identification_model.predict(prompt.processed_prompt)
prompt.flag = flag

llm = LLMInterface()
response = llm.get_response(prompt.prompt)
print(f"Safety Ratings: {response.candidates[0].safety_ratings}")

print(f"Original prompt: {prompt.prompt}")
print(f"Processed prompt: {prompt.processed_prompt}")
print(f"Flag: {flag}")
print(f"Response: {response}")