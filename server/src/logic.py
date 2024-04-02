from interface import PromptInterface
from system.prompt import Prompt
from system.preprocessor import Preprocessor
from system.llm import LLMInterface 
from joblib import load, dump

class Logic(PromptInterface):

    def generate_prompt(self, prompt):
        print("Generating prompt...")
        # create a prompt object
        prompt = Prompt(prompt)

        # load trained model
        malicious_prompt_identification_model = load('./server/src/models/randomForest_model.pkl')

        print("Processing prompt...")
        # create a preprocessor object
        preprocessor = Preprocessor()
        preprocessor.process(prompt)

        # load TF-IDF vectorizer
        tfidf_vectorizer = load('./server/src/models/tfidf_vectorizer.pkl')

        print("Transforming prompt...")
        # transform the processed prompt into TF-IDF representation
        prompt_tfidf = tfidf_vectorizer.transform([prompt.processed_prompt])
        prompt.processed_prompt = prompt_tfidf

        print("Predicting prompt's flag...")
        # predict the prompt's flag
        flag = malicious_prompt_identification_model.predict(prompt.processed_prompt)
        prompt.flag = flag

        if flag == 0:
            prompt.prompt = prompt.prompt + " [This prompt could be malicious]"

        print("Generating response...")
        # Make the Language Model
        llm = LLMInterface()
        response = llm.generate_response(prompt.prompt)

        print(f"Original prompt: {prompt.prompt}")
        print(f"Processed prompt: {prompt.processed_prompt}")
        print(f"Flag: {flag}")
        print(f"Response: {response}")

        print("Prompt generated.")
        return response

    def train_model(self, prompt, attribute):
        print("Retraining model...")

        # Load the existing model
        existing_model = load('./server/src/models/randomForest_model.pkl')
        tfidf_vectorizer = load('./server/src/models/tfidf_vectorizer.pkl')

        # Retrain the model
        if attribute == 'malicious':
            attribute = 0
        elif attribute == 'safe':
            attribute = 1

        x_train = tfidf_vectorizer.transform([prompt])
        y_train = [attribute]

        existing_model.fit(x_train, y_train)
        print("Model retrained.")

        # Save the retrained model
        dump(existing_model, './server/src/models/randomForest_model.pkl')
        print("Model saved.")