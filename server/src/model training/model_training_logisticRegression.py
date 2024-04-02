import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the train set
train_path = './server/data/train.csv'
train_df = pd.read_csv(train_path)

# Create a pipeline
model = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression()
)

# Train the model
X_train = train_df['Prompt']
Y_train = train_df['Flag']
model.fit(X_train, Y_train)

# Save trained model
model_path = "./server/src/models/logisticRegression_model.pkl"
joblib.dump(model, model_path)