import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import joblib

# Load the train set
train_path = './server/data/train.csv'
train_df = pd.read_csv(train_path)

# Define pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),  # You can use TF-IDF or other vectorizers as well
    ('classifier', SVC())  # Support Vector Classifier (SVC)
])

# Train the model
X_train = train_df['Prompt']
Y_train = train_df['Flag']
model.fit(X_train, Y_train)

# Save trained model
model_path = "./server/src/models/svm_model.pkl"
joblib.dump(model, model_path)