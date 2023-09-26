
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv(r'C:\Users\msubh\Downloads\dataset - netflix1.csv') 

# Display basic information about the dataset
print("Dataset shape:", df.shape)
print("Columns:", df.columns)
print("Sample data:")
print(df.head())

df.fillna(df.mean(), inplace=True)

z_scores = np.abs(stats.zscore(df))
df_cleaned = df[(z_scores < 3).all(axis=1)] 


print("\nCleaned Dataset shape:", df_cleaned.shape)
print("Columns in cleaned dataset:", df_cleaned.columns)
print("Sample cleaned data:")
print(df_cleaned.head())

df_cleaned.to_csv('cleaned_dataset.csv', index=False)
print("Cleaned dataset saved as cleaned_dataset.csv")