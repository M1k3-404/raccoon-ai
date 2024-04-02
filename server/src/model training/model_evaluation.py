import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from joblib import load

# Load preprocessed test dataset
test_dataset_path = "./server/data/test.csv"
test_df = pd.read_csv(test_dataset_path)

X_test = test_df['Prompt']
y_test = test_df['Flag'] 

# Load trained models
logistic_regression_model = load('./server/src/models/logisticRegression_model.pkl')
svm_model = load('./server/src/models/svm_model.pkl')

def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Evaluation results for {model_name} model:")
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1}")
    print("\n")

# Evaluate Logistic Regression model
evaluate_model(logistic_regression_model, X_test, y_test, "Logistic Regression")

# Evaluate SVC model
evaluate_model(svm_model, X_test, y_test, "SVC")

# Naive Bayes model was evaluated in the model_training_naiveBayes.py script
# Evaluation results for Naive Bayes model:
# Accuracy: 0.855
# Precision: 0.7456445993031359
# Recall: 0.9385964912280702
# F1-score: 0.8310679611650486