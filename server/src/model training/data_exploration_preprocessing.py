import pandas as pd
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
dataset_path = "./server/data/final_dataset.csv"
df = pd.read_csv(dataset_path, encoding='utf-8', encoding_errors='ignore')

# Display the first few rows of the dataset
# print(df.head())

# Get basic information about the dataset
# print(df.info())

# Summary statistics
# print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Explore categorical variables
#print(df['ID'].value_counts())
#print(df['Prompt'].value_counts())
#print(df['Flag'].value_counts())

# Preprocessing
# Preprocessing Prompts column
# Tokenization and Lowercasing
df['Prompt'] = df['Prompt'].apply(lambda x: x.lower().split())

#Remove punctutation and special characters
df['Prompt'] = df['Prompt'].apply(lambda x: [word.translate(str.maketrans('', '', string.punctuation)) for word in x])

# Remove stop words
stop_words = set(stopwords.words('english'))
df['Prompt'] = df['Prompt'].apply(lambda x: [word for word in x if word not in stop_words])

# Lemmatization
lemmatizer = WordNetLemmatizer()
df['Prompt'] = df['Prompt'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

# Join tokens back into a single string
df['Prompt'] = df['Prompt'].apply(lambda x: ' '.join(x))

# Preprocessing Flag column
# Convert 'Flag' column to numerical values
label_encoder = LabelEncoder()
df['Flag'] = label_encoder.fit_transform(df['Flag'])

# Save the cleaned dataset
preprocessed_dataset_path = "./server/data/preprocessed_dataset.csv"
df.to_csv(preprocessed_dataset_path, index=False)