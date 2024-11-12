from Data_loader import diesel_df
import pandas as pd
import numpy as np
from itertools import combinations
from itertools import product

def calculate_average(data_of_interest, column_name):
    if column_name in data_of_interest.columns:
        average = data_of_interest[column_name].mean()
        return average
    else:
        raise ValueError(f"Column '{column_name}' does not exist.")
average_R1 = calculate_average(diesel_df, 'R1')

print(f"Average is: {average_R1}")

# Visa datan
#print(diesel_df.head())
#print(diesel_df.info())
#print(diesel_df.dtypes)
#print(diesel_df.describe())

# Create an empty list to store the results
distance_results = []

for material, group in diesel_df.groupby('Material'):
    for (idx1, row1), (idx2, row2) in combinations(group.iterrows(), 2):
        # Calculate Euclidean distance for columns 'R1', 'R2', 'R3'
        distance = np.sqrt((row1['R1'] - row2['R1'])**2 + 
                           (row1['R2'] - row2['R2'])**2 + 
                           (row1['R3'] - row2['R3'])**2)
        
        # Append the result to the list
        distance_results.append({
            'Material': material,
            'Comparison': f"{int(row1['Replicate'])} vs {int(row2['Replicate'])}",
            'Distance': distance
        })

# Convert the list of results to a DataFrame
distance_within_df = pd.DataFrame(distance_results)
distance_within_df['Type'] = 'Within'

# Display the result
print(distance_within_df)


# Create an empty list to store the results
distance_results = []

for (mat1, mat2) in product(diesel_df['Material'].unique(), repeat=2):
    if mat1 != mat2:  # Ensure comparisons are only between different materials
        group1 = diesel_df[diesel_df['Material'] == mat1]
        group2 = diesel_df[diesel_df['Material'] == mat2]

        for (idx1, row1), (idx2, row2) in product(group1.iterrows(), group2.iterrows()):
            distance = np.sqrt((row1['R1'] - row2['R1'])**2 +
                               (row1['R2'] - row2['R2'])**2 +
                               (row1['R3'] - row2['R3'])**2)
            
            # Append the result to the list
            distance_results.append({
                'Material_1': mat1,
                'Replicate_1': row1['Replicate'],
                'Material_2': mat2,
                'Replicate_2': row2['Replicate'],
                'Distance': distance
            })

# Convert the list of results to a DataFrame
distance_between_df = pd.DataFrame(distance_results)
distance_between_df['Type'] = 'Between'

# Display the result
print(distance_between_df)