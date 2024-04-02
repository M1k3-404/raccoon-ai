import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the train set
train_path = './server/data/train.csv'
train_df = pd.read_csv(train_path)

# Load the test set
test_path = './server/data/test.csv'
test_df = pd.read_csv(test_path)

X_train = train_df['Prompt']
Y_train = train_df['Flag']
X_test = test_df['Prompt']
Y_test = test_df['Flag']

# Define the vectorizer
vectorizer = CountVectorizer()

# Vectorize the train set
X_train_vectorized = vectorizer.fit_transform(X_train)

# Vectorize the test set
X_test_vectorized = vectorizer.transform(X_test)

# Create a Naive Bayes classifier
model = MultinomialNB()

# Train the classifier
model.fit(X_train_vectorized, Y_train)

# Evaluate the classifier
accuracy = accuracy_score(Y_test, model.predict(X_test_vectorized))
precision = precision_score(Y_test, model.predict(X_test_vectorized))
recall = recall_score(Y_test, model.predict(X_test_vectorized))
f1 = f1_score(Y_test, model.predict(X_test_vectorized))

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")

# Save trained model
model_path = "./server/src/models/naiveBayes_model.pkl"
joblib.dump(model, model_path)