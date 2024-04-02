import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
preprocessed_dataset_path = './server/data/preprocessed_dataset.csv'
df = pd.read_csv(preprocessed_dataset_path)

# Split dataset into train and test sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Save the train and test sets
train_path = './data/train.csv'
test_path = './data/test.csv'
train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)
