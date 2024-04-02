import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the train set
train_path = './server/data/train.csv'
train_df = pd.read_csv(train_path)

# Load the test set
test_path = './server/data/test.csv'
test_df = pd.read_csv(test_path)

X_train = train_df['Prompt']
y_train = train_df['Flag']
X_test = test_df['Prompt']
y_test = test_df['Flag']

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the text data to numerical vectors
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Initialize the random forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier on the training data
model.fit(X_train_tfidf, y_train)

# Make predictions on the TF-IDF transformed test set
y_pred = model.predict(X_test_tfidf)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Save the TF-IDF vectorizer to the models folder
vectorizer_path = './server/src/models/tfidf_vectorizer.pkl'
joblib.dump(tfidf_vectorizer, vectorizer_path)

# Save the model to the models folder
model_path = './server/src/models/randomForest_model.pkl'
joblib.dump(model, model_path)