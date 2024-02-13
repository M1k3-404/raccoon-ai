import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    
    def process(self, prompt):
        # Tokenization and Lowercasing
        tokens = word_tokenize(prompt.prompt.lower())

        # Remove punctuation and special characters
        tokens = [word.translate(str.maketrans('', '', string.punctuation)) for word in tokens]

        # Remove stopwords
        tokens = [word for word in tokens if word not in self.stop_words]

        # Lemmatization
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]

        # Join tokens back into text
        processed_prompt = str(' '.join(tokens))

        prompt.processed_prompt = processed_prompt
