import pandas as pd

diesel_df = pd.read_csv('multivariate_diesel.csv', delimiter=';')

print(diesel_df.head())
print(diesel_df.info())

CNN_df = pd.read_csv('test_scores_100.csv', delimiter=',')
CNN_df['is_same_substances?'] = CNN_df['is_same_substances?'].astype(str)

print(CNN_df.head())
print(CNN_df.info())
